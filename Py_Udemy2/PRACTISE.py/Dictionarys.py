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
        print('car is already present')
    else:
        print('car is not present do you want to add')
if_key_is_present ('lexus')
if_key_is_present ('HONDA')