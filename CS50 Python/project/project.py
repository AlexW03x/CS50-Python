from classes import entity
from random import randint
import sys
import time
import random
import math

import names

##the turn-based game##
def main(): ##initialisation <create character>
    global level
    level = 1
    while True:#
        try:
            for i in range(0,100):
                print("\n") #to clear the terminal
            print("Welcome To Alex's Turn Based Game")
            print("=================================")
            print("        SELECT CHARACTER         ")
            print("=================================")
            print("| 1.       The Warrior          |")
            print("| 2.       The Wizard           |")
            print("| 3.       The Phantom          |")
            print("| 4.       The Rogue            |")
            print("=================================")
            user = int(input("Select A Character [1-4]: "))
            if user in [1,2,3,4]:
                break
        except ValueError:
            print("Incorrect Character Choice!")
            continue
        except EOFError:
            sys.exit("EOFError Executed!")

    if user == 1:
        createclass(1)
    elif user == 2:
        createclass(2)
    elif user == 3:
        createclass(3)
    elif user == 4:
        createclass(4)
    else:
        return


def createclass(classnum): ##creates our character class##
    global classtype
    if classnum == 1: ##warrior
        classtype = entity("The Warrior", 200 + (10 * level), 50 + (5 * level), "The Warrior is a power-house character that focuses on physical attacks and the weakpoint is his lack of mana", 15 + (2 * level), "Basic", "Heal", "Mana", "Raging Slash", 10)
    elif classnum == 2: ##wizard
        classtype = entity("The Wizard", 150 + (10 * level), 100 + (5 * level), "The Wizard is a strong spell-caster that focuses on magical attacks with the weakpoint being slow speed and lowered health", 10 + (2 * level), "Basic", "Heal", "Mana", "Flaming Mindbreaker", 1)
    elif classnum == 3: ##The phantom
        classtype = entity("The Phantom", 75 + (10 * level), 150 + (5 * level), "The Phantom is a mystical entity that haunts the living causing both physical and magical attacks, with the only weakpoint being its health", 8 + (2 * level), "Basic", "Heal", "Mana", "Crippling Haunt", 55)
    elif classnum == 4: ##The Rogue
        classtype = entity("The Rogue", 125 + (10 * level), 90 + (5 * level), "The Rogue is a stealthy assassin that practises survival skills with both physical and spell casting elements, the only weakpoint is the power they have", 5 + (2 * level), "Basic", "Heal", "Mana", "Poison Slash", 25)
    else:
        classtype = None

    while True:#
        print(classtype.getdesc())
        ans = input("Continue [Yes/No]?: ").lower()
        if ans == "yes":
            story()
            break
        elif ans == "no":
            main()
            break
        else:
            continue


