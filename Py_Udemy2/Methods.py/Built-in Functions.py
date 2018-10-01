"""
Some built-in functions :
max() : It takes any number of arguments and returns the largest one.

min() : It takes any number of arguments and returns the smallest one.

abs() : It returns the absolute value of the number, that number's distance from0.
It always returns a postive value and it only takes a single number.

type(): It returns the type of the data it receives as an argument.
"""

def largest_num(*args): # "*" means it's capable of multiple arguments
    print(max(args))

largest_num (-20,-10,4,3,2,-100)

def smallest_num(*args):
    print(min(args))

smallest_num(-1000,10,2,3,-19) 

def absolute_num(a):
    print(abs(a))

absolute_num (-20)
absolute_num(10)

print(type(99))
print(type(99.10))
print(type("99.6"))
l=[1,2,3,4]
print(type(l))