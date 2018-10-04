"""
Object Oriented Programming
"""
from Tools.i18n.msgfmt import make
""" 
# CAR is an object we have 'PROPERTIES/ATTRIBUTES'[color,make of the car model of the car, year of the car] for the CAR and 
# METHODS [start the car,drive,stop,break,engine start] to perform on this car'.
# Static things what defines our car are the properties of the car and we have METHODS that peform on the CAR.
"""
s = "this is a string"
#S.Upper
#s.lower() 
print(s.upper())

"""
** CLASS is a template that defines the OBJECT
"""
## ADVISED TO START 'CLASS' NAME WITH CAPITAL LETTER


class Car(object):

    def __init__(self, make, model, gear):
        self.make = make
        self.model = model
        self.gear = gear

c1 = Car('AUDI','A4','manual')
print(c1.make)
print(c1.model)
print(c1.gear)

c2 = Car('benz','A140','Auto')
print(c2.make)
print(c2.model)
print(c2.gear)

class Amzon(object):
    def __init__(self, Movies,Series, Cartoon):
        self.Movies = Movies
        self.Series = Series
        self.Cartoon = Cartoon

Sharat = Amzon('Die-hard','PriosnBreak','Rick& Morty')
print(Sharat.Movies)
print(Sharat.Series)
print(Sharat.Cartoon)

Asha = Amzon ('Avengers','OnceUPonAtime','Rhymes')
print(Asha.Movies)
print (Asha.Series)
print(Asha.Cartoon)
