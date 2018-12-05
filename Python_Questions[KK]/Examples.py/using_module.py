"""
10) what is the use of __init__==__main__: condition in python? [GeneralQuestions-1]
Example
"""

"""
foo = 100

def hello():
    print("i am from my_module.py")
if __name__ == "__main__":
    print ("Executing as main program")
    print("Value of __name__ is: ", __name__)
    hello() 
    """
import my_module
 
print(my_module.foo)
my_module.hello()
 
print(my_module.__name__)
#As you can see now if statement in my_module  fails to execute because the value of __name__  is set to 'my_module'