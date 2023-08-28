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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    return int(input("how many quarters?: ")) * 0.25 + int(input("how many dimes?: ")) * 0.1 + \
        int(input("how many nickles?: ")) * 0.05 + int(input("how many pennies?: ")) * 0.01


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        resources['money'] += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")

# TODO: 1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
while True:
    water, milk, coffee, money = resources['water'], resources['milk'], \
        resources['coffee'], resources['money']

    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the Coffee Machine by entering "off" to the prompt.
    if user_input == "off":
        print("Program exiting...")
        break

    # TODO: 3. Print report
    elif user_input == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    # TODO: 4. Check resources sufficient?
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        # TODO: 5. Process coins.
        drink = MENU[user_input]
        if is_resource_sufficient(MENU[user_input]['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink['ingredients'])
