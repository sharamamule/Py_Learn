"""
To Iterate multiple lists at same time we use ZIP function
"""

l1 = [1,2,3,4]
l2 = [10,20,30,40,50,60,70]
  
for a,b in zip (l1, l2):
    print(a)
    print(b)  # Only prints till 4 & 40 as ZIP will take the low list sequence and ends when its done
              # So the list will stop when there is no PAIR              
Cars = ['AUDI','HONDA','BENZ','TOYOTA','LEXUS']
Modles= ['A4','CRV','A100','CAREENA']
for C,M in zip (Cars,Modles):
    print (C)
    print(M)

p1 = [10,20,30]
p2 = [10,20,30,40,50]

for A,B in zip (p1,p2):
    if A > B:
        print(A)
    else:
        print(B)