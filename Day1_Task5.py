# find the year is leap year or not

year = int(input("Enter the year: "))

#check wheather it can be divided by 4 or not
if (year %4==0 and year % 100 != 0) or (year % 400 ==0):
    print("This year is a leap year")
else:
    print("This year is Not a Leap year")