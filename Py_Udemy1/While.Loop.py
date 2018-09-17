
import math
"""
We use While loop to execute statements repeatedly
Conditions are used to stop the execution of loops
Iterable items are strings, Lists, Tuple, Dictionary
"""
"""
****
The Import 3 Loop questions :
1.What do I want to repeat?
2.What do I want to change each time!
3.HOwlong should we repeat?
"""

x= 0
while x < 10:
    print("Value of x is: " + str(x))
    x = x +1

l =[]
num = 0
while num <10:
    l.append(num)
    print("Value of num is: " + str(num))
    num = num +1

print(l)

"""
Write while loops to do the following:
1.– Repeatedly print the value of the variable xValue, decreasing it by 0.5 each time,
as long as xValue remains positive.
2.– Print the square roots of the first 25 odd positive integers.
3.– Repeats a block of code as long as the user indicates they want it to.
4.– Drive the user crazy by insisting they re-enter a particular input no matter what
they enter. Be creative...
"""

# 1.Repeatedly print the value of the variable xValue, decreasing it by 0.5 each time,
#   as long as xValue remains positive. 

x=x-0.5
while  x<50 :
    print ("This number is decreasing by: "+ str(x))
    x=x+1
print("************")

# 2.Print the square roots of the first 25 odd positive integers.
#  first [ import math ] & then use print (math .sqrt(1))
x= 1
while x <= 25 :
 print (math.sqrt (x) )
 x= x+2
 
 print("************")

print (math.sqrt (1) )
print (math.sqrt (3) )
print (math.sqrt (5) )
print (math.sqrt (7) )
print (math.sqrt (9) )
print (math.sqrt (11) )
 # 3.
