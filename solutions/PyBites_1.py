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
