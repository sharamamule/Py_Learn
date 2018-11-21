"""
table
object reference count
"""
a = "nyc"
b = "nyc"
print(a) 

a = 123 
print (a)
print(b)

b=12345
print(b)

c= 'nyc'
d = c 
print(c==d)

"""
Variable Rules
"""
import keyword         ## using in-built libraries
print(keyword.kwlist)  ## this will give all the list of keywords

a = b = c = 10   ## we can assign these 3 at one time
print(a)
print(b)
print(c)

x,y,z =10,20,30  ## This is doable
print(x)
print(y)
print(z)