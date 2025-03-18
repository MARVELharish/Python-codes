# vowels or consonent

def vowelsOrConsonent(input):
    vowels = "aeiou"
    count_of_vowels = 0
    count_of_consonent = 0


    for char in input:
        if char.isalpha():
            if char in vowels:
                count_of_vowels += 1
            else:
                count_of_consonent += 1
    return count_of_vowels, count_of_consonent
input = input("Enter you words here: ").lower()

print(vowelsOrConsonent(input))