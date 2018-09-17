class Car(object):
    def __init__(self):
        print ("You have selected the CAR")

    def drive(self):
        print ("Car Started")

    def start (self):
        print ("Car has to start")

    def stop (self):
        print ("Car has stopped")

class AUDI (Car):
    def __init__(self):
        Car.__init__(self) ## This will print the attributes from Parent
        print ("This is AUDI NOW")

    def Start (self):
        print ("Audi has Started") ## this is over-riding the parent class attribute         

    def drive (self):
        super(AUDI, self).drive()  ## This will enable to use 'drive' attributes from Parent
        print ("Audi Drives Smooth")

A= AUDI()
A.drive()
A.stop()
A.Start()

