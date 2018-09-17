"""
Sequence of characters
Contain a-z, 0-9, special characters
When defined should be under double or  single quotes
"""

a= "This is a simple string"
b= 'Using a single string'
print(a)
print(b)

c = "Need to use 'quotes' inside a string" ## we are trying to quote with in a quote, can be acheived by using single quotes insde & other way round. 
print(c)    

d = "Another way to handle \"quotes\""  ## The ' \' back slash will ignore the functionality of double quotes and print the double quote as it is.
print(d)

a= "This is a single\
 string"
print(a)
