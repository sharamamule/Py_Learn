""" 
Lists & Accessing ELEMENTS
"""
# List is a data type used to store more than one value in one VARIABLE NAME

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