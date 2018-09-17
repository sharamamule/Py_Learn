class Fruit (object):
    def __init__(self):
        print ("We should eat summer fruits")

    def nutrition(self):
        print("The nutrition levels are high in Summer fruits")

    def fruit_shape(self):
        print ("Some fruits come in funny Shapes")

class Mango(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print ("Mango is also a summer fruit....")

    def nutrition(self):
        print ("Mango Nutrition levels are awsome")

    def color(self):
        print ("The color of Mango fruit is Yellow")

f=Fruit()
f.nutrition()
f.fruit_shape()

print ("****************")

m=Mango()
m.nutrition()
m.color()
m.fruit_shape()


