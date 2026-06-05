

#Daily Task Planner


tasks = []

while True:
    task = input("Enter a task ")
    if task == "done":
        break
    tasks.append(task)
   

while True:
    print("1. View tasks")
    print("2. Complete a task")
    print("3. Enter another task")
    print("4. Exit")

    choice = input("Enter your choice ")

    if choice == "1": 
        print("============================================\n")
        print("Your tasks:")
        
        for task in tasks:
            print(task)
        print("============================================\n")

    elif choice == "2":  
        if len(tasks) == 0:
            print("No tasks to complete")
        else:
            print("============================================\n")
            print("Your tasks: ")

            for task in tasks:
                print(task)
            print("============================================\n")

            print("Enter the task number to complete: ")
            task_number = int(input()) - 1

            if 0 <= task_number < len(tasks):

                completed_task = tasks.pop(task_number)

                print(f"\nTask '{completed_task}' completed!\n")
            else:
                print("\nInvalid task number\n")
    
    elif choice == "3": 
        task = input("Enter a task " )
        tasks.append(task)
    
    elif choice == "4":
        print("Exiting...")
        break
