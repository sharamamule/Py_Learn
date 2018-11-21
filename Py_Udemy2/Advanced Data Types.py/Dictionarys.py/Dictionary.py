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

                    ## THIS WILL 'PRINT' THE 'EMPTY' DICTIONARY
d = {} 
d['one']= 1
d['two']=2
print(d)

sum_1= d['two']+8    # =10 , This way we can perform operations on dictionaries
print(sum_1)

                    ## TO CHANGE 'VALUE' ON 'FLY'
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
                ## THIS WILL PRINT ALL THE'KEY's' OF THE DICTIONARY
print(cars_nested2.keys()) 
print ("^"*20)
print(car2.keys())
                ## THIS WILL DISPLAY THE 'VALUES' OF THE DICTIONARY
print(car2.values()) 
                ## THIS WILL GIVE ALL THE 'KEYS' & 'VALUES' OF THE DICTIONARY & CALLED 'TOPPLE'
print(car2.items()) 
car2_copy=car2.copy()
                ## THIS WAY WE CAN 'COPY' THE DICTIONARY This way we can copy the dictionary
print(car2_copy)
                ## THIS WILL 'CLEAR' THE DICTIONARY 
car2_copy.clear() 
print(car2_copy)
print ("*"*20)
print(car2)
                ## THIS WILL 'DELETE' THE MODEL FROM THE DICTIONARY
print(car2.pop('Model')) 
print(car2)
print ("^"*20) 
                ## TO 'ADD' NEW VALUES TO THE DICTIONARY 
d= {'Honda':'CRV','BENZ':'A140'}
print(d)
d.update({'Audi':'A4'})
print(d)

k={'pobey':'Alpha','Pulka':'Pusky'}
print(k)