MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

'''
    3 hot flavors # 3 hương vị
    coins operate # tiền vận hành
    automatic cup dispenser # tự động phân phối cốc
    counting cup selling - đếm số cốc bán
    exam: 
    Espresso - 50ml water - 18g coffee
    Penny - 1 cent - $ 0.01
    Dime - 10 cents - $ 0.10
    Nickel - 5 cents - $0.05
    Quarter - 25 cents - $0.25 
'''
# --- Program Requirements  ---
# TODO 1 Prompt user by asking  “What would you like? (espresso/latte/cappuccino):

# TODO 2 Turn off the Coffee Machine by entering “

# TODO 3. Print report.
# TODO 4. Check resources sufficient(hop ly)
# TODO 5. Process coins
# TODO 6. Check transaction successful
# TODO 7. Make coffee


def report():
    for key in RESOURCES:
        if key == "coffee":
            print(f"{key.title()}: {RESOURCES[key]}g")
        elif key == "money":
            print(f"{key.title()}: ${RESOURCES[key]}", end="")
        else:
            print(f"{key.title()}: {RESOURCES[key]}ml")


def is_resource_sufficient(c):
    """Returns True when order can be made,
    False if ingredients are insufficient."""
    for key in c:
        if c[key] > RESOURCES[key]:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    global money
    if money_received >= drink_cost:
        change = round((money_received - drink_cost), 2)
        print(f"Here is ${change} dollars in change.")
        money += drink_cost
        return True
    else:
        print("“Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(name, order_ingredients):
    for key in order_ingredients:
        RESOURCES[key] -= order_ingredients[key]
    print(f"Here is your {name} ☕️. Enjoy")


money = 0
is_activity = True
while is_activity:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        report()
        print(f"Money: ${money}")
    if choice == "off":
        is_activity = False
        print("Bye! See you again. 😴")
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
