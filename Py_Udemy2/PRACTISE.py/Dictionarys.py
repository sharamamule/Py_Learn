"""
Source : https://www.w3resource.com/python-exercises/dictionary/#EDITOR

1.Write a Python script to sort (ascending and descending) a dictionary by value
"""
import operator

d = { 1:2 ,2:3,4:3,4:5,2:1,0:0}
print('orinal dictionary : ', d)
sorted_d = sorted (d.items() , key = operator.itemgetter(0))
print ('Dictionary in asending order by value : ' ,sorted_d)
sorted_d = sorted(d.items() , key = operator.itemgetter(0), reverse= True)
print ('Dictionary in desc order by value : ' ,sorted_d)

"""
2.Write a Python script to concatenate following dictionaries to create a new one 
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
"""
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dic4 = {**dic1, ** dic2,**dic3}
print(dic4)

# OR #

dic5={1:10, 2:20} 
dic6={3:30, 4:40} 
dic7={5:50,6:60}
dic8= {}
for d in (dic5,dic6,dic7): dic8.update(d)
print(dic8)

"""
3.Write a Python script to check if a given key already exists in a dictionary.
"""
d= {'Audi' :'A4','benz':'A140','HONDA':'CRV'}
def if_key_is_present (x):
    if x in d:
        print('You won this car already !')
    else:
        print('car is not present do you want to buy it? ')
if_key_is_present ('lexus')
if_key_is_present ('HONDA')
if_key_is_present('ROLLYCE')

"""
Write a Python program to iterate over dictionaries using for loops.
"""
d= {'x': 1,'Y':2,'Z':3}
for dic_key, dic_value in d.items():
   print (dic_key , '-->', dic_value)

""" ******
Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
"""
# n= int(input("INPUT a Number"))
# d = dict()

# for x in range (1,n+1):
#     d[x] = x*x
# print(d)

"""
Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
"""
d= dict ()

for x in range (1, 16):
    d[x] = x*x
print(d)

"""
Write a Python script to merge two Python dictionaries.
"""
d={'AUDI':'A4','HONDA':'4x4','BENZ':'A140'}
e= {'Audi':'Automatic','Honda':'MANUAL','BENZ':'Manual'}
z ={**d, **e}
print(z)
# OR # 
z= d.copy()
z.update(e)
print(z)

"""
Write a Python program to iterate over dictionaries using for loops.
"""

