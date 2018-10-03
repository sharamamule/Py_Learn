"""
DATETIME
"""
import datetime
print (datetime.datetime.now())

"""
IMPORT PI
"""
from math import pi     ## IN GEOMETRY,THE ARE ENCLOSED BY A CIRCLE OF RADIUS R IS πr2. 
                        ## HERE THE GREEK LETTE 'π' REPRESENTS A CONSTANT,APPROXIMATELY EQUALS T0 '3.14159'
                        ## WHICH IS EQUAL TO THE RATIO OF THE CIRCUMFERENCE OF ANY CIRCLE TO ITS DIAMETER.
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2)) ## '**' MEANS THE 'R' VALUE MULTIPLE TWICE

"""
SPLIT()
"""
values = input("Input some comma seperated numbers: ")
list = values.split ("_")    ## 'SPLIT()' METHOD RETURNS A LIST OF STRINGS AFTER BREAKING THE GIVEN STRING BY THE SPECIFIED SEPARATOR.
tuple = tuple(list)
print('List : ', list)
print('Tuple : ',tuple)

"""
TO PRINT THE EXTENSION
"""
file_name = input (" Sample filename : ")
file_extension = file_name.split(".")
print (type(file_name))      ## THIS PRINTS OUT THE TYPE OF EXTENSION
print("The Extension of the file is : " + repr (file_extension[-1])) ## THIS WILL PRINT THE EXTENSION AFTER ' .'