"""
a program that will work endlessly to make coffee for all
interested persons until the shutdown signal is given.

checks if the machine is out of resources for making
coffee. If the coffee machine doesn't have enough resources
to make coffee, the program outputs a message that
says it can't make a cup of coffee.

if the user types "buy" to buy a cup of coffee and
then changes their mind, they can type "back" to
return into the main menu.
"""


# this is the initial inventory
water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def machine_inventory():
    """
    prints the current inventory of the machine
    """
    print(f"""\nThe coffee machine has:\n{water} of water\n{milk} of milk
{coffee_beans} of coffee beans\n{cups} of disposable cups\n${money} of money\n""")


def machine_action():
    """
    gives the user the options to buy coffee, fill the machine, or take the money
    """
    action = ""
    while action != "exit":
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        if action == "buy".lower():
            buy_coffee()
        elif action == "fill".lower():
            fill_coffee()
        elif action == "take".lower():
            take_money()
        elif action == "remaining".lower():
            machine_inventory()
        elif action == "back".lower():
            machine_action()


def buy_coffee():
    """
    when the user chooses an option, this will adjust the inventory accordingly.
    """
    global water, milk, coffee_beans, cups, money
    buy_options = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
    if buy_options == "1":
        min_resources_espresso()
    elif buy_options == "2":
        min_resources_latte()
    elif buy_options == "3":
        min_resources_cappuccino()


def fill_coffee():
    """
    asks the user the number if items they would like to add to inventory
    """
    global water, milk, coffee_beans, cups
    fill_water = int(input("\nWrite how many ml of water do you want to add:\n"))
    water += fill_water
    fill_milk = int(input("Write how many ml of milk do you want to add:\n"))
    milk += fill_milk
    fill_coffee_ = int(input("Write how many grams of coffee beans do you want to add:\n"))
    coffee_beans += fill_coffee_
    fill_cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    cups += fill_cups
    print()


def take_money():
    """
    this empties the money from the machine
    """
    global money
    print(f"\nI gave you ${money}\n")
    money = 0


def min_resources_espresso():
    """
    checks to see if there is enough to make espresso
    """
    global water, milk, coffee_beans, cups, money
    enough = True
    sorry = "Sorry, not enough"
    if water < 250:
        print(f"{sorry} water!")
        enough = False
    elif coffee_beans < 16:
        print(f"{sorry} coffee beans!")
        enough = False
    elif cups < 1:
        print(f"{sorry} cups!")
        enough = False
    if enough:
        if cups >= 1:
            cups -= 1
            money += 4
            coffee_beans -= 16
            water -= 250

        print("I have enough resources, making you a coffee!\n")


def min_resources_latte():
    """
    checks to see if there is enough to make latte
    """
    global water, milk, coffee_beans, cups, money
    enough = True
    sorry = "Sorry, not enough"
    if water < 350:
        print(f"{sorry} water!\n")
        enough = False
    elif milk < 75:
        print(f"{sorry} milk!\n")
        enough = False
    elif coffee_beans < 20:
        print(f"{sorry} coffee beans!\n")
        enough = False
    elif cups < 1:
        print(f"{sorry} cups!\n")
        enough = False
    if enough:
        if cups >= 1:
            cups -= 1
            money += 7
            water -= 350
            milk -= 75
            coffee_beans -= 20
        print("I have enough resources, making you a coffee!\n")


def min_resources_cappuccino():
    """
    checks to see if there is enough to make cappuccino
    """
    global water, milk, coffee_beans, cups, money
    enough = True
    sorry = "Sorry, not enough"
    if water < 200:
        print(f"{sorry} water!")
        enough = False
    elif milk < 100:
        print(f"{sorry} milk!")
        enough = False
    elif coffee_beans < 12:
        print(f"{sorry} coffee beans!")
        enough = False
    elif cups < 1:
        print(f"{sorry} cups!")
        enough = False
    if enough:
        if cups >= 1:
            cups -= 1
            money += 6
            water -= 200
            milk -= 100
            coffee_beans -= 12
        print("I have enough resources, making you a coffee!\n")


machine_action()

