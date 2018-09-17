"""
Creating our own Method for Car example
"""
class Car(object):
    
    def __init__(self, make ,model):
        self.make =make
        self.model= model

    def info(self):
        print ("The make of the car is: " + self.make)   ## We can create our own "utility"-method and use it 
        print ("The model of the car is: " + self.model)  # - to print the values,
      
c1 =Car ("AUDI",'A4')
c1.info()   ## Now we can use utility method to print the values

c2 =Car('HONDA','4X4')
c2.info()
print ("***********************************************************")

class Kar(object):

    wheels =4  ## We define this "Member-Variable" to use it every time prior to "__init__"
                # This way we can use them at instances level i.e 'k1.wheels' 

    def __init__(self,make,model,color,gear):
        self.make=make
        self.model=model 
        self.color= color
        self.gear =gear
    def info(self):
        print ("The make of the car is: "  + self.make)     
        print ("The model of the car is: " + self.model)
        print ("The color of the car is: " + self.color)
        print ("The gear of the car is: "  + self.gear)

k1=Kar('Audi', 'A4','Black','Automatic')
print (k1.make)
print (k1.color)
print (k1.gear)
print (k1.model)
print (k1.wheels) ## ** This is not recomanded ,If we to use 'Wheels' here 
                   # -we need to define them at 'Attribute' level

print ("************")

k2=Kar('HONDA','4x4','Silver','Manual')
print (k1.make)
print (k1.color)
print (k1.gear)
print (k1.model)


print(Kar.wheels)## The best way to use 'memeber-variable',define 'class name.member-variable' & use here

