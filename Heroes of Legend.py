#Central Casting: Heroes of Legend
import random

class Table:

    def __init__(self, tableList = []):
        self.tableList = tableList

    def add(self, toAdd):
        self.tableList.append(toAdd)

    def roll(self):
        """Rolls on the table"""
        if len(self.tableList) == 0:
            return None
        else:
            return random.choice(self.tableList)

def rollDice(numDice, typeDice):
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
    print str(rollDice(1, 6))
    print str(rollDice(1, 100))

if __name__ == "__main__":
    main()
