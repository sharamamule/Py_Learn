"""
Variable Scope
 A variable we define in a Method has a local scope

"""

# a=10
# def test_method(a):
#     print("Value of local a is: "+ str(a))
#     a =2
#     print("New value of local a is :" + str(a)) # this will change the value of a to 2 as the local variable change is happening with in the method

# print("Value of Global a is: "+ str(a))
# test_method(a)
# print(" did the value of global value change ?  :" + str(a))  # this will still print a=10 as the variable is defined globally out side the method

a =100

def test_method(): ## we are not passing any values in the method but it will use the global valus of 'a' i.e 100
    global a
    print("Value of 'a' inside the method is: " + str(a))
    a=111
    print("New value of 'a' inside the method is: "+ str(a))

print("The value of Global 'a' is : " + str(a))
test_method()  ## here we are checking if the value of global variabe has changed to a=111, 
print("The value of Global 'a' changed? :  "+ str(a))  ## this prints value of a=111 as it's global variable

print("*" * 20)

b='Sharath'

def sharath_character():
    global b
    print("Is he angry ? : " + b)
    b= 'Asha'
    print('Asha is angry than sharath? :' + str(b))

print('Will Akshara be angry:' + str(b))
sharath_character()
print ('Who is more angry:' + str(b))