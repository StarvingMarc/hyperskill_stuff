def can_coffee_brew():
    """
    User inputs the amount of ingredients the coffee machine has.
    This will find out the minimum cups it can make or if it
    can't make any at all.
    """
    available_water = int(input("Write how many ml of water the coffee machine has: "))
    available_milk = int(input("Write how many ml of milk the coffee machine has: "))
    available_beans = int(input("Write how many grams of coffee beans the coffee machine has: "))
    needed_cups = int(input("Write how many cups of coffee you will need: "))
    water = 200
    milk = 50
    beans = 15

    ingredients = [available_water // water, available_milk // milk, available_beans // beans]

    min_cups = min(ingredients)
    extra_cups = min_cups - needed_cups

    if needed_cups == min_cups:
        print("Yes, I can make that amount of coffee")
    elif needed_cups < min_cups:
        print(f"Yes, I can make that amount of coffee (and even {extra_cups} more than that)")
    elif min_cups == 0:
        print("I need to be refilled")
    else:
        print(f"No, I can make only {min_cups} cup(s) of coffee")


can_coffee_brew()

