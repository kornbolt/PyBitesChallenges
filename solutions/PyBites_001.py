'''
PyBites 1. Sum n numbers 
Write a function that can sum up numbers:

It should receive a list of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument ...
Have fun!
'''

def sum_numbers(numbers=None):
    sum = 0
    if numbers is None:
        numbers = range(1,101)

    for num in numbers:  
        sum += num
    
    return sum
    
    
#PyBites Solution
def sum_numbers(numbers=None):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)
