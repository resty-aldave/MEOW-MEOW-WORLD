import os
import sys, time
import random #maybe i'll delete this 
import math #maybe i'll delete this
from character import characters
from Question import lvl1

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def clear2 (delay = 2):
    time.sleep(delay)
    os.system("cls" if os.name == "nt" else "clear")


def loading(text="Loading", dots=3, delay=0.1):#change to 0.5
    print()
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

def paragraph(text, delay=0.1, color="\033[97m"):
    for char in text:
        sys.stdout.write(color + char + "\033[97m")
        sys.stdout.flush()
        time.sleep(delay)
    print()


def ask_question(question, correct_answer, stats):
    wronganswercount = 0
    #Ask a T/F question and update stats if wrong.
    while True:
        clear2()
        system_text(f"{question}?")
        ans = input("\n(T/F): ").upper()
        if ans not in ["T", "F"]:#change this when you add the story
            clear()
            print("Invalid input, type T or F only.\n")
            continue

        if ans == correct_answer:
            print("\n✅ Correct!\n")
            return True
        
        else:
            print("\n❌ Incorrect!\n")

            wronganswercount += 1

            # Minus HP
            DMG = 10*wronganswercount
            stats["HP"] -= DMG
            stats["HP"] += ((stats["DEF"]/100)*stats["HP"])
            print(f"{stats['NAME']} (Updated Stats)")
            for key, value in stats.items():
                if key != "NAME":
                    print(f"{key}:{round(value)}")
            print()

            if stats["HP"] <= 0:
                clear()
                print("\n💀 GAME OVER! You have no HP left.\n")
                print(f"{stats['NAME']} (Updated Stats)")
                print("HP: 0")
                for key, value in stats.items():
                    if key != "NAME":
                        pass
                        if key != "HP":
                            print(f"{key}: {value}")
                print()
                print()
                sys.exit()


def randomHpDeductionFighting(text, stats):

    system_text(text)

    DMG = random.randint(20, 25)
    stats["HP"] -= DMG
    stats["HP"] += ((stats["DEF"]/100)*stats["HP"])

    print(f"{stats['NAME']} (Updated Stats)")

    for key, value in stats.items():
        if key != "NAME":
            print(f"{key}:{round(value)}")
    print()

    if stats["HP"] <= 0:
        clear()
        print("\n💀 GAME OVER! You have no HP left.\n")
        print(f"{stats['NAME']} (Updated Stats)")
        print("HP: 0")
        for key, value in stats.items():
            if key != "NAME":
                pass
                if key != "HP":
                    print(f"{key}: {value}")
            print()
            print()
            sys.exit()


