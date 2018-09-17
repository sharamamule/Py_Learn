# Accessing characters in a string
# Index starts from 0 in python 
first = "hello"[0]
city ='nottingham'
print(first)
ft = city[4]
print(ft)

"""
In-buit Strings :
len()
lower()
upper()
str()
replace()
sub()
step()
split()
"""

stri = "THIS IS a TEST CASE"
print(stri.lower())
print(len(stri))
print (stri.upper())

print(stri + str(2))

"""
Concatenation
"""

print("hellow "+ ""+ "World")

print ("today "+ ""+ "tomarrow "+""+ "working "+ ""+ "then its holiday!!")

a = "abc1abc2abc3abc4abc"
print(a.replace('abc','ABC'))
print('********')
print (a.replace ('abc', 'ABC',3))

print("*********")

a = "1abc2abc3abc"
sub = a[0:6]    # this will print from 0-5 index for a
step = a[1:6:2] # this will start from 1th index and skip the nxt and so on till 5th index 

print(sub)
print(step)

# **  String Slicing :
a= "Hellow is a world matters"
print (a[3:]) # will start from 3rd Index and go till the End
print (a[-2])
print (a[::]) # Returns every thing
print (a[::2]) 

print (a[::-1]) # this will reverse string
print (a)

# **  String Formatting :

city = "Nottingham"
event = "stand up Comedy"
presenter = "Russell Peter"
along = "AR Rehman"
print(" Welcome to " + city + ""+ " and enjoy " + event + " by " + presenter) # this can be written in a different way ?

print("welcome to %s " % city) # this will only print one variable.
print("welcome to %s and enjoy the %s by %s" % (city,event,presenter)) # Variables are used and replaced with help of " % " sign
print("------------------------")
print ("welcome to %s and enjoy the %s by %s along with %s" % (city,event,presenter,along))
    # Make sure the number of '%s' sings used relate to number of  '%' variables entered at the END

