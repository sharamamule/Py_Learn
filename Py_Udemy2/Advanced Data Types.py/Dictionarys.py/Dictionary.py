"""
Dictionary :is a data type to store more than one variable name ,
It should be in terms of Key value pairs sepeareted by {} in key:value pairs , seperated with ","
 {'k1':'v1','k2':'v2'}
 -- Not Sequence
 --** No indexing , only mapping
 """

car = {'Make':'AUDI','Model':'A4','year':'2013'}
print(car)
print(car['Make'])
model =car ['Make']
print(model)

d = {} # this will print the empty dictionary
d['one']= 1
d['two']=2
print(d)

sum_1= d['two']+8 # =10 , This way we can perform operations on dictionaries
print(sum_1)

# to change the value of dictionary on fly...?
print(d)
d ['two'] =d['two']+8
print(d)

"""
Nested Dictionary 
d = {'k1':{'nestki1':'nestvaluek1','nestk2':'nestvaluek2'}}
to access d['k1']['nestki1']
"""
cars_nested = {'AUDI':{'model':'A4','year':'2013'}, 'Benz':{'model':'A140','year':'2010'}}
audi_model = cars_nested ['AUDI']['model']
print (audi_model)
audi_year = cars_nested ['AUDI']['year']
print (audi_year)

"""
Dictionary Methods
"""
car2 = {'Make':'AUDI','Model':'A4','year':'2013'}
cars_nested2 = {'AUDI':{'model':'A4','year':'2013'}, 'Benz':{'model':'A140','year':'2010'}}

print(cars_nested2.keys()) ## this will print all the KEY's of the Dictionary
print(car2.keys())
print(car2.values()) # this will display the VALUES of the dictionary

print(car2.items()) # this will give all the Keys & Values of the dictionary, this is called 'TOPPLE'
car2_copy=car2.copy()

print(car2_copy) # This way we can copy the dictionary
car2_copy.clear() # this will clear the dictionary
print(car2_copy)
print ("*"*20)
print(car2)
print(car2.pop('Model')) # this will delete the model from the Dictionary
print(car2)


