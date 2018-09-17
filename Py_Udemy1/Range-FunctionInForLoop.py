"""
It's a Built-in fucntion
** Creates a sequence of numbers but does not save them in memory
Very Useful for generatng numbers
"""

a = range (0,10)
print(a)  # this will only print the range defined i.e range(1,10)

print(list((a))) # this will print all the values between 0-9 , no 10

b= range (0,20,2)
print(list(b))  # This will print the range in 2's

print ("***************")

# using in For loop

F= [1,2,3,4,5,6]

for num in F:
   print(num) # this will print 'F' in full

print ("***************")

for num in range (2,6):
    print(num)
