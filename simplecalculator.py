print("Welcome to the simple calculator")

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
operation = input("Enter the operation (+, *, /, -): ")

if operation == "+":
    print(number1 + number2)

elif operation == "*":
    print(number1 * number2)

elif operation == "/":
    print(number1 / number2)

elif operation == "-":
    print(number1 - number2)

else:
    print("Invalid operation")