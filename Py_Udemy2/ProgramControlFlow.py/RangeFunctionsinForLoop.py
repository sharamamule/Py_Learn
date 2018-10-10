"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very useful for generating numbers
"""

# print(range(0,10)) # this will only print the (0,10)
# print(list(range(0,10)))

a= range(50)
print(list(a))

b= range(0,20,2) # this will print in 2's
print(list(b))
print("****************")

l=[1,2,3,4,5,6,7,8,9]
for num in range(1,9):
    print(num)