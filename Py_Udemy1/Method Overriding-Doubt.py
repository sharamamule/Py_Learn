"""
Method OverRiding :

"""

class Car(object):
    def __init__(self,make,model,color,transmission,fuel):
        print("Our first car is")
        self.make =make
        self.model =model
        self.color =color
        self.transmission =transmission
        self.fuel=fuel

class HONDA(Car):
    def __init__(self):
        print ("Our Second car is")

c1 = Car('AUDI','A4','BLACK','Automatic','Diesel')
print(c1.make)
print (c1.model)
print(c1.color)
print(c1.transmission)
print(c1.fuel)

h= HONDA()
print(h.make)
print (h.model)
print(h.color)
print(h.transmission)
print(h.fuel)
        