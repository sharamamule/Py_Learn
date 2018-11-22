"""
11) what is the type of *args and **kargs ??
Ans: When programming, you may not be aware of all the possible use cases of your code, 
     and may want to offer more options for future programmers working with the module, 
     or for users interacting with the code.
     We can pass a variable number of arguments to a function by using "*args" and "**kwargs" in our code.
     The single asterisk form (*args) is used to pass a non-keyworded, variable-length argument list, 
     and the double asterisk form is used to pass a keyworded, variable-length argument list.
"""

    ##  EXAMPLE : 1 ##
    # --> With "*args" we can create more flexible code that accepts a varied amount of non-keyworded arguments within your function.
def multiply(x,y):
    print(x * y)
multiply(4,5) ## OUTPUT = 20

# What if, later on, we decide that we would like to multiply three numbers rather than just two?
     # If we try to add an additional number to the function, as shown below, we’ll receive an error.

# def multiply(x,y):
  #  print(x * y)
# multiply(4,5,3) ## OUTPUT = ERROR

 ## So, if you suspect that you may need to use more arguments later on, 
    # you can make use of *args as your parameter instead
def multiply2(*args):
    z=1
    for num in args:
        z *= num
    print (z)
multiply2(4,5)
multiply2(4,5,6)
multiply2(3,4,5,6) ## OUTPUT : 20-120-360

# --> The double asterisk form of "**kwargs" is used to pass a keyworded, variable-length argument dictionary to a function. 
     #  Using **kwargs provides us with flexibility to use keyword arguments in our program.
     #  When we use **kwargs as a parameter, we don’t need to know how many arguments we would eventually like to pass to a function.
def print_kwargs(**kwargs):
        print(kwargs)
print_kwargs(kwargs_1="Shark", kwargs_2=4.5, kwargs_3=True)
   # NOTE: A dictionary called kwargs is created from above and we can work with it just like we can work with other dictionaries.

# Create a function to greet a dictionary of names. 
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
print_values(my_name="Sammy", your_name="Casey")
# Because dictionaries may be unordered, your output may be with the name Casey first or with the name Sammy first.

# Pass additional arguments to the function to show that "**kwargs" will accept however many arguments you would like to include
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
print_values(
            name_1="Alex",
            name_2="Gray",
            name_3="Harper",
            name_4="Phoenix",
            name_5="Remy",
            name_6="Val"
        )
""" In practice, when working with explicit positional parameters along with *args and **kwargs, your function would look like this:
    --> def example(arg_1, arg_2, *args, **kwargs):
      ...
"""
""" when working with positional parameters along with named keyword parameters in addition to *args and **kwargs, 
    your function would look like this:
    --> def example2(arg_1, arg_2, *args, kw_1="shark", kw_2="blobfish", **kwargs):
    ...
"""

## Using *args and **kwargs in Function Calls
   # We can also use *args and **kwargs to pass arguments into functions

# example with "*args".
def some_args(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)
args = ("Sammy", "Casey", "Alex")
some_args(*args)

# In the function above, there are three parameters defined as arg_1, arg_, and arg_3. 
  # The function will print out each of these arguments. We then create a variable that is set to an iterable (in this case, a tuple),
    # and can pass that variable into the function with the asterisk syntax
## OUTPUT:arg_1: Sammy -arg_2: Casey -arg_3: Alex

# We can also modify the program above to an iterable list data type with a different variable name. 
  # Let’s also combine the "*args" syntax with a named parameter:
def some_args2(arg_1, arg_2, arg_3):
    print("arg_1:", arg_1)
    print("arg_2:", arg_2)
    print("arg_3:", arg_3)
my_list = [2, 3]
some_args2(1, *my_list)
# OUTPUT :arg_1: 1 -arg_2: 2 -arg_3: 3

## Similarly, the keyworded "**kwargs "arguments can be used to call a function. 
   # We will set up a variable equal to a dictionary with 3 key-value pairs (we’ll use kwargs here, but it can be called whatever you want), 
     # and pass it to a function with 3 arguments:
def some_kwargs(kwarg_1, kwarg_2, kwarg_3):
    print("kwarg_1:", kwarg_1)
    print("kwarg_2:", kwarg_2)
    print("kwarg_3:", kwarg_3)
kwargs = {"kwarg_1": "Val", "kwarg_2": "Harper", "kwarg_3": "Remy"}
some_kwargs(**kwargs)
# OUTPUT:kwarg_1: Val -kwarg_2: Harper- kwarg_3: Remy

    ##   EXAMPLE : 2  ##
# Here is an example of how to use the non-keyworded form 
def Kar(make, *args):
    print('Make of Car is: '+ make)
    for arg in args:
            print ("another arg: ", arg)
Kar('Audi',"Benz",'A4','pusky','pobey')

# The below steps is how we normally define a module & call it:
"""
    #print('Modle of car is :'+ model)
        ## Now we can use this model in a different code .[refer to built-in modules.py]
# def kar2(engine,color):
#     print("Engine is powerful : "+ engine)
#     print("Color Guess? :" + color)
#k1= Kar('Audi',"Benz",'A4')
#k2=kar2('2.2','BLUE')
"""
# Here is an example of how to use the keyworded form. Again, 
  # one formal argument and two keyworded variable arguments are passed.
def Kar2(make, **kwargs):
    print('Make of Car is: ', make)
    for key in kwargs:
            print ("another Keyword arg: %s: %s" % (key, kwargs[key]))
Kar2(make=1,model1="AUDI",model2=3)

# This special syntax can be used, not only in function definitions,but also when calling a function
def test_var_args_call(ar1,ar2,ar3,ar4):
    print ("ar1:", ar1)
    print("ar2:", ar2)
    print("ar3:",ar3)
    print ("ar4:",ar4)
args = ("two",3,9)
test_var_args_call (1,*args)

# Here is an example using the keyworded form when calling a function:
def make_and_model_of_my_car (car1,car2,car3,car4):
    print ("mycar1:", car1)
    print("mycar2:",car2)
    print ("mycar3:", car3)
    print ("mycar4:", car4)
Kwargs = {"car4":"audi", "car2":"benz","car3":"honda"}
make_and_model_of_my_car("bmw", **Kwargs)