from data import resources, MENU


def report(resources):
    for ingredient in resources:
        if ingredient in ["water", "milk"]:
            print(f"{ingredient.title()}: {resources[ingredient]}ml")
        elif ingredient == "coffee":
            print(f"{ingredient.title()}: {resources[ingredient]}g")
        elif ingredient == "money":
            print(f"{ingredient.title()}: ${resources[ingredient]}")


def check_resources(option, MENU, resources):
    if MENU[option]["ingredients"]["water"] > resources["water"]:
        return "Sorry, there is not enough water."
    elif MENU[option]["ingredients"]["milk"] > resources["milk"]:
        return "Sorry, there is not enough milk."
    elif MENU[option]["ingredients"]["coffee"] > resources["coffee"]:
        return "Sorry, there is not enough coffee."
    else:
        return True


def price_drink(total_amount, MENU, option):
    if total_amount > MENU[option]["cost"]:
        cash_change = total_amount - MENU[option]["cost"]
        return f"Here is ${cash_change:.2f} in change"
    elif total_amount == MENU[option]["cost"]:
        return "Thank you for the money"
    elif total_amount < MENU[option]["cost"]:
        return "Sorry, there is not enough money. Money refunded."


resources["money"] = 0
MENU["espresso"]["ingredients"]["milk"] = 0


on = True
while on:
    drink = input("What would you like? (espresso/latte/cappuccino): ")
    while drink == "report":
        report(resources)
        drink = input("What would you like? (espresso/latte/cappuccino): ")
    if drink == "off":
        print("See you tomorrow!")
        on = False

    else:
        check_result = check_resources(option=drink, MENU=MENU, resources=resources)
        if check_result != True:
            print(check_result)
        else:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: ")) * 0.25
            dimes = int(input("How many dimes?: ")) * 0.10
            nickles = int(input("How many nickles?: ")) * 0.05
            pennies = int(input("How many pennies?: ")) * 0.01

            total_amount = quarters + dimes + nickles + pennies
            money_given = price_drink(total_amount=total_amount, MENU=MENU, option=drink)

            if money_given == "Sorry, there is not enough money. Money refunded.":
                print(money_given)
            else:
                print(money_given)

                print(f"Here is your {drink} ☕. Enjoy!")

                for item in resources:
                    if item != "money":
                        resources[item] -= MENU[drink]["ingredients"][item]
                    else:
                        resources[item] += MENU[drink]["cost"]
