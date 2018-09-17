"""
and
*********
True and True  --> True
True and false --> False
False and False --> False
****************************
or
********
True or True    --> True
True or False   --> True
False or False  --> False
********************************
not
*******
Not True  --> False
Not False --> True

"""

and_output1 =(10==10) and (10 >9)
print(and_output1)
and_output2 =(10==10) and (10<9)
print(and_output2)
and_output3 = (10>10) and (10<9)
print(and_output3)
print ("-------")
or_output = (10 / 2 == 0) or (10 ==10)
print(or_output)
or_output2 = ('Akshara' == 'Akshara') or (10 >10)
print(or_output2)
or_output3 = ('AksharaT' == 'Akshara') or (10 >10.56)
print(or_output3)
print ("** ** ** **")
not_true= not (10/2== 5)
print(not_true)
not_false =not( 10 >10)
print(not_false)

### Order of Precedence [ when all the expressions are used same time]
  # not [1st] - and [2nd] & or [3rd] , the only way to control this is to use " ( ) -parenthesis"

"""
1.not
2.and
3.or
"""

bool_output = True or not False and False
  # First its 'not False'= True --> then True and False --> False --> Finally True or False = True
print(">>>>>>>>>>>")
print(bool_output)
print(">>>>>>>>>>>")
bool_output_1 = 10 == 10 or not 10>10 and 10>10
print (bool_output_1)
print(">>>>>>>>>>>")
bool_output_1 = (10 == 10 or not 10>10) and 10>10
print (bool_output_1) # True or True -> True and False -> False