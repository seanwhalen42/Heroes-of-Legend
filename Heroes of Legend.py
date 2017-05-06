#Central Casting: Heroes of Legend
import random

class Character:

    def __init__(self, race = []):
        self.race = race



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
                
def main():
    character = Character()
    race  = table101a()
    character.race = race
    print (character.race)
    table101c()

if __name__ == "__main__":
    main()
