#Central Casting: Heroes of Legend
import random

class Character:

    def __init__(self, race = [], culture = "", cuMod = 0, social = "",
                 solMod = 0, familyHead = "", siblings = 0, illSiblings = 0,
                 relations = [], birthplace = "", biMod = 0):
        self.race = race 
        self.culture = culture 
        self.cuMod = cuMod
        self.social = social #social standing
        self.solMod = solMod
        self.familyHead = familyHead #head of family
        self.siblings = siblings
        self.illSiblings = illSiblings #illegitimate siblings
        self.relations = relations #other relations
        self.birthplace = birthplace
        self.biMod = biMod

def rollDice(numDice, typeDice):
    """Rolls numDice of typeDice"""
    result = 0
    for i in range(numDice):
        result += random.randint(1, typeDice)
    return result

def table101a():
    diceRoll = rollDice(1, 20)
    if 1 <= diceRoll <= 12:
        return ["human"]

    elif 13 <= diceRoll <= 14:
        return ["elf"]

    elif 15 <= diceRoll <= 16:
        return ["dwarf"]

    elif 17 <= diceRoll <= 18:
        return ["halfling"]

    elif diceRoll == 19:
        race1 = table101a()
        race2 = table101a()
        if race1 == race2:
            if race1 == ["human"]:
                raceList = ["human", "elf"]
                random.shuffle(raceList)
                return raceList
            else:
                raceList = race1 + ["human"]
                random.shuffle(raceList)
                return raceList
        else:
            return race1 + race2

    else:
        return table101b()

def table101b():
    diceRoll = rollDice(1, 10)
    if 1 <= diceRoll <= 3:
        return ["beastman"]

    elif 4 <= diceRoll <= 5:
        return ["reptileman"]

    elif diceRoll == 6:
        return ["orc"]

    else:
        raceList = ["orc", "human"]
        random.shuffle(raceList)
        return raceList

def table101c():
    diceRoll = rollDice(1, 20)
    if 1 <= diceRoll <= 8:
        print ("The character's cultural ties are to his "
               "current nation of residence. While "
               "the character's ancestors may have "
               "come from another land, he has no "
               "strong emotional, physical or cultural "
               "ties to another country.")

    elif 9 <= diceRoll <= 10:
        print ("The character's recent ancestry and "
               "current nation of residence are the "
               "same. However, the character has "
               "strong ethnic ties to, and takes great "
               "pride in his more distant ancestors' "
               "country of origin")

    elif 11 <= diceRoll <= 14:
        print ("The character is a member of a racial "
               "minority within a nation.")

    elif diceRoll == 15:
        print ("The character is a member of a repressed race within his nation.")

    elif diceRoll == 16:
        print("The character is a member of an "
              "indigenous race that has been uprooted "
              "or overthrown by invaders.")

    elif diceRoll == 17:
        print("The character is the child of recent "
              "immigrants to this land and still does "
              "not fit in with the dominant society.")

    elif diceRoll == 18:
        print ("The character was born in a foriegn "
               "land and moved to this land while "
               "young. He retains memories of his "
               "original homeland and may even seek "
               "to return.")

    elif diceRoll == 19:
        print ("The character was born in a foreign "
               "land and moved to this land upon "
               "reaching adulthood. He almost "
               "certainly stands out as a foreigner.")

    else:
        table101c()

def table102(character):
    diceRoll = rollDice(1, 100)
    if 1 <= diceRoll <= 5:
        character.culture = "Degenerate Civilized"
        character.cuMod = 0

    elif 6 <= diceRoll <= 15:
        character.culture = "Primitive"
        character.cuMod = 0

    elif 16 <= diceRoll <= 19:
        character.culture = "Regressive Civilized"
        character.cuMod = 2

    elif 20 <= diceRoll <= 34:
        character.culture = "Nomadic"
        character.cuMod = 6

    elif 35 <= diceRoll <= 64:
        character.culture = "Barbaric"
        character.cuMod = 2

    elif 65 <= diceRoll <= 77:
        character.culture = "Developing Civilized"
        character.cuMod = 6

    elif 78 <= diceRoll <= 87:
        character.culture = "Dynamic Civilized"
        character.cuMod = 10

    elif 88 <= diceRoll <= 92:
        character.culture = "Stagnant Civilized"
        character.cuMod = 4

    else:
        character.culture = "Decadent Civilized"
        character.cuMod = 7

def table103(character):
    diceRoll = rollDice(1, 100) + character.cuMod
    if 1 <= diceRoll <= 15:
        character.social = "Destitute"
        character.solMod = 0

    elif 16 <= diceRoll <= 40:
        character.social = "Poor"
        character.solMod = 2

    elif 41 <= diceRoll <= 85:
        character.social = "Comfortable"
        character.solMod = 4

    elif 86 <= diceRoll <= 95:
        character.social = "Well-to-Do"
        character.solMod = 5

    elif 96 <= diceRoll <= 99:
        character.social = "Wealthy"
        character.solMod = 7

    else:
        #Nobility - needs work
        character.social = "Nobility"
        character.solMod = 10

