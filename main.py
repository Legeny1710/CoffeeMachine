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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}





def report():
    for i in resources:
        print(f'{i} : {resources[i]}')
    print(f'Profit: {profit}')

def check_resources(coffe):
    if resources["water"] >= MENU[coffe]["ingredients"]["water"] and resources["coffee"] >= MENU[coffe]["ingredients"]["coffee"]:
        if coffe == "latte" or coffe == "cappuccino":
            if resources["milk"] >= MENU[coffe]["ingredients"]["milk"]:
                resources["water"] -= MENU[coffe]["ingredients"]["water"]
                resources["milk"] -= MENU[coffe]["ingredients"]["milk"]
                resources["coffee"] -= MENU[coffe]["ingredients"]["coffee"]

                return True
        elif coffe == "espresso":
            resources["coffee"] -= MENU[coffe]["ingredients"]["coffee"]
            resources["water"] -= MENU[coffe]["ingredients"]["water"]
            return True
    else:
        print("Sorry there is not enough ingredients")
        return False


def process_coins(quarters, dimes, nickles, pennies):
    total = 0
    quarters = quarters * 0.25
    dimes = dimes * 0.10
    nickles = nickles * 0.05
    pennies = pennies * 0.01
    total += quarters + dimes + nickles + pennies
    return total



def transaction(coins, coffee):
    if coins >= MENU[coffee]["cost"] and resourceAvailable:
        change = coins - MENU[coffee]["cost"]
        print("Transaction is Successfull!")
        print(f'heres the change: {round(change, 3)}')
        print(f"Here is your Coffee!")
        profit = coins - change
        return profit
    elif coins < MENU[coffee]["cost"]:
        print("Transaction is not approved!, You don't have enough money")
        resources["water"] += MENU[coffee]["ingredients"]["water"]
        resources["milk"] += MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] += MENU[coffee]["ingredients"]["coffee"]
        return 0
    elif not resourceAvailable:
        resources["water"] += MENU[coffee]["ingredients"]["water"]
        resources["milk"] += MENU[coffee]["ingredients"]["milk"]
        resources["coffee"] += MENU[coffee]["ingredients"]["coffee"]
        return 0



user_coffee = input("What would you like? (espresso/latte/cappuccino):")

while user_coffee != "off":
    if user_coffee == "report":
        report()
    else:

        print("Please insert Coins")
        quarters = int(input("how many quarters?:"))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))

        resourceAvailable = check_resources(user_coffee)

        profit += transaction(
        process_coins(quarters, dimes, nickles, pennies), user_coffee)

    user_coffee = input("What would you like? (espresso/latte/cappuccino):")

