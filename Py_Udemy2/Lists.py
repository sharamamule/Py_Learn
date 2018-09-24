""" 
Lists & Accessing ELEMENTS
"""
#List is a data type used to store more than one value in one VARIABLE NAME

cars =["AUdi","HONDA","BMW","MERC"]
empty_list= []
print(cars)
print(empty_list) 

# Access invidual items in LIST using Indexes

print(cars[2])
print("*" *20)
print(cars[1:3])

num_list = [10,3,2]
sum_list = num_list[0]+num_list[2]
print(sum_list)

more_cars= ["AUDI",'Benz','Toyota']
print(more_cars)
print("*"*10)
more_cars[2] = "HONDA" ## This will replace the LIST item on 2nd INDEX

print(more_cars)

apartment=  ["Flat","Single","double","parking"]
print(apartment[2])

"""
List Methods 
"""
cars = ["AUDI","HONDA","BENZ"]
length = len(cars)
print(length)

cars.append("TOYOTA") # to add new Items 
print(cars)

cars.insert(1,"SUZUKI") # this will add new Item on from END Index
print(cars)

x=cars.index("HONDA") # this will give the index of HONDA
print(x)

y=cars.pop()
print(y) # this will REMOVE last from END

cars.remove("SUZUKI")
print(cars)

## SLICING a LIST
slicing = cars[0:2] # this will get all the items of the list startionf form 1st index till END
print(slicing)
a= cars[1:]
print(a)
print("*"*20)
print(cars)
cars.sort()
print(cars)  # this will Sort the list alphabetically

