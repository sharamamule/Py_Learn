def make_and_model_of_my_car (car1,car2,car3,car4):
    print ("mycar1:", car1)
    print("mycar2:",car2)
    print ("mycar3:", car3)
    print ("mycar4:", car4)
Kwargs = {"car4":"audi", "car2":"benz","car3":"honda"}
make_and_model_of_my_car("bmw", **Kwargs)

def make_lorry(lorry1,lorry2,lorry3):
    print("My Lorry: ", lorry1)
    print ("my lorry2 :", lorry2)
    print ("my lorry3: ", lorry3)
Kwargs = {"lorry3":"TATA","lorry2":"ACER"}
make_lorry("BENZ", **Kwargs)