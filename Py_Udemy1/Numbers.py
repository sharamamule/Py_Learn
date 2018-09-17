int_num = 1000   # this is the way we define the number in python
float_num = 20.5

print(int_num)
print(float_num)
print ('*******')
a=10 
b=50

add = a+b
print(add)

sub =b-a
print(sub)

multi = a*b
print(multi)

div = a/b
print(div)

exponents = 10 ** 20  # 10 to the power of 20 (10*10...20 times) , symbol is " ** "
print(exponents)

remainder = 11 % 3   #  % -- will give the remainder for the value
print(remainder)    

"""
>>> (2+4) * 3 / 2 ## the output  is 8.0 I.e division & multiplication will take the precedence , hence they are done first
9.0
>>> (2+4*5 ) * 3 / 2
33.0
>>> (2+4*2 ) * 3 / 2 ## But if we want to do it our way we use 'parenthesis' = (2+4)*3 /2  = 9.0
15.0                 ## Same precedence is carried out if we have multiple calculations under parenthesis.
>>>
"""