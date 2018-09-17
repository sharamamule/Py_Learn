# List is Data type to store more than one value ina one varibale name
# List items are in brackets, seperated with "," [1,2,3]

cars = ["BMW","AUDI","Honda"]
empty_list = []
print(cars)
print(empty_list)

# To Access the elements in List we use indexes

print("*#" * 20)
print(cars[0])
print(cars[2])

num_list = [1,2,3,4]
sum_num = num_list[0] + num_list[2]
print(sum_num)

more_cars = ["BMW","AUDI","Honda"]
print(more_cars[1])  

print("##########################")
i=[1,2,3,4,2,6,2,8,2]
print(i.count(2))
print("##########################")

more_cars[1] = "AudiQ5" # assigning valus to the list
print(more_cars[1])
print(more_cars)

#-------------------------

bcars = ["BMW","AUDI","Honda"]

length = len(bcars)
print(length)

bcars.append("Benz") # to add more values to the list using 'Append'
print(bcars)

bcars.insert(1,"JEEP") # We can use 'Insert' also to add more values
print(bcars)

x= bcars.index("Honda") # to find the index value in the List
print(x)

y= bcars.pop() # To Remove values from LIST --Use 'POP()' will remove the last value from the LIST
print(y)
print(bcars)

bcars.remove("JEEP")  ## To remove what we want use 'remove'
print(bcars)

slicing=  bcars[0:2]   # Slicing a LIST
a = bcars[1:]
print(slicing)
print(a)
print("******")

print (bcars)
bcars.sort()   ## To Sort the list accoridngly we use Sort()
print(bcars)
