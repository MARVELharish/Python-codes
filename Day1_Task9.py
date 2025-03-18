side1 = int(input())
side2 = int(input())
side3 = int(input())

if side1 == side2 == side3:
    print("This is the Equalorial Triangle")
elif side1 != side2 != side3:
    print("This is the Scalene Triangle")
else:
    print("This is the Isoscles Triangle")