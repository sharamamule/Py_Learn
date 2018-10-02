"""
and
*********************
True and True    --> True
True and False   --> False
False and False  --> False

or
*********************
True or True    --> True
True or False   --> True
False or False  --> False

not
********************
not True    --> False
not False   --> True
"""

and_output1= (10 == 10) and (10 >9)
and_output2= (10 == 10) and (10 >19)
and_output3= (10 == 10.2) and (10 >9)

print(and_output1)
print(and_output2)
print(and_output3)
print("*************")
or_output1= (10 == 10) or (10 >9)
or_output2= (10 == 10) or (10 > 19)
or_output3= (10 == 10.2) or (10 >29)

print(or_output1)
print(or_output2)
print(or_output3)

print("*************")
not_true = not (10==10)
not_false= not(10>100)

print(not_true)
print(not_false)
print("*************")
"""
Order of Boolean_precedence
1.not
2.and
3.or
"""
bool_output = True or not False and False
print(bool_output)

bool_output_1 = 10==10 or not 10 >10 and 10>10
print(bool_output_1) # True

bool_output_2 = (10==10 or not 10 >10) and 10>10
print(bool_output_2) # False
