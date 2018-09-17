"""
Some buit-n functions :
max (): It takes any number of arguments and returns the largest one

min() : It takes any number of arguments and returns the smallest one

abs(): It returns the absolute value of the number, that number's distance from 0
       It always returns a postive value and it only takes a single number

type():It returns the type of the data it receives as an argument

"""

def largest_num(*args):  # * means it can accept any number of arguments
    print(max(args))
    return(max(args))   # we can return it not mandatory simply use print also

x=largest_num(-20, -10, 0,20, 100) # 100 is printed which is the max

def smallest_num(*args): # * means it can accept any number of arguments
    print(min(args))

smallest_num(10,-10,30,-5,100 )
print ("*****************************")  
def abs_function(a):
    print(abs(a))

abs_function(-30)
abs_function(40) 
print ("*****************************")  

print(type(99))
print(type(28.99))
print(type("67.99"))
l= [1,2,3,4,5,6]
print(type(l))

