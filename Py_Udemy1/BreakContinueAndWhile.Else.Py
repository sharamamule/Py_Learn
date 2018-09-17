"""
Break: To break our of the closest enclosing loop
Continue: Go to the start of the closeset enclosing loop
"""

# x= 0
# while x <10:
#     print("Value of x is: " + str(x))
#     x = x+1

#     if x==8:
#         break
#     print ("this example is good ")
#     print ("*"*20)
    
# print ("just break out of the loop")
# ##########################################
# x= 0
# while x <10:
#     print("Value of x is: " + str(x))
#     x = x+1

#     if x==8:
#         continue ## At this point the loop will jump to first i.e line-19 so it will nto print
#                   # any thing for 8 - then print 9 then continues printing all related content.
#     print ("*" * 20)
#     print ("this example is good ")

# print ("just break out of the loop")
##########################################
x= 0
while x <10:
    print("Value of x is: " + str(x))
    x = x+1

    if x==8:
       break
    print ("this example is good ")
    print ("*"*20)
    
else:
    print(" Else will print this") # Else block of pile will print if the loop is entered or not
                    # The only time Else block not printed is when loop stopped because of 'Break'statement.
