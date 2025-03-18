# sum of two digit with in a number

num = int(input("Enter two digit number or more: "))
Total = 0

# check wheather is given number is two digit or not
if num < 10:
    print("Your number is less than 10!\"Kindly\" provide a two or more digit")
else:
    for i in str(abs(num)):
         Total += int(i)

print(Total)