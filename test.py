def calculate_average(numbers):
    """
    calculate_averae - calc ave of numbers
    
    numbers = input number
    """
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Usage:
numbers = [10, 20, 30, 0, 50]
result = calculate_average(numbers)
print(f"The average is: {result}")
