# # Fibonacci series

# def fibonacciSeries(num):
#     values = [0,1]

#     if num <= 0:
#         return []
#     elif num ==0:
#         return [0]
    
#     for i in range(2,num):
#         total = values[-1] + values[-2]
#         values.append(total)

        
#     return values[:num]

# num = int(input("Enter the number: "))
# print(fibonacciSeries(num))


def fibonacci_sum(n):
    # Initialize the first two terms of the Fibonacci sequence
    fib_sequence = [0, 1]
    
    # Check if n is less than or equal to 1
    if n <= 0:
        return 0
    elif n == 1:
        return 0  # Sum of first term is just 0
    elif n == 2:
        return 1  # Sum of the first two terms: 0 + 1 = 1
    
    # Generate the Fibonacci sequence up to n terms
    for i in range(2, n):
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    # Return the sum of the Fibonacci sequence
    return sum(fib_sequence[:n])

# Example usage
n = int(input("Enter the number: "))
print(fibonacci_sum(n))
