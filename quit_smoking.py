import sys
import os
from datetime import date
import json

'''

First we have to load the savefile.txt
Then we check the date_started time on line 1
Then we check the number on line 2.
The number represents the 

'''

# File will always be in the same dir for this program.
SAVE_FILENAME = "savefile.json"

if os.stat(SAVE_FILENAME).st_size == 0:
    clear = lambda: os.system('clear') #on Linux System
    clear()
    print("Ready to start the challenge? Let's go!")
    input("Press a key to continue...")
    clear = lambda: os.system('clear') #on Linux System
    clear()
    name = input("What is your name? ")
    goal = input("How many days will you go without smoking? ")
    reward = input(f"What will be your reward at the end of your goal of {goal} days? ")

    config = {
        "name": name,
        "date_started": str(date.today()),
        "days": 0,
        "goal": int(goal),
        "reward": reward,
    }

    with open(SAVE_FILENAME, 'r+') as json_file:
        json.dump(config, json_file)
        
with open(SAVE_FILENAME, 'r') as json_file:
    data = json.load(json_file)
    if data['days'] == data['goal']:    
        clear = lambda: os.system('clear') #on Linux System
        clear()
        print(f"You are a legend! You made it {data['days']} days without smoking!")
        print(f"You've earned your reward: {data['reward']}")
        input("")
        clear = lambda: os.system('clear') #on Linux System
        clear()
        sys.exit()
    else:
        json_file.close()
        clear = lambda: os.system('clear') #on Linux System
        clear()


        print(f"Current Streak: {data['days']} day(s)")

        question = "Did you smoke or vape today? "

        answer = input(question)

        answer = answer.lower()

        if answer == 'no' or answer == 'yes':
            if answer == 'no':
                with open(SAVE_FILENAME, 'r+') as json_file:
                    data = json.load(json_file)
                    data['days'] += 1
                    clear = lambda: os.system('clear') #on Linux System
                    clear()
                    print(f"Awesome! Current Streak: {data['days']}. Only {str(data['goal'] - data['days'])} days to go!")
                    input("")
                    clear = lambda: os.system('clear') #on Linux System
                    clear()

                with open(SAVE_FILENAME, 'r+') as json_file:
                    json.dump(data, json_file)
            else:
                with open(SAVE_FILENAME) as json_file:
                    data = json.load(json_file)
                    clear = lambda: os.system('clear') #on Linux System
                    clear()
                    print(f"Keep trying! You got this! You haven't smoked for: {data['days']} day(s)! You only had {str(data['goal'] - data['days'])} day(s) left! Don't give up!")
                    data['days'] = 0
                    input("")
                    clear = lambda: os.system('clear') #on Linux System
                    clear()

                with open(SAVE_FILENAME, 'r+') as json_file:
                    json.dump(data, json_file)

        else:
            print("Aborting... 3... 2...1.... Poof.")
            sys.exit()
