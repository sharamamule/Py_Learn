class car(object):
    def __init__(self):
        print("I just created Car Instance: ")

    def drive(self):
        print(" The car is ready to drive :")
    def stop(self):
        print (" The Car has stopped")

c= car()
c.drive()
c.stop()

class Audi(car): ## WE ARE USING 'CAR' INSTEAD OF OBJECT MEANS THE CAR PROPERTIES ARE 'INHERITED'
    def __init__(self):
        print (" Car properties are inherited to AUDI :")
A= Audi()
A.drive()
A.stop()

print ("*"*20)

class Movie(object):
    def __init__(self):
        print("What..! ")
    def Prime (self):
        print("Prime movies/Series are boring :")
    def Netflix (self):
        print('Netflix movies/Series are interesting: ')
    def YuppTv (self):
        print('Yup Tv is good for Regional Movies: ')
M1= Movie()
M1.Prime()
M1.Netflix()
M1.YuppTv()
print ("*"*20)
class TvSeries(Movie):
    def __init__(self):
        print('****---Tv Series comparision...!: ')
    def Youtube (self):
        print('Youtube is Expensive to watch: ')
TV =TvSeries()
TV.Prime()
TV.Netflix()
TV.YuppTv()
TV.Youtube()
    
