l1 = [1,2,3]
l2 = [6,7,8,9]

for a,b in zip(l1,l2): ## Zip is a built in function,will create a pair of elemets when we pass two elements and will stop at the end of the shorter LIST
    if a>b:
        print(a)
    else:
        print(b)