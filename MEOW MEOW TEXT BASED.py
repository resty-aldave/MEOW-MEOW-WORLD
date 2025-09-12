import os
import sys, time
import random #maybe i'll delete this 
import math #maybe i'll delete this
from character import characters
from Question import lvl1

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def clear2 (delay = 3):
    time.sleep(delay)
    os.system("cls" if os.name == "nt" else "clear")


def loading(text="Loading", dots=3, delay=0.1):#change to 0.5
    for i in range(dots):
        sys.stdout.write("\r" + text + "." * (i+1))
        sys.stdout.flush()
        time.sleep(delay)
    clear()

def start(text, delay=0.01, color="\033[31m"):#change to 0.5
    for char in text:
        sys.stdout.write(color + char + "\033[31m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def welcome_text(text, delay=0.01, color="\033[92m"):#change to 0.5
    for char in text:
        sys.stdout.write(color + char + "\033[0m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def system_text(text, delay=0.01, color="\033[97m"):#change to 0.5
    for char in text:
        sys.stdout.write(color + char + "\033[97m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def system_text2(text, delay=0.01, color="\033[97m"):#change to 0.3
    for char in text:
        sys.stdout.write(color + char + "\033[97m")
        sys.stdout.flush()
        time.sleep(delay)
    print()

def ask_question(question, correct_answer, stats):
    wronganswercount = 0
    #Ask a T/F question and update stats if wrong.
    while True:
        system_text("Please wait...")
        clear2()
        ans = input(f"{question}? (T/F): ").upper()
        if ans not in ["T", "F"]:
            clear()
            print("Invalid input, type T or F only.\n")
            continue

        if ans == correct_answer:
            print("✅ Correct!\n")
            return True
        
        else:
            print("❌ Incorrect!\n")

            wronganswercount += 1

            # Deduct HP
            DMG = 10*wronganswercount
            stats["HP"] -= DMG
            print(f"{stats['NAME']} (Updated Stats)")
            for key, value in stats.items():
                if key != "NAME":
                    print(f"{key}: {value}")
            print()

            if stats["HP"] <= 0:
                print("\n💀 GAME OVER! You have no HP left.\n")
                sys.exit()

def levelcomplete(text, delay = 0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

    print("\nExiting in:\n")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print()
    sys.exit()



clear()
welcome_text("Welcome to MEOW MEOW world! 🐈")
system_text("\nPlease select the world you want to play....",)
system_text2("1. Purrlantic Shores\n2. Whiskerwood Hollow\n3. Coming Soon...\n4. Coming Soon...\n5. Coming Soon...\n")
GameSelected = input("Enter world number to start: ")
clear()

#WORLD SELECTION
while True:  
    if GameSelected == "1":
        loading("\nRedirecting")

        system_text("Please select how many players\n")
        system_text2("1. One Player \n2. Two Player")
        HowManyPlayer = input("\nEnter your selected mode here: ")
        clear()

        #GAME MODE
        while True: 
            if HowManyPlayer == "1":
                clear()
                loading("\nRedirecting")

                system_text("Please select the LVL\n")
                system_text2("1. Level 1\n2. Level 2\n3. Level 3")
                LVLSelected = input("\nPlease enter the number of the level: ")
                clear()

                #LEVEL SELECTION
                while True: 
                    if LVLSelected == "1":
                        clear()
                        loading("\nRedirecting")

                        system_text("Select you Character\n")

                        for name, stats in characters.items():
                            print(f"\n{stats['NAME']}")
                            for key, value in stats.items():
                                if key != "NAME":
                                    print(f"{key}: {value}")

                        Character_1 = input("\nEnter the name of your character: ")
                        clear()

                        #CHARACTER SELECTION
                        while True:
                            found = False
                            for name, stats in characters.items():
                                if Character_1.upper() == stats["NAME"].upper():
                                    clear()
                                    loading("\nRedirecting")

                                    start("Game Start")
                                    system_text2(f"Starting World Number {GameSelected}")
                                    system_text2(f"Level {LVLSelected}")

                                    print(f"\n{stats['NAME']}")
                                    for key, value in stats.items():
                                        if key != "NAME":
                                            print(f"{key}: {value}")

                                    # Quiz
                                    loading("\nStarting", delay=0.5)
                                    
                                    for key, qa in lvl1.items():
                                        ask_question(qa["question"], qa["answer"], stats)
                                        loading("Next", delay=1)

                                        





                                    found = True
                                    break   # stop looping characters since we found one

                            if found:
                                break   # exit character selection loop

                            else:
                                clear()
                                system_text("\nInvalid choice! Please try again.\n")
                                for name, stats in characters.items():
                                    print(f"\n{stats['NAME']}")
                                    for key, value in stats.items():
                                        if key != "NAME":
                                            print(f"{key}: {value}")
                                Character_1 = input("\nEnter the name of your character: ")

                        # After quiz ends → go back to world selection question
                        levelcomplete("Game done, congratiolations on completing this level!!!🎉")

                        back = input("\nDo MEOWyou want to go back to World Selection? (y/n): ")
                        if back.lower() == "y":
                            clear()
                            system_text("\nThanks for playing! Goodbye.")
                            break   # exit game

                        elif back.lower() == "n":
                            system_text("\nThanks for playing! Goodbye.")
                            break   # exit game


                    elif LVLSelected == "2":
                        clear()
                        system_text("\nStill in work")

                        back = input("\nDo you want to go back to Level Selection? (y/n): ")
                        if back.lower() == "y":
                            clear()
                            system_text("Please select the LVL\n")
                            system_text2("1. Level 1\n2. Level 2\n3. Level 3")
                            LVLSelected = input("Please enter the number of the level: ")
                            continue   # go back to level selection

                        elif back.lower() == "n":
                            system_text("\nThanks for playing! Goodbye.")
                            break   # exit game


                    elif LVLSelected == "3":
                        clear()
                        system_text("\nStill in work")

                        back = input("\nDo you want to go back to Level Selection? (y/n): ")
                        if back.lower() == "y":
                            clear()
                            system_text("Please select the LVL\n")
                            system_text2("1. Level 1\n2. Level 2\n3. Level 3")
                            LVLSelected = input("Please enter the number of the level: ")
                            continue   # go back to level selection

                        elif back.lower() == "n":
                            system_text("\nThanks for playing! Goodbye.")
                            break   # exit game

                    else:
                        clear()
                        system_text("\nInvalid choice! Please try again.\n")
                        system_text2("1. Level 1\n2. Level 2\n3. Level 3")
                        LVLSelected = input("\nPlease enter the number of the level: ")


            #Working in Progress
            elif HowManyPlayer == "2":
                clear()
                loading("\nRedirecting")
                #system_text("Select you Character\n")
                system_text("\nStill in work")
                
                back = input("\nDo you want to go back to Game Mode? (y/n): ")
                if back.lower() == "y":
                    clear()
                    system_text("Please select how many players\n")
                    system_text2("1. One Player \n2. Two Player")
                    HowManyPlayer = input("\nEnter your selected mode here: ")
                    continue #go back to game mode

                elif back.lower() == "n":
                    system_text("\nThanks for playing! Goodbye.")
                    break   # exit game

            else: 
                clear()
                system_text("Invalid choice! Please try again.\n")
                system_text2("1. One Player \n2. Two Player")
                HowManyPlayer = input("\nEnter your selected mode here: ")



    #Working in Progress
    elif GameSelected == "2":
        clear()
        loading("\nRedirecting")
        system_text(f"Starting World {GameSelected}...")
        system_text("\nStill in work")

        back = input("\nDo you want to go back to World Selection? (y/n): ")

        if back.lower() == "y":
            clear()
            system_text("\nPlease select the world you want to play....")
            system_text2("1. SWU School\n2. Philippines River\n3. Coming Soon...\n4. Coming Soon...\n5. Coming Soon...\n")
            GameSelected = input("Enter world number to start: ")
            continue   # go back to world selection

        elif back.lower() == "n":
            system_text("\nThanks for playing! Goodbye.")
            break   # exit game

    

#Onward is not playable!!!
    elif GameSelected == "3" or GameSelected == "4" or GameSelected == "5":
        clear()
        print("\nThat world is not ready yet! Please choose again.\n")
        system_text2("1. SWU School\n2. Philippines River\n3. Coming Soon...\n4. Coming Soon...\n5. Coming Soon...\n")
        GameSelected = input("Enter world number to start: ")
        clear()
        loading("Redirecting")

    else:
        clear()
        print("\nInvalid choice! Please try again.\n")
        system_text2("1. Purrlantic Shores\n2. Whiskerwood Hollow\n3. Coming Soon...\n4. Coming Soon...\n5. Coming Soon...\n")
        GameSelected = input("Enter world number to start: ")