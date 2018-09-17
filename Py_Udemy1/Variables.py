"""
table
object reference count
"""

a= "NYC"
b= "NYC"

print(a)
a=123

print(a)
print(b)

b=456
print(b)

c='NYC'
d=c
print(c==d)
print(d is c)

"""
Variable rules
"""
import keyword 
print(keyword.kwlist)

a = b = c =10    # we can assign mutiple variables in one step but is not recommanded #
print(a)
print(b)
print(c)

x,y,z =10,20,30   # Always best practise is to define the code neat but not mix like this #
print(x)
print(y)
print(z)

