"""
It is a Data type to store more than one value in one variable name, 
and should be in terms of 'Key value' pair which is separated by " , " 
 { 'K1' :'v1' , 'K2' :'V2'} , not indexed, no sequencing.
 """

car = {'make':'Audi','model':'A4','Color':'Black','Transmission':'Automatic','Miles':'61500'}
print (car) 

## print(car[2]) # this will throw error as no Index

print (car['Color'])

model = car ['model'] ## can access using a varible
print (model)

d={}
print(d) # Empty one

d['one']=1
d['two']=2
print(d)  ## This way we can add values to dictionary

sum_dic = d['one']+8
d['three'] = sum_dic
print(sum_dic)
print(d) ## adding one value and assigning them to 'd'

d['two'] = d['three']
print(d)

## Nested Dictionary : 
"""
Nested Dictionary:
d = {'k1': {'nestk1':'nestvalue1', 'nestk2': 'nestvalue2'}}
d['k1']['nestk1']
"""

cars ={'AUDI':{'Transmission':'Automatic','model':'A4','Color':'Black','Miles':'61000','Year':2013},\
'Honda':{'Transmission':'MAnual','model':'4X4','Color':'Silver','Miles':'58000','Year':'2010'} }
print(cars)

model_car ='model is ' + cars ['AUDI']['model']
print("Car name = Audi")  ## We can access the values in Dictionary like this 
print (model_car)
print(cars['AUDI']['Year']) ## We can also access the values in Dictionary like this referencing the 'Key'
print("Car name = Honda")
model_car = 'model is ' + cars ['Honda']['model']
print(model_car)
print (cars['Honda']['Year'])

print ("---------------------------------")

## Dictioanary Methods :

car = {'make':'Audi','model':'A4','Color':'Black','Transmission':'Automatic','Miles':'61500'}
cars ={'AUDI':{'Transmission':'Automatic','model':'A4','Color':'Black','Miles':'61000','Year':2013},\
'Honda':{'Transmission':'MAnual','model':'4X4','Color':'Silver','Miles':'58000','Year':'2010'} }

print (car.keys())   # to print the keys of a dictionary
print(cars.keys())
print( car.values()) # to print the Values of a dictionary
print(cars.values())
print (cars.items()) # to print the items of a dictionary
print("---><-----")
kenbrook_cars = cars.copy() # to copy the dictionary items into a variable
print(kenbrook_cars)
print("---><-----")
print(car)
print(car.pop('Transmission')) # to remove a particular key from dictionary
print (car)

db={"key1": [1, 2, 3], "key2": [4, 5, 6], "key3": [7, 8, 9]}
print (db["Key1"][2]) # d["key1"] returns the list [1, 2, 3]. Then [2] returns the element 3 from the list



