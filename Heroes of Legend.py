#Central Casting: Heroes of Legend
import random

class Character:

    def __init__(self, race = [], culture = "", cuMod = 0, social = "",
                 solMod = 0, familyHead = ""):
        self.race = race
        self.culture = culture
        self.cuMod = cuMod
        self.social = social
        self.solMod = solMod
        self.familyHead = familyHead

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

def table104b(character, reroll = false, adopt = false):
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
        if guradianRoll <= 8:
            table747(character)
        else:
            table101b(character, false, true)

    elif headRoll == 17:
        character.familyHead = "None known"
        character.social = "Destitute"

    elif headRoll == 18:
        character.familyHead = "Orphanage"
        character.social = "Poor"
        dmRoll = rollDice(1, 4)
        print ("GM: Table 968-104b-" + str(dmRoll))

    elif headRoll == 19:
        table104d(character)

    else:
        table104b(character, true, false)
        addRel = rollDice(1, 6)
        table104d(character, addRel)
            

def main():
    character = Character()
    race  = table101a()
    character.race = race
    print (character.race)
    table101c()
    table102(character)
    print (character.culture)
    print (character.cuMod)
    table103(character)
    print (character.social)
    print (character.solMod)

if __name__ == "__main__":
    main()
