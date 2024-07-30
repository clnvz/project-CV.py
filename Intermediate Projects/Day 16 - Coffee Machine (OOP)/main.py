from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

menulist = menu.get_items().split("/")
menulist.remove("")
menu_table = PrettyTable()
menu_table.add_column("Drink", menulist)
menu_table.add_column("Price", ["$ 2.5", "$ 1.5", "$   3"], "r")

coffee_machine = True
while coffee_machine == True:
    customer_order = input(f"{menu_table}\nWhat would you like to order?: ").lower()
    if customer_order == "off":
        coffee_machine = False
    elif customer_order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        valid_drink = menu.find_drink(customer_order)

        if coffee_maker.is_resource_sufficient(valid_drink) and money_machine.make_payment(valid_drink.cost):
            coffee_maker.make_coffee(valid_drink)