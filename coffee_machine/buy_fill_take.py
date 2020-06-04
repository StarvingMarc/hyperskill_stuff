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
    print(f"""The coffee machine has:\n{water} of water\n{milk} of milk
{coffee_beans} of coffee beans\n{cups} of disposable cups\n{money} of money\n""")


def machine_action():
    """
    gives the user the options to buy coffee, fill the machine, or take the money
    """
    machine_inventory()
    action = input("Write action (buy, fill, take): ")
    if action == "buy".lower():
        buy_coffee()
    elif action == "fill".lower():
        fill_coffee()
    elif action == "take".lower():
        take_money()


def buy_coffee():
    """
    when the user chooses an option, this will adjust the inventory accordingly.
    """
    global water, milk, coffee_beans, cups, money
    buy_options = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
    if buy_options == "1":
        water -= 250
        coffee_beans -= 16
        money += 4
        cups -= 1
    elif buy_options == "2":
        water -= 350
        milk -= 75
        coffee_beans -= 20
        money += 7
        cups -= 1
    elif buy_options == "3":
        water -= 200
        milk -= 100
        coffee_beans -= 12
        money += 6
        cups -= 1
    print()
    machine_inventory()


def fill_coffee():
    """
    asks the user the number if items they would like to add to inventory
    """
    global water, milk, coffee_beans, cups
    fill_water = int(input("Write how many ml of water do you want to add: "))
    water += fill_water
    fill_milk = int(input("Write how many ml of milk do you want to add: "))
    milk += fill_milk
    fill_coffee_ = int(input("Write how many grams of coffee beans do you want to add: "))
    coffee_beans += fill_coffee_
    fill_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    cups += fill_cups
    print()
    machine_inventory()


def take_money():
    """
    this empties the money from the machine
    """
    global money
    money = 0
    print()
    machine_inventory()


machine_action()

