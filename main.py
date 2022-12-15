MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def print_report():
    for key, value in resources.items():
        if key == "money":
            print(key.capitalize(), ':', "$", value)
        else:
            print(key.capitalize(), ':', value, "ml")


is_on = True


def resources_check(drink_ingredients):
    """takes user drink choice and returns True if there are sufficient resources"""
    for item in MENU[drink_ingredients]['ingredients']:
        if MENU[drink_ingredients]['ingredients'][item] <= resources[item]:
            return True
        else:
            return False
    # print(resources_check(choice['ingredients']))


def take_coins():
    """takes coins from user, displays credit and change, and returns True if they inserted enough money."""
    global choice
    print("Please insert coins. ")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickels = float(input("How man nickels? "))
    pennies = float(input("How many pennies? "))
    user_credit = quarters * .25 + dimes * .10 + nickels * .05 + pennies
    required_change = user_credit - MENU[choice]['cost']
    print(f"You have inserted ${user_credit:.2f}")
    if user_credit >= MENU[choice]['cost']:
        resources['money'] += MENU[choice]['cost']
        print(f"Your change is ${required_change:.2f}")
        return True
    else:
        return False


def update_resources(drink_ingredients):
    """takes user choice and subtracts its resources from resources"""
    global choice
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]


while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        print("Thank you, goodbye. ")
        is_on = False
    elif choice == "report":
        print_report()
    else:
        print(f"Excellent choice. That costs ${MENU[choice]['cost']:.2f}")
        resources_check(choice)
        if resources_check(choice):
            if take_coins():
                update_resources(MENU[choice]['ingredients'])
                print("Here is your coffee. Enjoy! ")
            else:
                print(
                    f"You have inserted $, but your selected drink costs ${MENU[choice]['cost']:.2f}. Please insert more coins. ")
                take_coins()
        else:
            print(f"I'm sorry, but we are all out of {choice}. Please come back later. ")
