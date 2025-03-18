# Grade Calculation

sub1 = int(input("Enter your score: "))
sub2 = int(input("Enter your score: "))
sub3 = int(input("Enter your score: "))
sub4 = int(input("Enter your score: "))
sub5 = int(input("Enter your score: "))

Total_score = sum([sub1,sub2,sub3,sub4,sub5])

Percentage_score = Total_score/5


if Percentage_score > 90:
    print("A Grade")
elif Percentage_score > 80:
    print("B Grade")
elif Percentage_score > 70:
    print("C Grade")
else:
    print("Fail")


