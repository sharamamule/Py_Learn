"""
Postiional Parameters
They are like optional paramters
And can be assigned a default value, if no value is provided from outside
"""

def sum_nums (n1=2, n2=4):  # Optional Paramters 
# def sum_nums (n1,n2=4): we can declare this also
    return n1 + n2

sum1 = sum_nums(n1=5,n2=5) 
print(sum1)

print("**********************")

sum2 = sum_nums (4,n2=10) # We can use the arguments different ways
print(sum2)

def sum_nums2(n1, n2=4):
   
    return n1 + n2

sum1 = sum_nums2(n1=4, n2=12)
print(sum1)