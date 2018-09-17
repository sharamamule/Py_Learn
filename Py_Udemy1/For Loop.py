"""
To Execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are strings, list, Tuple, Dictionary
"""
## Strings for loop
my_string = 'abcabcabc'

for c in my_string:
    if c=='a':
        print('A', end='') # To print this side by side we use end='' 
    else:
        print(c,end='')
print()
print("*" * 10)
## List for Loop

cars = ['Audi','BMW','BENZ','HONDA']

for car in cars:
    print(car)
print("*" * 10)

nums= [1,2,3,4,5]
for n in nums:
    print(n * 10) # This will multiply nums with 10

print("*" * 10)

## List for Dictionary's

d={'Audi': 'A4','Honda':'CRV','Benz':'A100'}
for k in d:
    print(k+ " "+ str(d[k]))
print("*" * 10)

for k,v in d.items():
    print(k)       # This will print Items and values in a line
    print(v)