def table104a(character):
    legitRoll = rollDice(1, 20)

    if legitRoll >= 19:
        print ("This character is illegitimate")
        character.solMod -= rollDice(1, 4)

def table104b(character, reroll = False, adopt = False):
    if reroll:
        headRoll = rollDice(1, 16)

    elif adopt:
        headRoll = rollDice(1, 15)
    
    else:
        headRoll = rollDice(1, 20)
    hiLoRoll = rollDice(1, 2)

    if 1 <= headRoll <= 9:
        if adopt:
            character.familyHead = "Two Adoptive Parents"
        else:
            character.familyHead = "Two Parents"

    elif 10 <= headRoll <= 12:
        if hiLoRoll == 1:
            if adopt:
                character.FamilyHead = "Adoptive Father"
            else:
                character.familyHead = "Father"
        else:
            if adopt:
                character.familyHead = "Adoptive Mother"
            else:
                character.familyHead = "Mother"

    elif headRoll == 13:
        if adopt:
            character.familyHead = "Adoptive Aunt and/or Uncle"
        else:
            character.familyHead = "Aunt and/or Uncle"

    elif headRoll == 14:
        if hiLoRoll == 1:
            if adopt:
                character.familyHead = "Adoptive Older Brother"
            else:
                character.familyHead = "Older Brother"
        else:
            if adopt:
                character.familyHead = "Adoptive Older Sister"
            else:
                character.familyHead = "Older Sister"

    elif headRoll == 15:
        if adopt:
            character.familyHead = "Adoptive Grandparents"
        else:
            character.familyHead = "Grandparents"

    elif headRoll == 16:
        guardianRoll = rollDice(1, 20)
        if guardianRoll <= 8:
            table747(character)
        else:
            table104b(character, False, True)

    elif headRoll == 17:
        character.familyHead = "None known"
        character.social = "Destitute"

    elif headRoll == 18:
        character.familyHead = "Orphanage"
        character.social = "Poor"
        dmRoll = rollDice(1, 4)
        print ("GM: Table 968-104b-" + str(dmRoll))

    elif headRoll == 19:
        table104d(character, False, False)

    else:
        table104b(character, True, False)
        addRel = rollDice(1, 6)
        table104d(character, addRel)

def table104c(character):
    diceRoll = rollDice(1, 20)

    if diceRoll <= 2:
        character.siblings += 0

    elif 3 <= diceRoll <= 8:
        character.siblings += rollDice(1, 3)

    elif 9 <= diceRoll <= 13:
        character.siblings += (rollDice(1, 3) + 1)

    elif 14 <= diceRoll <= 16:
        character.siblings += (rollDice(1, 4) + 2)

    elif 17 <= diceRoll <= 18:
        character.siblings += rollDice(2, 4)

    elif diceRoll == 19:
        character.siblings += rollDice(1, 4)
        table104c(character)

    elif diceRoll == 20:
        character.illSiblings += rollDice(1, 3)
        table104c(character)

def table104d(character, num, reroll = False):
    for i in range(num):
        diceRoll = rollDice(2, 8)
        if 2 <= diceRoll <= 3:
            character.relations.append("Distant Relative")

        elif diceRoll == 4:
            character.relations.append("2nd Cousin")

        elif 5 <= diceRoll <= 8:
            hiLoRoll = rollDice(1, 2)
            if hiLoRoll == 1:
                character.realtions.append("Brother")
            else:
                character.relations.append("Sister")

        elif diceRoll == 9:
            character.relations.append("Cousin")

        elif 10 <= diceRoll <= 11:
            character.relations.append("Great Aunt or Uncle")

        elif diceRoll == 12:
            character.relations.append("Great Grandparent")

        elif diceRoll == 13:
            character.relations.append("Ancestor")

        else:
            if not reroll:
                table104d(character, 1, True)
                character.relations[-1] = "Mysterious " + character.relations[-1]
                print ("GM: 967-104d")
            else:
                table104d(character, 1, True)

def table105b(character, foreigner):
    diceRoll = rollDice(1, 20)
    print (diceRoll)
    if 1 <= diceRoll <= 6:
        character.birthPlace = "In the character's family home "
        character.biMod = 2

    elif diceRoll == 7:
        character.birthPlace = "In a friend's home "
        character.biMod = 2

    elif diceRoll == 8:
        character.birthPlace = "In a hospital or healer's guild hall "
        character.biMod = 0

    elif diceRoll == 9:
        character.birthPlace = "In a voyaging ship "
        character.biMod = 8

    elif diceRoll == 10:
        character.birthPlace = "In a carriage or wagon while travelling "
        character.biMod = 8

    elif diceRoll == 11:
        character.birthPlace = "In a common barn "
        character.biMod = 8

    elif 12 <= diceRoll <= 13:
        if not foreigner:
            table105b(character, True)
            character.birthPlace += "in a foreign land."
            character.biMod += 5

    elif diceRoll == 14:
        character.birthPlace = "In a cave "
        character.biMod = 10

    elif diceRoll == 15:
        character.birthPlace = "In the middle of a field "
        character.biMod = 8

    elif diceRoll == 16:
        character.birthPlace = "In a forest "
        character.birthMod = 9

    else:
        table105c(character)

