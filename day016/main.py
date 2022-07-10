from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
drink = Menu()
ingredients = CoffeeMaker()

is_on = True
while is_on:
    drink.get_items()
    name = input(f"What would you like? {drink.get_items()}: ")
    if name == "off":
        is_on = False
    elif name == "report":
        ingredients.report()
        money.report()
    else:
        choice = drink.find_drink(name)
        if choice is not None:
            if ingredients.is_resource_sufficient(choice) and money.make_payment(choice.cost):
                ingredients.is_resource_sufficient(choice)
                ingredients.make_coffee(choice)
