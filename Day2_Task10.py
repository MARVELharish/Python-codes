# Palindrom or not

def palindrome(input):
    
    input = str(input).lower()

    return input == input[::-1]

input = input("Enter the sting: ")

if palindrome(input):
    print(f" '{input}' is a Palindrome")
else:
    print(f" '{input}' is not a Palindrome")