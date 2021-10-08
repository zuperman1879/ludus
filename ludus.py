### ludus v 0.1
### steven franken 

### imports
from random import randint
from pcinput import getLetter

def HitAnyKey():
    anykey = input("\nHit any key:")

def GladiatorFight (gladiators):
    ### define nr op oponents
    minimum = gladiators-2
    maximum = gladiators*50/100
    oponents = randint (gladiators-2, int(gladiators+maximum))
    ### calculate win of lose
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
    print ("### (f)ight gladiator                                   ###")
    print ("### (r)etire                                            ###")
    print ("###########################################################")
    command = getLetter ("Your words, my hands :")
    ## debug print ("\n\n command was :", command)	
    if command == 'R' or command == 'X':  
        break
    elif command == 'G':
        print ("market is closed")
        HitAnyKey()
    elif command == 'T':
        print ("gladiator in training")
        HitAnyKey()
    elif command == 'F':
        gladiators = GladiatorFight (gladiators)
        print ("--->", gladiators)
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
