"""4.
Write a Python program which accepts the radius of a circle from the user and compute the area
"""
from math import pi     ## IN GEOMETRY,THE ARE ENCLOSED BY A CIRCLE OF RADIUS R IS πr2. 
                        ## HERE THE GREEK LETTE 'π' REPRESENTS A CONSTANT,APPROXIMATELY EQUALS T0 '3.14159'
                        ## WHICH IS EQUAL TO THE RATIO OF THE CIRCUMFERENCE OF ANY CIRCLE TO ITS DIAMETER.
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2)) ## '**' MEANS THE 'R' VALUE MULTIPLE TWICE