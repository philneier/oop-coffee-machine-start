from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drink_menu = Menu()
coffee_maker = CoffeeMaker()
process_money = MoneyMachine()

available_items = drink_menu.get_items()
is_on = True
while is_on:
    choice = input(f"What would you like? ({available_items}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        process_money.report()
    else:
        drink = drink_menu.find_drink(choice)
        if drink != None:
        # print(drink)
        # print(coffee_maker.is_resource_sufficient(drink))
            if coffee_maker.is_resource_sufficient(drink):
                print(f"a {choice} is ${drink.cost}.")
                if process_money.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)