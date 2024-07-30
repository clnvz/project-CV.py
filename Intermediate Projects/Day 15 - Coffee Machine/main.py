from choices import MENU
from choices import resources


def calc_change(customer_choice, quart, dime, nick, penn):
    price = MENU[customer_choice]["cost"]
    cash = (quart * 0.25) + (dime * 0.10) + (nick * 0.05) + (penn * 0.01)
    return cash - price


def get_profit(customer_choice):
    return MENU[customer_choice]["cost"]


def check_resources(customer_choice):
    if resources["water"] < MENU[customer_choice]["ingredients"]["water"]:
        print("Sorry, there's not enough water.")
        return 1
    elif resources["milk"] < MENU[customer_choice]["ingredients"]["milk"]:
        print("Sorry, there's not enough milk.")
        return 1
    elif resources["coffee"] < MENU[customer_choice]["ingredients"]["coffee"]:
        print("Sorry, there's not enough coffee.")
        return 1
    else:
        return 0


def update_resources(customer_choice):
    resources["water"] -= MENU[customer_choice]["ingredients"]["water"]
    resources["milk"] -= MENU[customer_choice]["ingredients"]["milk"]
    resources["coffee"] -= MENU[customer_choice]["ingredients"]["coffee"]


def give_report(profit):
    print(f"Water: {resources["water"]} mL")
    print(f"Milk: {resources["milk"]} mL")
    print(f"Coffee: {resources["coffee"]} g")
    print(f"Money: ${profit}")


profit = 0
coffee_machine = True
while coffee_machine == True:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_choice == "report":
        give_report(profit)
    elif customer_choice == "off":
        coffee_machine = False
    else:
        inventory = check_resources(customer_choice)
        if inventory == 0:
            print("Please insert coins.")
            quart = int((input("How many quarters?: ")))
            dime = int((input("How many dimes?: ")))
            nick = int((input("How many nickles?: ")))
            penn = int((input("How many pennies?: ")))
            change = calc_change(customer_choice, quart, dime, nick, penn)
            if change < 0:
                print("Sorry that's not enough money. Money refunded.")
            else:
                profit += get_profit(customer_choice)
                update_resources(customer_choice)
                print(f"Here's your change: ${round(change, 2)}")
                print(f"Here's your {customer_choice}. Enjoy!")