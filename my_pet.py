import time



pet_name =  "Fluffy"

hunger = 20
happiness = 50
sleepiness = 30  
played_with = True

while True:
    print(f"\nHello. I'm {pet_name} ") 
    time.sleep(1)
    print(f"Hunger {hunger}")
    time.sleep(1)
    print(f"Happiness {happiness}" )
    time.sleep(1)
    print(f"Sleepiness {sleepiness}")   
    time.sleep(1)
    print(f"Have we played today {played_with} ")

    action = input("What do you want to do? (feed/play/sleep/) ")

    if "feed" in action: 
        time.sleep(1)
        print("Choose what do you want to feed? Carrots, Pet Food, or Treats")
        food = input("Enter your choice: ")
        time.sleep(1)
        print("Very Yummy😋😋 ")
        hunger = 0 

    elif "play" in action:
        time.sleep(1)
        print(f"Time to play !!🥎🥎🐕🐈")
        print("Throwing the ball... ")
        time.sleep(3)
        happiness = happiness + 20
        sleepiness = sleepiness + 20
        played_with = True  
        print(f"{pet_name} fetched the ball !!")

    elif "sleep" in action: 
        time.sleep(1)
        print("Zzzzzzz... 💤💤")
        time.sleep(1)
        print("Zzzzzzz... 💤💤")
        time.sleep(1)
        print("Zzzzzzz... 💤💤")
        print(f"{pet_name} is fresh now !!")
        sleepiness = 0
        happiness = happiness + 10




    

