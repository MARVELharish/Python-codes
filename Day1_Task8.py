# Operations by user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Enter the symbol for the operations")


if operation == '+':
    print(num1 + num2)

elif operation == '-':
    print(num1 - num2)

elif operation == '*':
    print(num1 * num2)
else:
    if num2 == 0:
        print("Divide by 0 not possible")
    else:
        print(num1/num2)