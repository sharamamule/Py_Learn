"""
Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, Lists, Tuple, Dictionary
""" 
# STRINGS for loop
my_string =" abcabc"

for c in my_string: # ' C' is onfly variable created here
    if c == 'b':
        print('B', end=' ')
    else:
        print(c, end=' ') 

print()

#Lists for loop
cars = ['AUDI','BENZ','HONDA']

for car in cars:
    print(car)

nums = [1,2,3]

for n in nums:
    print(n * 10)
print("********")

#Dictionaries for loop
d={'One': '1', 'Two':'2','Three':'3'}
for k in d:
    print(k + " " + str(d[k]))
print("********")

for k,v in d.items():
    print(k)
    print(v)