#class Fruit(object):
#     def __init__(self,nutrition,fruit_shape,fruit_season):
#         self.nutrition=nutrition
#         self.fruit_shape=fruit_shape
#         self.fruit_season= fruit_season

# F1 = Fruit('C vitamin','Round','Any season')
# print(F1.nutrition)
# print(F1.fruit_shape)
# print(F1.fruit_season)


# class Orange(Fruit):
#     def __init__(self,type_fruit,color,shape):
#         self.type_fruit=type_fruit
#         self.color=color
#         self.shape=shape
# F2=Orange('Mandarin','Amber','ovel')
# print(F2.type_fruit)
# print(F1.nutrition)
# print(F2.shape)
# print(F1.fruit_season)
# print(F2.color)

class Fruit(object):

    def __init__(self):
        print(" I am a Fruit : ")

    def nutrition(self):
        print (" I am rich in vitamin C :")
    def fruit_name(self):
        print('My Name is Orange :')

    def fruit_shape(self):
        print ("I come in different shapes :")

    def fruit_price(self):
        print("I am very cheap to buy :")

f= Fruit()
f.nutrition()
f.fruit_name()
f.fruit_shape()
f.fruit_price()

print("*"* 29)

class Mango(Fruit):
    def __init__(self):
        print('I am a MANGo Fruit: ')
    def fruit_taste(self):
        print('I am very sweet')
    def Availability(self):
        print('I am only available in Summer :')
m=Mango()
m.fruit_taste()
m.nutrition()
m.fruit_shape()
m.Availability()

print("*"* 29)
class Car(object):
    def __init__(self):
        print ("I am part of VW Group :")
    def make(self):
        print('I am AUDI : ')
    def model(self):
        print ('I am A4 model: ')
    def transmission(self):
        print('I can be automatic & manual: ')
c=Car()
c.model()
c.make()
c.transmission()

print("*"* 29)
class AudiA5(Car):
    def __init__(self):
        print ("I am Model A5 :")
    def Engine(self):
        print("I have powerful Engine:")
C2=AudiA5()
C2.Engine()
C2.make()
C2.transmission()

