"""
Inheritance : The process where we can use the methos defined in another 'Class'

"""
class Car(object):
    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Card started...")

    def stop(self):
        print("Car Stopped")

class Honda(Car): ## We r inheriting from the 'Car' class not the object
            
    def __init__(self):
        print("You just created HONDA Instance")     
        
C= Car()
C.drive()
C.stop()

h=Honda()
h.drive()
h.stop()