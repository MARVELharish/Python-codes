def find_largest_number(numbers):
    # Check if the list is not empty
    if not numbers:
        return None  # Return None if the list is empty
    
    # Initialize the first element as the largest number
    largest = numbers[0]
    
    # Iterate through the list and compare each number
    for number in numbers:
        if number > largest:
            largest = number
    
    return largest

# Example usage:
numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
largest_number = find_largest_number(numbers)

if largest_number is not None:
    print(f"The largest number is: {largest_number}")
else:
    print("The list is empty.")
