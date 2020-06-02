def simple_calc():
    complete = 0
    answer = "The answer is: "
    while complete != 1:
        num1 = int(input("Enter the first number: "))
        a = isinstance(num1, int)
        operator = input("Enter the symbol of the operation you'd like: ")
        num2 = int(input("Enter the first number: "))
        if operator == "+":
            complete = 1
            return answer + str(num1 + num2)
        elif operator == "-":
            complete = 1
            return answer + str(num1 - num2)
        elif operator == "*":
            complete = 1
            return answer + str(num1 * num2)
        elif operator == "/":
            complete = 1
            return answer + str(num1 / num2)
        elif complete == 0:
            print("I don't understand, please try again.\n")


print(simple_calc())

