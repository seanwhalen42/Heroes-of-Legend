#Central Casting: Heroes of Legend
import random

class Character:

    def __init__(self, race):
        self.race = race

class Table:

    def __init__(self, numDice, typeDice, tableList = []):
        self.numDice = numDice
        self.typeDice = typeDice
        self.modDice = modDice
        self.tableList = tableList

    def roll(self):
        """Rolls on the table"""
        if len(self.tableList) == 0:
            return None
        else:
            return tableList[rollDice(numDice, typeDice)]

def rollDice(numDice, typeDice):
    """Rolls numDice of typeDice"""
    result = 0
    for i in range(numDice):
        result += random.randint(1, typeDice)
    return result

def main():
    exList = ["Item 1", "Item 2", "Item 3"]
    testTable1 = Table()
    testTable2 = Table(exList)
    print (testTable1.roll())
    print (testTable2.roll())
    print (rollDice(1, 6))
    print (rollDice(1, 100))

if __name__ == "__main__":
    main()
