"""
Method is defined and used as 'def' in python
It can take arguments or can be defined empty
A Group of code statements which can perform some specific task
Methods are re-usable and can be called when needed in the code

"""

def sum_nums():
    print(3+2) 

sum_nums()  # This is how we cal the method, by using the method name

def sum_nums2(n1,n2): # This way we can re-use it
    print(n1+n2)

sum_nums2(2,9)
sum_nums2(10,7)

l= [1,2,3]
print(l.append(4)) ### when we clicked ' . ' operation python will display all inbuilt methods
print(l)