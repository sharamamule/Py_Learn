"""
While Loop is used to execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, Lists, Tuple, Dictionary
""" 
# x=0
# while x <10 :
#     print("X is the greatest: " + str(x)) ## this is infinite LOOOP
#     x = x+1
# l= []
# num =0
# while num <10:
#     l.append(num)
#     num+=1
#     print(" Value of num is: " + str(num))
# print("*"*20)
# print(l) 

# """
# Break Continue and While Else
# Break : To break out of the closest enclosing loop
# Continue : Go to the start of the closest enclosing loop
# """

x=0
while x<10:
    print( "value of x is: " + str(x))
    x= x+1

    if x==8:
        break
    print("This is a good example")
    print("***********")
else:     ##  ** If the Loop ends as a result of a Break statemet then the ' else' statement is not executed.
    print("Just brooke of the Loop")

# x=0
# while x<10:
#     print("Value of X is :"+str(x))
#     x= x+1

#     if x==8:
#         continue  ## It will come sout of the Loop for that condition and prints the next later.
#     print(" This is continue")
#     print("this is good example")
    
# print("I am done printing")