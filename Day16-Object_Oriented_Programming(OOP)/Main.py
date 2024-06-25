# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("red", "green")
# for i in range(1, 100):
#     timmy.forward(i)
#     timmy.left(i)
# print(my_screen.canvheight)
# my_screen.exitonclick()
#
# from prettytable import PrettyTable
#
# table_pokemon = PrettyTable(["Pokemon Name", "Type"])
# table_pokemon.add_rows([
#     ["Pikachu", "Electric"],
#     ["Picchu", "Electric"],
#     ["Scatterbug", "Bug"],
#     ["Raichu", "Electric"]
# ])
# table_pokemon.align = "c"
# print(table_pokemon)
from Menu import Menu
from CoffeeMaker import CoffeeMaker
from MoneyMachine import MoneyMachine

is_activity = True
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
while is_activity:
    option = menu.get_items()
    choice = input(f"What would you like? {option}: ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    if choice == "off":
        is_activity = False
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink.ingredients)
