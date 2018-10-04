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