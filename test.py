def calculate_average(numbers):
    """
    calculate_averae - calc ave of numbers
    
    numbers = input number
    """
    average = sum(numbers) / len(numbers)
    return average

# Usage:
try:
    numbers = [10, 20, 30, 0, 50]
    print("The average is:", calculate_average(numbers))
except ZeroDivisionError:
    print("List is empty")
except TypeError:
    print("Invalid input")
except:
    print("something went wrong")
# test
