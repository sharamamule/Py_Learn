class car (object):
    def __init_(self):
        print('This is the parent class : ')
    def drive(self):
        print('Drive means drive: ')
    def Stop(self):
        print('Stop means stop :')
    
class Audi(car):
    def __init__(self):
        print("AUDI is Inheriting 'Car' Properties: ")
    def drive(self):
            print('before driving check Fuel : ') ## THIS IS OVER RIDING THE 'PARENT -CLASS', SO THIS WILL BE PRINTED FOR DRIVE()
            super (Audi ,self).drive() ## BY USING "SUPER" WE CAN PRINT BOTH [PARENT] & [CHILD] - METHODS FOR DRIVE()
    def Go(self):
        print ('Go means drive fast :')

A= Audi ()
A.drive()
A.Stop()
A.Go()
