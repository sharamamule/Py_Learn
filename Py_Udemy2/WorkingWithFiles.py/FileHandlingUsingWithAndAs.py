"""
With / As keywords = We can use these two instead of "close()" when working with 'files'
"""

with open ("Withas.txt","w") as with_as_write:    ## WE CAN USE ANY NAME AFTER AS LIKE 'FILE' etc
    with_as_write.write("This is an example of with as write/read") 

print ("*"*20)

print("Read Starts from here..!")
with open ("Withas.txt","r") as with_as_read: 
    print(str(with_as_read.read()))    
                  ## SO WE CAN OPEN A FILE AND CLOSE IT WITH OUT USING 'close()' in this way...!