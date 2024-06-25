class MenuITem:
    """Models each Menu Item."""
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }


class Menu:
    """Models the Menu with drinks."""
    def __init__(self):
        self.menu = [
            MenuITem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuITem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuITem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        """ Returns all the names of the available menu items """
        option = "|"
        for items in self.menu:
            option += f"{items.name}|"
        return option

    def find_drink(self, name):
        """Searches the menu for a particular drink by name.
         Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if name == item.name:
                return item
        print("Sorry that item is not available.")

