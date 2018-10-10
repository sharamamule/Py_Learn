"""
Exceptions ar errors
We should handle exceptions in our code
to make sure the code is working the way we want and is handling all the unwanted issues
URL:https://docs.python.org/3/library/exceptions.html [ We don't have to remember these]
"""

def exceptionhandling():
    try:
        a=10
        b='String'
        c=0

        d= (a+b)/c
        print(d)
    # except ZeroDivisionError:  ## WE CAN HAVE MULTIPLE 'EXCEPT' BUT NOT EASY TO REMEMBER ALL HENCE WE USED ONE 'EXCEPT'
    #     print('Zero Division Error : ') 
    # except TypeError:
    #     print('Type Error Exception')
    except:
      print ("Exception is handled because of Error :")

exceptionhandling()