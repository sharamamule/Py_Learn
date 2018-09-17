"""
Variable Scope
A variable defined inside a method will have local scope, means
   it can not be used out side the method.self.
"""
a =10
def test_method(a):
     print("Value of method/local 'a' is: "+ str(a))
     a=5
     print ("Value of method/loacl changed to: " + str(a))

print("value of global variable 'a' is: "+ str(a))
test_method(a)
print ("Did the Global 'a' Change?: No it's still:  "+ str(a))

print ("**********************************************************************")

b=100
def test_method2():
    global b
    print ("the method variable is: "+ str(b))
    b=111
    print ("the method variable changed to: "+ str(b))

print("the global Variable was: " + str(b))
test_method2()
print("the Global Variable also changed to: "+ str(b))
