import random
def haiku():

    sevenSyllables = ["past the winter skyline", "over yonder is our home", "a song drifts into the sea"]
    fiveSyllables = ["out of the water", "these yawning valleys", "can you slice the wind", "i stand in the shore", "days blink like torches", "hola el mundo"]
    a = fiveSyllables[random.randint(0,2)]
    b = sevenSyllables[random.randint(0,2)]
    c = fiveSyllables[random.randint(3,5)]
    print(a)
    print(b)
    print(c)

haiku()
#exitonclick

import random                                                                   #adds random function
def nameGenerator():                                                            #define function

    firstnames = ["Adam", "Taylor", "Sam", "Maya", "Chloe", "Daphne"]           #lists of names
    lastnames = ["Swift", "Carter", "McDonald"]
    newname = []                                                                #list for new name
    newname.append(random.choice(firstnames))                                   #add randomly selected name from old list to new list
    newname.append(random.choice(lastnames))
    print(newname)                                                              #print new list

nameGenerator()

