"""
Create a dictionary " car"
create 3 keys
-make
-model
-year

Try to access the color key.It will throw an exception as there is not 'color' key , handle exception using
try, except and finally block
"""

def exceptionhandlgin():
    try:
        Car = {"make":"Honda","model":"4x4","YEAR":"2010"}
        print (Car["make"])  ## This will print the 'Value' for -'Make'
        print (Car["color"])  ## This will print the 'Exception' 
        
    except:
        print("THERE is an exception in printing the Key : ")
    finally:
        print("Please try another Key")
exceptionhandlgin()
