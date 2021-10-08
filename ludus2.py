### ludus v 0.2
### steven franken

### imports
from random import randint
from pcinput import *

def HitAnyKey():
    anykey = input("\nHit any key:")

def GladiatorFight (gladiators):
    ### define nr op oponents
    minimum = gladiators-2
    maximum = gladiators*50/100
    oponents = randint (gladiators-2, int(gladiators+maximum))
    ### calculate win or lose
    print ("out of the",gladiators, "gladiators that fought",oponents,"oponents")

    while gladiators >= 1:
        if oponents == 0:
            break
        if (randint(1,10)%2) == 0:
            oponents -=1
        else:
            gladiators -=1

    print (gladiators, "survived")
    return gladiators

def Market(gladiatordummy):
    global gold
    global reputation
    global gladiators
    sale = False

    gladiatorMarket = randint(1,30)
    gladiatorPrice = 10

    print ("\n >There are",gladiatorMarket,"gladiators available for sale")
    print ("gladiator price is",gladiatorPrice,"gold each")
    print ("You have ",gold,"at your disposal")
    print ("")
    while sale == False:
        purchace = getInteger("how many gladiators would you like to purchase ? ")
        if purchace > gladiatorMarket:
            print ("there are only",gladiatorMarket,"available please try again")
        elif ((purchace+gladiators*2)/2) < 4:
            print ("You wouldn't be able to feed your gladiators for 4 days")
            print ("Please try again")
        elif purchace*gladiatorPrice > gold:
            print ("You lack the required funds for that purchace")
            print ("Please try again")
        elif purchace == 0:
            break
        else:
            print ("You procured",purchace,"gladiators for",purchace*gladiatorPrice,"gold")
            gladiators+=purchace
            gold -= (purchace*gladiatorPrice)
            sale=True
    return gladiators

### setup
day = 0
gold = 1000
reputation = -100
gladiators = 10


### mainloop
while True:
    day +=1
    gold = gold - (gladiators*2)

    print ("###########################################################")
    print ("### Ludus                                               ###")
    print ("###########################################################")
    print ("### Day                    {:>6}                       ###".format(day))
    print ("### Gold                   {:>6}                       ###".format(gold))
    print ("### Reputation             {:>6}                       ###".format(reputation))
    print ("### Maintanance per day    {:>6}                       ###".format(gladiators*2))
    print ("### nr of gladiators       {:>6}                       ###".format(gladiators))
    print ("###########################################################")
    print ("### (g)o to market                                      ###")
    print ("### (t)rain gladiator                                   ###")
    print ("### (s)leep for one day                                 ###")
    print ("### (e)nter the arena                                   ###")
    print ("### (r)etire                                            ###")
    print ("###########################################################")
    command = getLetter ("Your words, my hands :")
    ## debug print ("\n\n command was :", command)
    if command == 'R' or command == 'X':
        break
    elif command == 'G':
        gladiator = Market(gladiators)
        HitAnyKey()
    elif command == 'T':
        print ("gladiator in training")
        HitAnyKey()
    elif command == 'E':
        gladiators = GladiatorFight (gladiators)
        ## DEBUG: print ("--->", gladiators)
        reputation += 50
        gold += 100
        HitAnyKey()
    elif command == 'S':
        print ("you sleep all day")
        HitAnyKey()
    else:
        print ("I don't comprehend your command")
        HitAnyKey()

print ("program ends")