def story(): ##gameplay
    global level
    global classtype

    enemy = getrandomenemy()
    ##story telling##
    scenario = ["city", "tower", "cave", "pits", "abyss", "grass fields", "desert", "mountains", "prison", "ocean", "house", "hospital", "battlegrounds", "fortress", "camp", "basement"]
    while True:#
        for i in range(0,100):
            print("\n")
        print("You arrive at the " + scenario[random.randint(0, len(scenario)-1)] + " to find an enemy known as: " + enemy.getname())
        print("They are going to attack you!")
        print("=============================")
        print("= 1.      Fight Back        =")
        print("= 2.      Run Away..        =")
        print("=============================")

        try:
            ins = int(input("Option: "))
            if ins == 1 or 2:
                break
            else:
                continue
        except ValueError:
            continue
        except EOFError:
            sys.exit("EOFError Executed!")

    if ins == 1:
        ##begin battle##
        for i in range(0,100):
            print("\n")
        print("Battle Initiated!")

        x = random.randint(0,1)
        curTurn = "Self" if x == 0 else "Enemy" #determines first go

        while enemy.gethealth() > 0 and classtype.gethealth() > 0: #ensuring that the battle only occurs when we both have more than 0 health to show that we are not dead.
            ###if enemy goes first###
            if curTurn == "Enemy":
                print("\n"+enemy.getname() + " is attacking...")
                time.sleep(1)
                if enemy.gethealth() < enemy.getmaxhealth() / 1.5:
                    if enemy.getmana() == enemy.getmaxmana():
                        atk = 1 ##guaranteed heal##
                    if enemy.getmana() >= 40:
                        atk = random.randint(0,4)
                    elif enemy.getmana() >= 30:
                        atk = random.randint(0,3)
                    else:
                        atk = 0
                elif enemy.getmana() <= 10:
                    atk = 2 ##mana
                else:
                    if enemy.getmana() >= 40:
                        atk = random.randint(0,4)
                    elif enemy.getmana() >= 30:
                        atk = random.randint(0,3)
                    else:
                        atk = 0

                if atk == 0: #basic
                    dmg = int(round(enemy.getpower()))
                    enemy.setmana(round(enemy.getmana() + (enemy.getmaxmana()/10))) #replenish mana slowly
                    classtype.sethealth(classtype.gethealth() - dmg)
                    print(enemy.getname() + " uses " + enemy.getab1() + " dealing " + str(dmg) + "HP!")
                    print(enemy.getname() + " is now on: " + str(enemy.getmana()) + "MP!")
                    time.sleep(1)
                    print("You now have " + str(classtype.gethealth()) + " HP!")
                elif atk == 1: #heal
                    healamount = (round(enemy.gethealth()/5))
                    enemy.sethealth(enemy.gethealth() + healamount)
                    enemy.setmana(round(enemy.getmana() - 30))
                    print(enemy.getname() + " uses " + enemy.getab2() + " healing for " + str(healamount) + "HP!")
                    print(enemy.getname() + " is now on: " + str(enemy.gethealth()) + "HP!")
                    print(enemy.getname() + " is now on: " + str(enemy.getmana()) + "MP!")
                    time.sleep(1)
                elif atk == 2: #mana
                    mana = (round(enemy.getmana() + (enemy.getmaxmana()/2))) ##retrieve mana back fairly
                    enemy.setmana(mana)
                    print(enemy.getname() + " uses " + enemy.getab3() + " gaining " + str(mana) + "MP!")
                    print(enemy.getname() + " is now on: " + str(enemy.getmana()) + "MP!")
                    time.sleep(1)
                elif atk == 3: #strong attack
                    dmg = int(round(enemy.getpower() * 1.25))
                    classtype.sethealth(classtype.gethealth() - dmg)
                    enemy.setmana(round(enemy.getmana() - 40))
                    print(enemy.getname() + " uses " + enemy.getab4() + " dealing " + str(dmg) + "HP!")
                    print(enemy.getname() + " is now on: " + str(enemy.getmana()) + "MP!")
                    time.sleep(1)
                    print("You now have " + str(classtype.gethealth()) + " HP!")
                else: #revert to basic if value is beyond max
                    dmg = int(round(enemy.getpower()))
                    classtype.sethealth(classtype.gethealth() - dmg)
                    enemy.setmana(round(enemy.getmana() + (enemy.getmana()/10)))
                    print(enemy.getname() + " uses " + enemy.getab1() + " dealing " + str(dmg) + "HP!")
                    print(enemy.getname() + " is now on: " + str(enemy.getmana()) + "MP!")
                    time.sleep(1)
                    print("You now have " + str(classtype.gethealth()) + " HP!")

                time.sleep(1)
                ##set our go
                curTurn = "Self"

            if curTurn == "Self":
                print("\n" + classtype.getname() + ", You are attacking the enemy!")
                print("====================================")
                print("=       Choose Your Action         =")
                print("=       Your HP: " + str(classtype.gethealth()) + " MP: " + str(classtype.getmana()) + "        =")
                print("====================================")
                print("1. " + classtype.getab1() + " [0MP] ")
                print("2. " + classtype.getab2() + " [30MP] ")
                print("3. " + classtype.getab3() + " [10MP]")
                print("4. " + classtype.getab4() + " [40MP]")
                print("====================================")
                try:
                    youropt = int(input("Option: "))
                except ValueError:
                    pass
                except EOFError:
                    sys.exit("EOFError Executed!")
                if youropt == 1 or youropt == 2 or youropt == 3 or youropt == 4:
                    if youropt == 1: #basic attack
                        dmg = setdmg(classtype.getpower(), 1)
                        enemy.sethealth( enemy.gethealth() - dmg )
                        classtype.setmana(classtype.getmana() + round((classtype.getmaxmana()/10)))
                        print("You delt " + str(dmg) + " damage to " + enemy.getname())
                        print("You are now on: " + str(classtype.getmana()) + "MP!")
                        time.sleep(1)
                        print(enemy.getname() + " is now on: " + str(enemy.gethealth()) + "HP!")
                        time.sleep(1)
                        curTurn = "Enemy"
                    elif youropt == 2 and classtype.getmana() >= 30: #heal
                        healamount = int(round(classtype.getmaxhealth() / 2.5))
                        classtype.sethealth(classtype.gethealth() + healamount)
                        classtype.setmana(classtype.getmana() - 30)
                        print("You healed for: " + str(healamount) + "HP!")
                        print("You are now on: " + str(classtype.getmana()) + "MP!")
                        time.sleep(1)
                        curTurn = "Enemy"
                    elif youropt == 3 and classtype.getmana() >= 10: #mana
                        manaamount = int(round(classtype.getmaxmana() / 1.25))
                        classtype.setmana(manaamount)
                        print("You now have: " + str(classtype.getmana()) + "MP!")
                        time.sleep(1)
                        curTurn = "Enemy"
                    elif youropt == 4 and classtype.getmana() >= 40: #strong
                        dmg = setdmg(classtype.getpower(), 2)
                        enemy.sethealth(enemy.gethealth() - dmg)
                        classtype.setmana(classtype.getmana() - 40)
                        print("You delt " + str(dmg) + " damage to " + enemy.getname() + " using " + classtype.getab4())
                        print("You are now on: " + str(classtype.getmana()) + "MP!")
                        time.sleep(1)
                        print(enemy.getname() + " is now on: " + str(enemy.gethealth()) + "HP!")
                        time.sleep(1)
                        curTurn = "Enemy"
                else:
                    continue #make the user redo the input

        if enemy.gethealth() <= 0: #if enemy loses
            for i in range(0,100):
                print("\n")
            print("You won the battle against " + enemy.getname() + ", congrats...")
            level = level + 1 #increase difficulty
            while True:
                print("\n=================================")
                print("=        1. Next Level          =")
                print("=        2. Exit Game           =")
                print("=================================")
                ins = input("Your Option: ")
                if ins == 1 or ins == "1":
                    return story()
                    break
                elif ins == 2 or ins == "2":
                    sys.exit("You have exited the game!")
                    break
                else:
                    continue

        if classtype.gethealth() <= 0: #if we lose
            for i in range(0,100):
                print("\n")
            print("You lost the battle against " + enemy.getname() + ", unlucky...")
            while True:
                print("\n=================================")
                print("=        1. New Battle          =")
                print("=        2. Exit Game           =")
                print("=================================")
                ins = input("Your option: ")
                if ins == 1 or ins == "1":
                    return story()
                    break
                elif ins == 2 or ins == "2":
                    sys.exit("You have exited the game!")
                    break
                else:
                    continue
    elif ins == 2: ##retreat find new enemy
        return story()


