"""
Positional Paramters:
They are optional parameters
And can be assigned a default value, if no value is provided from outside
"""
def sum_nums(n1=4,n2=3):
    return n1+n2

s1= sum_nums()
print(s1)

s2=sum_nums(n1=10,n2=10) # We can assign values on GO
print(s2)

s3=sum_nums(n1=7) ## In this case n2 value is taken from method where n2=3
print(s3)