"""
10) what is the use of __init__==__main__: condition in python? [GeneralQuestions-1]
Example
"""

foo = 100
def hello():
    print("i am from my_module.py")
if __name__ == "__main__":
    print ("Executing as main program")
    print("Value of __name__ is: ", __name__)
    hello() 