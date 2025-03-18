# check the number is a Prime or not

def Prime(num):

    if num <2:
        return False
    elif num == 2:
        return True
    
    for i in range(2,num):
        if num%i==0:
            return False
        
    return True

num = int(input("Enter the number: "))
if Prime(num) is True:
    print(f"{num} is a Prime number")
else:
    print(f"{num} is not a Prime number")