"""
Kelsey Deffendol
CS1400 -- Programming Project 7
Due Dec 4
people that helped me: my father
Problem: create two classes that represent a stack of items and a player's inventory
Things learned:
    -how to implement classes
    -how to create objects and bring them into another object
    -documentation standards for python
"""

class ItemStack:
    """
    A class used to represent a stack of items

    Attributes
    ----------
    name : str
        name of the item stack
    quantity : int
        number of items in the stack

    Methods
    -------
    useItem()
        decreases quantity of item by one if used
    """

    def __init__(self, name, quantity):
        """
        Parameters
        ----------
        name : str
            name of the item stack
        quantity : int
            number of items in the stack
        """

        self.quantity = quantity
        self.name = name

    def __str__(self):
        """Prints name of item and the quantity
        """

        return "name: " + self.name + "\tquantity: " + str(self.quantity)

    def __lt__(self, other):
        """
        compares current item to another

        Parameters
        ----------
        other : str
            item stack being compared
        """
        return self.name < other.name

    def useItem(self):
        """decreases quantity of item by one if used
        """

        if (self.quantity > 0):
            self.quantity -= 1
        return self.quantity


class Inventory:
    """
    A class used to represent an inventory to hold items

    Methods
    -------
    itemExists(itemStack)
        checks to see if item already exists in inventory
    addItemStack(itemStackToAdd)
        adds new item stack to inventory
    """

    def __init__(self):
        self._itemList = {} #dictionary

    def __str__(self):
        allValues = ""
        for value in sorted(self._itemList.values()):
            allValues += str(value)+"\n"
        return allValues

    def itemExists(self, itemStack):
        """check to see if item exists in inventory

        Parameters
        ----------
        itemStack : obj
            stack of an item
        """

        return itemStack.name in self._itemList

    #add item stack to inventory
    def addItemStack(self, itemStackToAdd):
        """adds new item stack to inventory

        Parameters
        ----------
        itemStackToAdd : obj
            stack of an item to add to inventory
        """

        if (self.itemExists(itemStackToAdd)):
            existingItem = self._itemList[itemStackToAdd.name]
            existingItem.quantity += itemStackToAdd.quantity
        else:
            self._itemList[itemStackToAdd.name] = itemStackToAdd


#testing---------------------
a = ItemStack("Torches", 8)
b = ItemStack("Food", 9)
c = ItemStack("Potion", 5)
d = ItemStack("Potion", 6)

d.useItem()
d.useItem()

backpack = Inventory()
backpack.addItemStack(a)
backpack.addItemStack(b)
backpack.addItemStack(c)
backpack.addItemStack(d)


print(backpack)