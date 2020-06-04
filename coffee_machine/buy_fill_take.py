water = 400
milk = 540
coffee_beans = 120
cups = 9
money = 550


def machine_status():
    print(f"""The coffee machine has:\n{water} of water\n{milk} of milk
{coffee_beans} of coffee beans\n{cups} of disposable cups\n{money} of money\n""")


def machine_action():
    machine_status()
    action = input("Write action (buy, fill, take): ")
    if action == "buy".lower():
        buy_coffee()
    elif action == "fill".lower():
        fill_coffee()
    elif action == "take".lower():
        take_money()


def buy_coffee():
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
    machine_status()


def fill_coffee():
    global water, milk, coffee_beans, cups
    fill_water = int(input("Write how many ml of water do you want to add: "))
    water += fill_water
    fill_milk = int(input("Write how many ml of milk do you want to add: "))
    milk += fill_milk
    fill_coffee = int(input("Write how many grams of coffee beans do you want to add: "))
    coffee_beans += fill_coffee
    fill_cups = int(input("Write how many disposable cups of coffee do you want to add: "))
    cups += fill_cups
    print()
    machine_status()


def take_money():
    global money
    money = 0
    print()
    machine_status()


machine_action()

