"""
a state machine class that imitates a coffee machine.
Tt will work endlessly to make coffee for all
interested persons until the shutdown signal ("exit")
is given.

It checks if the machine is out of resources for making
coffee. If the coffee machine doesn't have enough resources
to make coffee, the program outputs a message that
says it can't make a cup of coffee.

If the user types "buy" to buy a cup of coffee and
then changes their mind, they can type "back" to
return into the main menu.
"""


class CoffeeMachine:
    # this is the initial inventory.
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = "start"  # self.state changes based on user actions.

    def machine_inventory(self):
        print(f"""\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee_beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money\n""")
        self.machine_action()

    def machine_action(self):
        print("Write action (buy, fill, take, remaining, exit): ")
        self.state = "action"

    def buy_coffee(self):
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")
        self.state = "buy action"

    def buy_action(self, coffee_type):
        if coffee_type == "1":
            self.min_resources_espresso()
        elif coffee_type == "2":
            self.min_resources_latte()
        elif coffee_type == "3":
            self.min_resources_cappuccino()
        elif coffee_type == "back":
            print("")
        self.machine_action()

    def min_resources_espresso(self):
        enough = True
        sorry = "Sorry, not enough"
        if self.water < 250:
            print(f"\n{sorry} water!")
            enough = False
        elif self.coffee_beans < 16:
            print(f"\n{sorry} coffee beans!")
            enough = False
        elif self.cups < 1:
            print(f"\n{sorry} cups!")
            enough = False
        if enough:
            if self.cups >= 1:
                self.cups -= 1
                self.money += 4
                self.coffee_beans -= 16
                self.water -= 250
            print("I have enough resources, making you a coffee!\n")
            self.state = "start"

    def min_resources_latte(self):
        enough = True
        sorry = "Sorry, not enough"
        if self.water < 350:
            print(f"\n{sorry} water!\n")
            enough = False
        elif self.milk < 75:
            print(f"\n{sorry} milk!\n")
            enough = False
        elif self.coffee_beans < 20:
            print(f"\n{sorry} coffee beans!\n")
            enough = False
        elif self.cups < 1:
            print(f"\n{sorry} cups!\n")
            enough = False
        if enough:
            if self.cups >= 1:
                self.cups -= 1
                self.money += 7
                self.water -= 350
                self.milk -= 75
                self.coffee_beans -= 20
            print("I have enough resources, making you a coffee!\n")

    def min_resources_cappuccino(self):
        enough = True
        sorry = "Sorry, not enough"
        if self.water < 200:
            print(f"{sorry} water!")
            self.enough = False
        elif self.milk < 100:
            print(f"{sorry} milk!")
            enough = False
        elif self.coffee_beans < 12:
            print(f"\n{sorry} coffee beans!")
            enough = False
        elif self.cups < 1:
            print(f"{sorry} cups!")
            enough = False
        if enough:
            if self.cups >= 1:
                self.cups -= 1
                self.money += 6
                self.water -= 200
                self.milk -= 100
                self.coffee_beans -= 12
            print("I have enough resources, making you a coffee!\n")

    def how_much_water(self):
        print("\nWrite how many ml of water do you want to add:")
        self.state = "fill water"

    def fill_water(self, ml):
        self.water += int(ml)
        self.how_much_milk()

    def how_much_milk(self):
        print("Write how many ml of milk do you want to add:")
        self.state = "fill milk"

    def fill_milk(self, ml):
        self.milk += int(ml)
        self.how_much_coffee()

    def how_much_coffee(self):
        print("Write how many grams of coffee beans do you want to add:")
        self.state = "fill coffee"

    def fill_coffee(self, grams):
        self.coffee_beans += int(grams)
        self.how_much_cups()

    def how_much_cups(self):
        print("Write how many disposable cups of coffee do you want to add:")
        self.state = "fill cups"

    def fill_cups(self, coffee_cups):
        self.cups += int(coffee_cups)
        print("")
        self.state = "start"
        self.machine_action()

    def take_money(self):
        print(f"\nI gave you ${self.money}\n")
        self.money = 0
        self.state = "start"
        self.machine_action()

    def decide(self, user_input):
        if self.state == "start":
            self.machine_action()
        elif self.state == "action":
            self.state = user_input
            self.decide('')
        elif self.state == "buy":
            self.buy_coffee()
        elif self.state == "buy action":
            self.buy_action(user_input)
        elif self.state == "fill":
            self.how_much_water()
        elif self.state == "fill water":
            self.fill_water(user_input)
        elif self.state == "fill milk":
            self.fill_milk(user_input)
        elif self.state == "fill coffee":
            self.fill_coffee(user_input)
        elif self.state == "fill cups":
            self.fill_cups(user_input)
        elif self.state == "take":
            self.take_money()
        elif self.state == "remaining":
            self.machine_inventory()
        else:
            print("Invalid entry\n")
            self.machine_action()


coffee_machine = CoffeeMachine()
user_input = ""
while user_input != "exit":
    coffee_machine.decide(user_input)
    user_input = input()
