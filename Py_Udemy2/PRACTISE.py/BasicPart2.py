import datetime

"""11.
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.
"""
print ("*"*20+ 'Solution 11:')

print(abs.__doc__)   ## SOLUTION-1

func_help= input("Enter a valid Python function name:") ## SOLUTION:2
display=help(func_help)
print(display)

"""12.
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. 
"""
print ("*"*20+ 'Solution 12:')

"""13.Write a Python program to print the following 'here document'.

Sample string:
a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example
"""
print ("*"*20+ 'Solution 13:')

print("""

a string that you "don't'" have to escape
This
is a ...... multi-line
heredoc string ------> example
""")

"""14. Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days 
"""
print ("*"*20+ 'Solution 14:')

## import datetime
print (datetime.datetime.now())

from datetime import date
f_date = date (2014,7,2)
l_date = date (2014 , 7, 11)
delta = l_date-f_date
print( delta)

"""15.Write a Python program to get the the volume of a sphere with radius 6.
 A spehere is a three-dimensional solid with no face, no edge, no base and no vertex.
 It is a round body with all points on its surface equidistant from the centre.
 The volume of a sphere is measured in cubic units.
 ** Volume of the sphere is : V = 4/3 × π × r3 = π × d3/6.
"""
print ("*"*20+ 'Solution 15:')
pi = 3.14159265535897931
r=6.0
v= 4.0/3.0*pi*r**3
print (' The Volume of the sphere is : ' , v)

print ("*"*20+ 'Solution 16:')
"""16.Write a Python program to get the difference between a given number and 17,
    if the number is greater than 17 return double the absolute difference
"""
def difference(n):
    if n<= 17:
        return 17-n
    else:
        return (n-17)*2
print (difference(22))
print(difference(18))

print ("*"*20+ 'Solution 17:')
"""17.Write a Python program to test whether a number is within 100 of 1000 or 2000
"""
num = int(input("Enter the Number:"))
def func1 (num):
    if num in range (900,1100) or num in range (1900, 2100):
       return ('True')
    else:
      return ('False')
print(func1(num))

print ("*"*20+ 'Solution 18:')
"""18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.
"""
def sum_ofValues(x,y,z):
    sum = x + y + z
    if x == y == z:
        sum= sum *3
    return sum

print (sum_ofValues(1,2,3))
print (sum_ofValues(3,3,3))
print(sum_ofValues(5,6,8))

"""19.Write a Python program to get a new string from a given string where "Is" has been added to the front.
      If the given string already begins with "Is" then return the string unchanged.
"""
print ("*"*20+ 'Solution 19:')
def new_string(str):
    if len(str) >=2 and str [:2] == "IS":
        return str
        return "IS" + str

print (new_string("Hellow"))
print (new_string("ISGod"))

"""20.  Write a Python program to get a string which is n (non-negative integer) copies of a given string
"""
print ("*"*20+ 'Solution 20:')

def larger_string (str,n):
    result = ""
    for i in range(n):
        result = result + str
    return result
print (larger_string('abc', 2))
print (larger_string('py',3))
      # OR #
def copies(s,n):
    return s*n
print(copies("thilak",2)) 

"""21.Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user. 
"""
print ("*"*20+ 'Solution 21:')

num2= int(input("Enter the NUMBER you want to check: "))
mod= num2 % 2
if mod >0:
       print (" This is Odd Number")
else:
        print ("this is a EVEN number")

"""22.Write a Python program to count the number 4 in a given list
"""
print ("*"*20+ 'Solution 22:')
def list_count4(nums):
    count=0
    for num in nums:
      if num == 4:
        count = count + 1
    return count
print(list_count4 ([1,4,5,4,8,4]))
print(list_count4 ([1,4,4,4,8,4]))

"""23.Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. 
      Return the n copies of the whole string if the length is less than 2.
"""
print ("*"*20+ 'Solution 23:')

def substring_copy(str, n):
    flen =2
    if flen > len(str):
        flen = len (str)
    substr = str [:flen]        
    result = "" 
    for i in range (n):
        result = result + substr
    return result
print (substring_copy('abcdef',2))
print (substring_copy('q',3 ))

##  OR ##

print ("*"*20+ 'Solution 23.1:')
def copy_str3(str, n):
   return (str * n    if len(str) < 2    else str[:2] * n)

print(copy_str3('abcdef', 3))
print(copy_str3('p', 3))

"""24.Write a Python program to test whether a passed letter is a vowel or not
"""
