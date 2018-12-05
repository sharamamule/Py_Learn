x='XXX'
withR= ("Prints with quotes: %r" %x)
withS= ("Prints with quotes: %s" %x)
print(withR)
print(withS)

def f():
    global x
    print (x)
    for j in range(20):
        if z >2:
            x=4