def levelcomplete(text, delay = 0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    clear2()
    print("\nExiting in:\n")
    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    print()
    sys.exit()

def title(text, delay=0.01, color="\033[94m"):#change to 0.5
    for char in text:
        sys.stdout.write(color + char + "\033[94m")
        sys.stdout.flush()
        time.sleep(delay)
    print()



clear()
welcome_text("Welcome to MEOW MEOW world! 🐈")
system_text("\nPlease select the world you want to play....",)
system_text2("\n1. Purrlantic Shores\n2. Whiskerwood Hollow\n3. Coming Soon...\n4. Coming Soon...\n5. Coming Soon...\n")
GameSelected = input("Enter world number to start: ")
clear()

#WORLD SELECTION
while True:  
    if GameSelected == "1":
        loading("Redirecting")

        system_text("Please select how many players\n")
        system_text2("1. One Player \n2. Two Player")
        HowManyPlayer = input("\nEnter your selected mode here: ")
        clear()

        #GAME MODE
        while True: 
            if HowManyPlayer == "1":
                clear()
                loading("Redirecting")

                system_text("Please select the LVL\n")
                system_text2("1. Level 1\n2. Level 2\n3. Level 3")
                LVLSelected = input("\nPlease enter the number of the level: ")
                clear()

                #LEVEL SELECTION
                while True: 
                    if LVLSelected == "1":
                        clear()
                        loading("Redirecting")

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
                            for Cnum, stats in characters.items():
                                if Character_1.upper() == stats["NAME"].upper():
                                    clear()
                                    loading("Redirecting")

                                    start("Game Start")
                                    system_text2(f"Starting World Number {GameSelected}")
                                    system_text2(f"Level {LVLSelected}")

                                    print(f"\n{stats['NAME']}")
                                    for key, value in stats.items():
                                        if key != "NAME":
                                            print(f"{key}: {value}")

                                    # STORY START
                                    loading("Starting", delay=1)


                                    #add a story here
                                    title("Dawn on the Shores")

                                    paragraph("\nThe morning sun rose slowly over the Purrlantic waves, \n" 
                                                "but the day already felt weak. On the cliffs of the Goldwhisker Highlands, \n" 
                                                "Lord Flufflebottom stood alone in exile. The sea wind blew through his fur \n" 
                                                "as he looked at a parchment with the names of traitors who had cast him out. \n" 
                                                "He asked himself if he should choose justice or revenge.")
                                    
                                    #boss level
                                    #put auto deduct health
                                    randomHpDeductionFighting("Fighting Wave 1\n", stats)
                                    
                                    clear2()
                                    

                                    paragraph("In the neon streets of Nyanctropolis, Whiskerbyte opened her eyes. \n"
                                              "A glowing file floated in front of her: PROJECT WHISKERBYTE: TERMINATE. \n"
                                              "For the first time, she felt real fear. Was she created as a mistake or as a weapon?")
                                    
                                    #boss level
                                    #put auto deduct health
                                    randomHpDeductionFighting("Fighting Wave 2\n", stats)

                                    clear2()
                                    
                                    paragraph("Deep inside Whimwood, Jinxpaw woke from her rest. The forest moved with her mood; \n" 
                                    "trees leaned down, rivers bubbled backward, and birds cried loudly in the sky. \n" 
                                    "Each breath she took made the Shores shake. No one knew the storm she might bring.")

                                    #boss level
                                    #put auto deduct health
                                    randomHpDeductionFighting("Fighting Wave 3\n", stats)
                                    
                                    clear2()
                                    
                                    
                                    paragraph("The day looked bright, but under the surface, the first cracks began to spread.")


                                    found = True
                                    break   # this will stop looping characters since we found one

                            if found:
                                break   # this exit character selection loop

                            else:
                                clear()
                                system_text("\nInvalid choice! Please try again.\n")
                                for Cnum, stats in characters.items():
                                    print(f"\n{stats['NAME']}")
                                    for key, value in stats.items():
                                        if key != "NAME":
                                            print(f"{key}: {value}")
                                Character_1 = input("\nEnter the name of your character: ")

                        # After quiz ends → go back to world selection question
                        levelcomplete("\nGame done, congratiolations on completing this level!!!🎉")


                    elif LVLSelected == "2":
                        clear()
                        system_text("Still in work")

                        back = input("\nDo you want to go back to Level Selection? (y/n): ")
                        if back.lower() == "y":
                            clear()
                            system_text("Please select the LVL\n")
                            system_text2("1. Level 1\n2. Level 2\n3. Level 3")
                            LVLSelected = input("\nPlease enter the number of the level: ")
                            continue   # go back to level selection

                        elif back.lower() == "n":
                            system_text("\nThanks for playing! Goodbye.")
                            sys.exit()


                    elif LVLSelected == "3":
                        clear()
                        system_text("Still in work")

                        back = input("\nDo you want to go back to Level Selection? (y/n): ")
                        if back.lower() == "y":
                            clear()
                            system_text("Please select the LVL\n")
                            system_text2("1. Level 1\n2. Level 2\n3. Level 3")
                            LVLSelected = input("\nPlease enter the number of the level: ")
                            continue   # go back to level selection

                        elif back.lower() == "n":
                            system_text("\nThanks for playing! Goodbye.")
                            sys.exit()

                    else:
                        clear()
                        system_text("\nInvalid choice! Please try again.\n")
                        system_text2("1. Level 1\n2. Level 2\n3. Level 3")
                        LVLSelected = input("\nPlease enter the number of the level: ")


            #Working in Progress
            elif HowManyPlayer == "2":
                clear()
                loading("Redirecting")
                #system_text("Select you Character\n")
                system_text("Still in work")
                
                back = input("\nDo you want to go back to Game Mode? (y/n): ")
                if back.lower() == "y":
                    clear()
                    system_text("Please select how many players")
                    system_text2("\n1. One Player \n2. Two Player")
                    HowManyPlayer = input("\nEnter your selected mode here: ")
                    continue #go back to game mode

                elif back.lower() == "n":
                    system_text("\nThanks for playing! Goodbye.")
                    sys.exit()

            else: 
                clear()
                system_text("Invalid choice! Please try again.\n")
                system_text2("1. One Player \n2. Two Player")
                HowManyPlayer = input("\nEnter your selected mode here: ")



    #Working in Progress
    elif GameSelected == "2":
        clear()
        loading("Redirecting")
        system_text(f"Starting World {GameSelected}...")
        system_text("\nStill in work")

        back = input("\nDo you want to go back to World Selection? (y/n): ")

        if back.lower() == "y":
            clear()
            system_text("\nPlease select the world you want to play....")
            system_text2("\n1. Purrlantic Shores\n2. Whiskerwood Hollow\n3. Coming Soon...\n4. Coming Soon...\n5. Coming Soon...\n")
            GameSelected = input("Enter world number to start: ")
            clear()
            continue   # go back to world selection

        elif back.lower() == "n":
                system_text("\nThanks for playing! Goodbye.")
                sys.exit()

    

#Onward is not playable!!!
    elif GameSelected == "3" or GameSelected == "4" or GameSelected == "5":
        clear()
        print("That world is not ready yet! Please choose again.\n")
        system_text2("1. Purrlantic Shores\n2. Whiskerwood Hollow\n3. Coming Soon...\n4. Coming Soon...\n5. Coming Soon...\n")
        GameSelected = input("Enter world number to start: ")
        clear()
        loading("Redirecting")

    else:
        clear()
        print("Invalid choice! Please try again.\n")
        system_text2("1. Purrlantic Shores\n2. Whiskerwood Hollow\n3. Coming Soon...\n4. Coming Soon...\n5. Coming Soon...\n")
        GameSelected = input("Enter world number to start: ")