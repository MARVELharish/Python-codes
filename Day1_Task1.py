#akes two numbers as input and prints their sum, difference, product, and quotient
# get input as integer value 
A = int(input("Enter the first number: "))
B = int(input("Enter the Second number: "))

# by using f-string
# Addition
print(f"Sum of the two number is: {A+B}")

# Subraction
print(f"Subraction of the two number is: {A-B}")

# Multiplication
print(f"Multiple of the two number is: {A*B}")

# Divide
print(f"Divide of the two number is:  {A/B:.2f}") # limit by 2 deciaml place