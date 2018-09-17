"""
 CLASS: Its a template that defines the object
Start name of class with 'Capital' letter
"""

class Car(object):           # Car class is inherting the 'object' class
    
    def __init__(self, make):
        self.make= make    # This wasy we define attributes of the CLASS
# 'init' -is like constructor ,it will set every thing that needed to set up the class
# 'self' means that the method in this class is referencing the class name
## it's just always the first paramter passsed in to the 'init' method and Python uses the first paramater 
 # - receives to actually refer the object that gets created.So when we create an instance of the car class
 # - Python is going to use this first paramater to refer to that instance-so we can use any word instead of 'Self'
 # -but 'Self' is commonly used in python
c1 = Car('Audi')
print(c1.make)

c2=Car('HONDA')
print(c2.make) ## C1 & C2 are not the instance, its the reference variable that access the Instance
                # - in the memory

class Kar(object):
    
    def __init__(self,make, model="4X4"): # We can also define like postional paramaters
        self.model = model # We create these 'Attributes' to assign values to 'instances'
        self.make = make

k1= Kar('AUDI')
print (k1.make)
print (k1.model)


k2 = Kar('benz')
print (k2.make)
print (k2.model)

class Movies(object):
    def __init__(self,moviename,genre,streamplace):
        self.genre=genre
        self.streamplace = streamplace
        self.moviename =moviename

m1 = Movies('Titanic','Drama','Netflix')
print (m1.moviename)
print (m1.genre)
print (m1.streamplace)

m2 = Movies('Die-hard','Action','AmazonPrime')
print (m2.moviename)
print (m2.genre)
print(m2.streamplace)

m3 = Movies('red','Action','Sky-view')
print (m3.moviename)
print (m3.genre)
print(m3.streamplace)
