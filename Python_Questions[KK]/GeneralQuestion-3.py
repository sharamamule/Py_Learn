"""
14) How will you set a global variable inside a function?
Ans:   Global variable ; is accessible by any function  , 
       Any variable defined in the main body is global
       Any variable defined in a function is local to that function.
       To specify a defined variable as global inside a function, use the "global" statement.     
"""
def myfun():
    global myvar  # Since we declared this as global variable can be used by other functions
    myvar =10      
def some_other_function():
    print (myvar) 
myfun()      # this will print 10
some_other_function() # this will print 10

## We can also pass values to functions as "arguments" rather than using them directly as global like below:

def myfunc(xx):
    print (xx)
def some_other_function2(yy):
    print (yy)
myvar =30
myfunc(myvar)
some_other_function2(myvar)
  ## In this we re-defined 'myvar' as global but instead of using it inside the functions directly,
   #  we are passing it as an argument to each of the function.
   # myvar gets aliased in each of the function xx & yy , 
   # alias means reference to the object is being passed and occupied ot the name XX & YY thus making it available to the function.

"""
12) difference between %s and %r in python 
Ans:  " %r" calls repr., while "%s "calls str . 
      These may behave differently for some types, but not for others:    
      --> repr returns " a printable representation of an object", 
      --> while str returns "a nicely printable representation of an object". For example, they are different for strings: 
"""
        ## First Example 
s = 'spam' 
# "repr" returns a printable representation of an object, 
# which means the quote marks will also be printed. 
print(repr(s)) 
# 'spam' 
# "str" returns a nicely printable representation of an 
# object, which means the quote marks are not included. 
print(str(s)) 
# spam 

        ## Second Example. 
x = "example" 
print ("My %r" %x) 
# My 'example' 
# Note that the original double quotes now appear as single quotes. 
print ("My %s" %x) 
# My example  

        ## Third Example. 
x = 'xxx' 
withR = ("Prints with quotes: %r" %x) 
withS = ("Prints without quotes: %s" %x) 
print(withR) 
# Prints with quotes: 'xxx' 
print(withS) 
# Prints without quotes: xxx

"""
 15) How will you share global variables across modules? 
 Ans:  Move all globals to a file, I call this file "settings.py". This file is responsible for defining globals and initializing them;
"""## EXAMPLE ##

# settings_globalVar1.py 
def myf():
    global myList
    myList = []
## Next, your Importing_globalVar2 can import globals:

# Importing_globalVar2.py
""" 
import settings_globalVar1
def somefunc():
    settings_globalVar1.myList.append('hellow')
"""
## Note that subfile does not call init() -- that task belongs to main.py:

# importing_sub_globalvar3.py
"""
import settings_globalVar1
import Importing_globalVar2 

settings_globalVar1.myf()             # Call only once
Importing_globalVar2.somefunc()        # Do stuff with global var
print (settings_globalVar1.myList[0])  # Check the result
"""

"""
23) recursive functions? 
 Ans:  We know that in Python, a function can call other functions. It is even possible for the function to call itself.
       These type of construct are termed as "recursive functions"
"""
# Example of recursive function
           #An example of recrusive function to find the factorial of a number.
def cal_factorial(x):
        """this is a recursive function to find the factorial of an integer"""
        if x==1:
           return 1
        else:
           return (x * cal_factorial(x-1))
num=5
print (" The Factorial of" , num, "is", cal_factorial(num))

"""OUTPUT
    "The Factorial of 5 is 120"  ## In the above example,"cal_factorial()" is a recrusive functions as it calls itself.
      When we call this fucntion with a postive integer, it will recrusively call itself by decreasing the number.
      Each function call multiples the number with the factorial of number 1 until the number is equal to one.
calc_factorial(4)              # 1st call with 4
4 * calc_factorial(3)          # 2nd call with 3
4 * 3 * calc_factorial(2)      # 3rd call with 2
4 * 3 * 2 * calc_factorial(1)  # 4th call with 1
4 * 3 * 2 * 1                  # return from 4th call as number=1
4 * 3 * 2                      # return from 3rd call
4 * 6                          # return from 2nd call
24                             # return from 1st call
    ## Recursion ends when the number reduces to 1. This is called the base condition.
       Every recursive function must have a base condition that stops the recursion or else the fucntion calls itself infinitely.
##Advantages of Recursion
        # Recursive functions make the code look clean and elegant.
        # A complex task can be broken down into simpler sub-problems using recursion.
        # Sequence generation is easier with recursion than using some nested iteration.
##Disadvantages of Recursion
        # Sometimes the logic behind recursion is hard to follow through.
        # Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
        # Recursive functions are hard to debug.
"""


