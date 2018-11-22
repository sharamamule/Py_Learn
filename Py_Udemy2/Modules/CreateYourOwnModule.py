def Kar(make, *args):
    print('Make of Car is: '+ make)
    for arg in args:
            print ("another arg: ", arg)

Kar('Audi',"Benz",'A4','pusky','pobey')
    #print('Modle of car is :'+ model)

        ## Now we can use this model in a different code .[refer to built-in modules.py]

def kar2(engine,color):
    print("Engine is powerful : "+ engine)
    print("Color Guess? :" + color)

k1= Kar('Audi',"Benz",'A4')
k2=kar2('2.2','BLUE')