def setdmg(pow, x):
    return int(round(pow * x))



def getrandomenemy(): ##creates randomised enemies
    global level
    randomstring = ["Warrior", "Archer", "Slayer", "Boxer", "Puntkicker", "Wrestler", "Mage", "Wizard", "Spellcaster", "Alchemist", "Brute", "Cryomancer", "Pyromancer", "Necromancer", "Goblin", "Rat", "Chupacabra", "Wolf", "Clone", "Zombie", "Unwanted", "Hustler", "Roidhead", "Enraged", "Corrupted", "Accused", "Prisoner", "Loyalist", "Painmaker", "Relentless", "Ogre"]
    basehealth = 200 + (35 * int(level))
    basemana = 50 + (5 * int(level))
    basepower = 10 + (2 * int(level))

    randomab = ["Super Strike", "Uppercut", "Burn", "Stomp", "Evaporate", "Poison", "Explode", "Rupture", "Grief", "Slap", "Super Punch", "Spear", "Jabs", "Dropkick", "Firestorm", "Icestorm", "Windstorm", "Sandstorm", "Lava Spray", "Water Choke"]
    enemy = entity(names.get_first_name() + " The " + randomstring[random.randint(0,len(randomstring)-1)], basehealth, basemana, "Is Enemy", basepower, "Basic", "Heal", "Mana", randomab[random.randint(0, len(randomab)-1)], random.randint(1, 50))

    return enemy

main()