def table105c(character):
    diceRoll = 4#rollDice(1, 20)
    if diceRoll == 1:
        table105c(character)
        table105c(character)

    elif diceRoll == 2:
        character.birthplace += "In a prison cell "
        character.biMod += 10

    elif diceRoll == 3:
        character.birthplace += "In the temple of a good deity "
        character.biMod += 22

    elif diceRoll == 4:
        battleRoll = rollDice(1, 6)
        print ("battleRoll: " + battleRoll)
        if battleRoll == 6:
            character.birthplace += "On a battlefield "
            character.biMod += 15
        else:
            #this block is not being reached
            character.birthplace += "In a war camp "
            character.biMod += 15

    elif diceRoll == 5:
        character.birthplace += "In an alley "
        character.biMod += 12

    elif diceRoll == 6:
        character.birthplace += "In a brothel "
        character.biMod += 9

    elif diceRoll == 7:
        character.birthplace += "In the palace of a local ruler "
        character.biMod += 9

    elif diceRoll == 8:
        character.birthplace += "In the palace of the ruler of the country "
        character.biMod += 12

    elif diceRoll == 9:
        character.birthplace += "In the palace of a powerful evil person, ruler or creature "
        character.biMod += 22

    elif diceRoll == 10:
        character.birthplace += "In a bar, tavern, or alehouse "
        character.biMod += 9

    elif diceRoll == 11:
        character.birthplace += "In the sewers "
        character.biMod += 17

    elif diceRoll == 12:
        character.birthplace += "In a thieves' den "
        character.biMod += 12

    elif diceRoll == 13:
        character.birthplace += "In the lair of " + table749()
        character.biMod += 9

    elif diceRoll == 14:
        character.birthplace += "DM: Table 968-105 "
        character.biMod += 32

    elif diceRoll == 15:
        character.birthplace += "In the temple of an evil or malignant deity "
        character.biMod += 27

    elif diceRoll == 16:
        character.birthplace += "On another plane of reality "
        character.biMod += 22

    elif diceRoll == 17:
        character.birthplace += "In another time period "
        character.biMod += 17

    elif diceRoll == 18:
        character.birthplace += "On a ship at sea "
        character.biMod += 9

    elif diceRoll == 19:
        character.birthplace += "In a prison cell "
        character.biMod += 16

    else:
        character.birthplace += "In a wizard's laboratory "
        character.biMod += 27



def table747(character):
    diceRoll = rollDice(1, 20)
    if 1 <= diceRoll <= 5:
        table757(character, True)

    elif 6 <= diceRoll <= 7:
        character.familyHead = "Orphanage"

    elif diceRoll == 8:
        character.familyHead = table745()

    elif diceRoll == 9:
        character.familyHead = table751()

    elif diceRoll == 10:
        table104b(character, False, True)

    elif diceRoll == 11:
        character.familyHead = table749()

    elif diceRoll == 12:
        character.familyHead = "Monastary"
        #table 639: 1d3 religious events

    elif diceRoll == 13:
        character.familyHead = "None"

    elif diceRoll == 14:
        character.familyHead = "Beggars, thieves, and outcasts"
        character.social = "Destitute"

    elif diceRoll == 15:
        character.familyHead = "Criminal"
        #865 Crimes for type of criminal
        #631 Underworld Events

    elif diceRoll == 16:
        character.familyHead = ("Character is passed from relative to "
                               "relative until reaching the age of maturity")

    elif diceRoll == 17:
        character.familyHead = "Adventurer"
        #750 Adventurers

    elif diceRoll == 18:
        years = rollDice(1, 10)
        character.familyHead = ("Character dissapears for " + years + " years, "
                               "returning older, but cannot remember what "
                               "happened during that time.")
        print("GM: 968-747")

    elif diceRoll == 19:
        character.familyHead = "Beasts"

    else:
        #Roll twice on this table and combine the result in an imaginatve way
        pass

def main():
    character = Character()
    character.race = table101a()
    print (character.race)
    table101c()
    table102(character)
    print (character.culture)
    print (character.cuMod)
    table103(character)
    print (character.social)
    print (character.solMod)
    table104a(character)
    table104b(character)
    print (character.familyHead)
    print (character.relations)
    table104c(character)
    print (character.siblings)
    print (character.illSiblings)
    table105b(character, False)
    print (character.birthplace)
    print (character.biMod)
    

if __name__ == "__main__":
    main()
