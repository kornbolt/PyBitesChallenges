"""
Iterate over the given names and countries lists, printing them prepending the number of the loop (starting at 1). 
Here is the output you need to deliver:

1. Julian     Australia
2. Bob        Spain
3. PyBites    Global
4. Dante      Argentina
5. Martin     USA
6. Rodolfo    Mexico
Notice that the 2nd column should have a fixed width of 11 chars, so between Julian and Australia there are 5 spaces
between Bob and Spain, there are 8. This column should also be aligned to the left.

"""


names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""
    EL = list(enumerate(zip(names, countries), 1))
    [ print(f"{n}. {name.ljust(11)}{country}") for n, (name, country) in EL ]
    
#using list comprehensions is the pythonic way! the other way is:

def enumerate_names_countries():
    for num, (name, country) in enumerate(zip(names,countries)):
        print(f"{num + 1}. {name.ljust(11)}{country}")
 
 
