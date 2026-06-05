import uuid
from typing import Dict, List, Optional
from collections import defaultdict
import json

class User:
    def __init__(self, name: str, email: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.email = email
        self.phone_numbers: List[str] = []

    def add_phone(self, phone: str):
        if phone not in self.phone_numbers:
            self.phone_numbers.append(phone)

    def __str__(self):
        return f"User({self.name}, {self.email})"

class Group:
    def __init__(self, name: str, admin: User):
        self.id = str(uuid.uuid4())
        self.name = name
        self.members: List[User] = [admin]
        self.admin = admin

    def add_member(self, user: User):
        if user not in self.members:
            self.members.append(user)

    def remove_member(self, user: User):
        if user != self.admin and user in self.members:
            self.members.remove(user)

    def __str__(self):
        return f"Group({self.name}, members: {[u.name for u in self.members]})"

class Split:
    def __init__(self, user: User, amount: float):
        self.user = user
        self.amount = amount

class Expense:
    def __init__(self, description: str, amount: float, payer: User, group: Group, splits: List[Split]):
        self.id = str(uuid.uuid4())
        self.description = description
        self.amount = amount
        self.payer = payer
        self.group = group
        self.splits = splits

    def validate(self):
        total_split = sum(s.amount for s in self.splits)
        if abs(total_split - self.amount) > 0.01:
            raise ValueError("Split amounts do not add up to total expense")

class BalanceManager:
    def __init__(self):
        self.balances: Dict[str, Dict[str, float]] = defaultdict(lambda: defaultdict(float))

    def add_expense(self, expense: Expense):
        for split in expense.splits:
            if split.user != expense.payer:
                self.balances[split.user.id][expense.payer.id] += split.amount
                self.balances[expense.payer.id][split.user.id] -= split.amount

    def get_balance(self, user1: User, user2: User) -> float:
        return self.balances[user1.id][user2.id]

    def get_net_balance(self, user: User) -> Dict[str, float]:
        net = defaultdict(float)
        for debtor_id, amount in self.balances[user.id].items():
            net[debtor_id] = amount
        for creditor_id, creditors in self.balances.items():
            if user.id in creditors:
                net[creditor_id] -= creditors[user.id]
        return dict(net)

    def simplify_debts(self) -> List[tuple]:
        # Simple debt simplification: calculate net owed and settle
        net_balances = {}
        for user_id in self.balances:
            net = 0
            for owed_to, amount in self.balances[user_id].items():
                net += amount
            net_balances[user_id] = net

        creditors = [(uid, amt) for uid, amt in net_balances.items() if amt > 0]
        debtors = [(uid, -amt) for uid, amt in net_balances.items() if amt < 0]

        settlements = []
        i, j = 0, 0
        while i < len(creditors) and j < len(debtors):
            creditor, credit_amt = creditors[i]
            debtor, debt_amt = debtors[j]
            settle_amt = min(credit_amt, debt_amt)
            settlements.append((debtor, creditor, settle_amt))
            creditors[i] = (creditor, credit_amt - settle_amt)
            debtors[j] = (debtor, debt_amt - settle_amt)
            if creditors[i][1] == 0:
                i += 1
            if debtors[j][1] == 0:
                j += 1
        return settlements

class Settlement:
    def __init__(self, from_user: User, to_user: User, amount: float):
        self.from_user = from_user
        self.to_user = to_user
        self.amount = amount

    def apply(self, balance_manager: BalanceManager):
        balance_manager.balances[self.from_user.id][self.to_user.id] -= self.amount
        balance_manager.balances[self.to_user.id][self.from_user.id] += self.amount

class ExpenseSharingSystem:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.groups: Dict[str, Group] = {}
        self.expenses: List[Expense] = []
        self.balance_manager = BalanceManager()
        self.settlements: List[Settlement] = []

    def create_user(self, name: str, email: str) -> User:
        if email in [u.email for u in self.users.values()]:
            raise ValueError("Email already exists")
        user = User(name, email)
        self.users[user.id] = user
        return user

    def create_group(self, name: str, admin: User) -> Group:
        group = Group(name, admin)
        self.groups[group.id] = group
        return group

    def add_expense(self, description: str, amount: float, payer: User, group: Group, split_type: str, split_data: Dict):
        if split_type == "equal":
            participants = split_data.get("participants", group.members)
            split_amount = amount / len(participants)
            splits = [Split(u, split_amount) for u in participants if u != payer]
        elif split_type == "exact":
            splits = [Split(u, amt) for u, amt in split_data.items() if u != payer]
        elif split_type == "percentage":
            splits = [Split(u, amount * pct / 100) for u, pct in split_data.items() if u != payer]
        else:
            raise ValueError("Invalid split type")

        expense = Expense(description, amount, payer, group, splits)
        expense.validate()
        self.expenses.append(expense)
        self.balance_manager.add_expense(expense)

    def record_settlement(self, from_user: User, to_user: User, amount: float):
        settlement = Settlement(from_user, to_user, amount)
        settlement.apply(self.balance_manager)
        self.settlements.append(settlement)

    def get_balances(self):
        return self.balance_manager.balances

    def get_simplified_settlements(self):
        return self.balance_manager.simplify_debts()

# CLI Interface
def main():
    system = ExpenseSharingSystem()

    # Create users
    ali = system.create_user("Ali", "ali@example.com")
    sara = system.create_user("Sara", "sara@example.com")
    ahmed = system.create_user("Ahmed", "ahmed@example.com")

    # Create group
    group = system.create_group("Friends", ali)
    group.add_member(sara)
    group.add_member(ahmed)

    # Add expenses
    system.add_expense("Dinner", 3000, ali, group, "equal", {})
    system.add_expense("Fuel", 1500, sara, group, "equal", {})

    # Print balances
    print("Balances:")
    for uid1, owes in system.get_balances().items():
        for uid2, amt in owes.items():
            if amt > 0:
                user1 = system.users[uid1]
                user2 = system.users[uid2]
                print(f"{user1.name} owes {user2.name}: {amt}")

    # Simplified settlements
    print("\nSimplified Settlements:")
    for debtor, creditor, amt in system.get_simplified_settlements():
        debtor_user = system.users[debtor]
        creditor_user = system.users[creditor]
        print(f"{debtor_user.name} pays {creditor_user.name}: {amt}")

if __name__ == "__main__":
    main()