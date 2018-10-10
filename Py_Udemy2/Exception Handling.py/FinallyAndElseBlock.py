"""
Exceptions are errors
'Else' with other conditions only seen in 'Python'
"""

def exceptionhandling():
    try:
       a=20
       b=2
       c=0
       d=(a+b)/c
       print(d)
    except:
        print ('Exception is handeled')
##  raise Exception (" This will RAISE all the Details of Exception") ## THIS WILL PRINT ALL THE EXCEPTIONS
    else:              ## 'ELSE' IS ONLY EXECUTED IF THE EXCEPTION IS NOT HANDELED.
        print ("No Exception hence Else is printed")
    finally:                                   ## 'FINALLY' IS ALLWAYS EXECUTED
        print("FINALLY is allways printed")

exceptionhandling()
