## sSOURCE : https://www.w3resource.com/python-exercises/python-basic-exercises.php 
""" 1.
Write a Python program to print the following string in a specific format (see the output):
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! 
Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
"""
print ("*"*20+ 'Solution 1:')

print ('Twinkle , twinkle, little star,')
print ("    " + ' How I wonder what you are!')
print("        "+'up above the world so high,')
print("        " + 'Like a diamond in the sky.')
print('Twinkle,Twinkle,little star, ')
print("    "+'How I Wonder what you are') 

print ("*"*20+ 'Solution 2:')
"""2.
Write a Python program to get the Python version you are using
"""
import sys              ## 'SYS' MODULE PROVIDES ACCESS TO SOME VARIABLES USED OR MAINTAINED BY INTERPERTER & TO FUNCTIONS THAT INTERACT STRONGLY WITH THE INTERPERTER.
print("python version")
print(sys.version)      ## THIS WILL GIVE THE PYTHON VERSION
# print('version info')
# print (sys.version_info) 

print ("*"*20+'Solution 3:')
"""3.
Write a Python program to display the current date and time.
"""
import datetime
print (" Current date and time: ")
print (datetime.datetime.now())

print ("*"*20+ 'Solution 4:')
"""4.
Write a Python program which accepts the radius of a circle from the user and compute the area
"""
# from math import pi     ## IN GEOMETRY,THE ARE ENCLOSED BY A CIRCLE OF RADIUS R IS πr2. 
#                         ## HERE THE GREEK LETTE 'π' REPRESENTS A CONSTANT,APPROXIMATELY EQUALS T0 '3.14159'
#                         ## WHICH IS EQUAL TO THE RATIO OF THE CIRCUMFERENCE OF ANY CIRCLE TO ITS DIAMETER.
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2)) ## '**' MEANS THE 'R' VALUE MULTIPLE TWICE

print ("*"*20+ 'Solution 5:')
"""5.
Write a Python program which accepts the user's first and last name 
and print them in reverse order with a space between them.
"""
# f= input('First name: ')
# l = input ('Last Name: ')
# firstname_lastname = l +" "+ f
# print ('Hello ' + firstname_lastname)

print ("*"*20+ 'Solution 6:')
"""6.
Write a Python program which accepts a sequence of comma-separated numbers from user
and generate a 'list' and a 'tuple' with those numbers
"""
# values = input("Input some comma seperated numbers: ")
# list = values.split ("_")    ## 'SPLIT()' METHOD RETURNS A LIST OF STRINGS AFTER BREAKING THE GIVEN STRING BY THE SPECIFIED SEPARATOR.
# tuple = tuple(list)
# print('List : ', list)
# print('Tuple : ',tuple)

# print ("*"*20+ 'Solution 7:')
# """7.
# Write a Python program to accept a filename from the user and print the extension of that
# """
# file_name = input (" Sample filename : ")
# file_extension = file_name.split(".")
# print (type(file_name))      ## THIS PRINTS OUT THE TYPE OF EXTENSION
# print("The Extension of the file is : " + repr (file_extension[-1])) ## THIS WILL PRINT THE EXTENSION AFTER ' .'

print ("*"*20+ 'Solution 8:')
"""8.
Write a Python program to display the first and last colors from the following list.
color_list = ["Red","Green","White" ,"Black"]
"""
color_list = ["Red","Green","White" ,"Black"]
print(color_list[0])
print(color_list[3])

print ("*"*20+ 'Solution 9:')
"""9.
Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = (11, 12, 2014)
Sample Output : The examination will start from : 11 / 12 / 2014
"""
exam_st_date = (11, 12, 2014)
print (" The examination will start from : %i/%i/%i"%exam_st_date)
print("The Examination will start from : "  ,exam_st_date[0] ,'/',exam_st_date[1],'/',exam_st_date[2])

print ("*"*20+ 'Solution 10:')
"""10.
Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5 
Expected Result : 615
"""
n = input (" input a number : ")
n=n
nn=n*2
nnn=n*3
value= int(n)+int(nn)+int(nnn) 
print('Result is :', value) 
## OR ##
a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)