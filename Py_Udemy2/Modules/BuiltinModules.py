"""
www.https://docs.python.org/3/library
MODULES ARE NOTHING BUT BUILT-IN FUNCTIONS
"""
import math  ## We need to import the Modules-BUT ITS NOT RECOMANDED TO IMPORT ALL MODULES JUST FOR ONE TIME USE IN 'CODE'-sO
from math import sqrt           ## THIS WAY WE CAN IMPORT ONLY WANTED MODULES
from CreateYourOwnModule import Kar ## THIS WAY WE "IMPORT THE MODULES MADE BY US-REFER TO CREATEYOUR OWN MODULES.PY"
from CreateYourOwnModule import kar2


class methods_demo():

    def builtin_modules(self):
        print(math.sqrt(100))  ## This way we can use the Methods imported
        #print(sqrt(50))  ## WHEN WE USE 'FROM MATH IMPORT SQRT' -THIS IS HOW WE CALL IT-wE DON'T HAVE TO TYPE "MATH.SQRT2" INSUCH SCENARIOS
        print (math.sin(10))
        print (math.cos(10))

    def kar_description(self):
        make= "Audi"
        model= "A4"
        engine = "2.2"
        color = "RED"
        Kar(make,model)
        kar2(engine,color)



m=methods_demo()
# m.builtin_modules()
m.kar_description()
