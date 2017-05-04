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


def main():
    exList = ["Item 1", "Item 2", "Item 3"]
    testTable1 = Table()
    testTable2 = Table(exList)
    print (testTable1.roll())
    print (testTable2.roll())

if __name__ == "__main__":
    main()
