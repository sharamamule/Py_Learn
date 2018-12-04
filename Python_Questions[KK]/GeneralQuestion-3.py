"""
14) How will you set a global variable inside a function?
Ans:   Global variable ; is accessible by any function  , 
       Any variable defined in the main body is global
       Any variable defined in a function is locla to that function.
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
