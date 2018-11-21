# class Car(object):
    
#     def __init__(self,make,model,transmission):
#         # self.make=make
#         # self.model=model
#         # self.transmission = transmission

#     def info(self):
#         print("Make of the car: " + self.make)
#         print("Model of the car: " + self.model)

#     # def info(self):
#     #     print('The color of the Car is :' ,+ self.make)  ## THIS IS CALLED 'UTILITY' METHOD
#     #     print('The model the car is: ' + self.model)
#     #     print('The Gear type of the cars is: ' + self.transmission)

# c1= Car('Audi','A4','Automatic')
# # print(c1.make)
# # print(c1.model)
# # print(c1.transmission)
# c1.info()


class Car(object):

    wheels = 4  ## This is a 'MEMBER-VARIABLE'

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)   ## THIS IS CALLED 'UTILITY' METHOD
        print("Model of the car: " + self.model)



c1 = Car('bmw', '550i')
 ## print(c1.wheels)   --> Never use the 'MEMEBER-VARIABLE' WITH INSTANCE 
print(c1.make)
#c1.info()

c2 = Car('benz', 'E350')
print(c2.make)
#c2.info()

print(Car.wheels)  ## THIS WAY WE NEED TO USE 'CLASS-NAME.MEMEBER-VARIABLE

print("*"* 20)
class Cycle(object):
    def __init__(self,make,model,accessories):
        self.make=make
        self.model=model
        self.accessories=accessories
print("*"* 20)


class BYKE(object):
    def __init__(self,make,color):
        self.make=make
        self.color=color

    def info(self):
        print("Byke make is :"+ self.make)
        print("Byke color is :"+ self.color)

b2=BYKE('CBZ','Yellow')
b2.info()
print("*"* 20)

class Movie(object):
    def __init__(self,MovieName,LeadRole,Director,Music):
        self.MovieName=MovieName
        self.LeadRole=LeadRole
        self.Director=Director
        self.Music=Music
    def info(self):
        print ('My Favourite Movie name is :' + self.MovieName)
        print ('My Favoyrite Lead Role is :' + self.LeadRole)
        print('director was :'+ self.Director)
        print('music director was :'+ self.Music)

print("My Favourite Movie in Tollywood is : ")
m1= Movie('Premadesam','Vineeth','Unknown','AR Rehman')
m1.info()
print("*"* 20)
print("My Favourite Movie in Hollywood is : ")
m2 =Movie('TITANIC','LEONARDO','JAMES CAMERON','Un-known')
m2.info()
print('I went to watch my Fav movie :')
b2.info()