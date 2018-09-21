# # """
# # Sequence of characters
# # can contain 'a-z, 0-9,special characters
# # Rule : is we need to use double or single quotes while defining them 
# # """

# # a = "this is a simple string"
# # b= 'Using single quotes'

# # print(a)
# # print(b)

# # c = "Need to Use 'Quotes' inside a string" # we can use single quotes inside if we have to to avoid error
# # print(c)

# # d = " Another way to \"handle\" the quotes" # \"handle\" by adding 2 back slashes the double quotes with in double quotes are handled
# # print(d)

# # e= " This is a very long string \
# #     make sure to add back \"slash\" " ## This was we can write a long string by using 'back-slash' 
# # print(e)

# """"
# StringMethods
# """
# ## Accessing characters in a string
#         # Strings are Index based and starts from Zero
# first = 'nyc'[1]
# city = 'Bezawada'
# print(first)
# bza = city[3]
# print(bza)

# ## Built in Strings 
#     # len() 
#     # lower() 
#     # str()
# stri = "THIS IS lower CASE" 
# print(stri.lower())   # this will print all in lower case
# print(stri.upper())   # this will print all in upper case
# print (len(stri))    # this will print the len of the string
# #print(str+2)    # This will throw error 
# print(stri + str(2))

# """
# Concatenation   
# """
# print("hellow "+ ""+ "World..!")
# print(stri + " "+ city)

# ## How do we repace some thing in a string...? - we use .replace (in-built function)
#     # " Replace Method"
# a = "abc123abc456"
# print(a.replace('abc','ABC')) 
# print("_____________")
# print (a.replace('abc','ABC',1)) # this will only change the first value as we mentioned it in the code 
#     # "sub-string method"
#     # Starting index is inclusive 
#     # Ending index is not inclusive 
# sub = a[1]
# print(sub) # this will print 'b' using index

# sub2 = a[1:6]
# step =a[1:6:3] ## this will print the the first and then skips next 2 & priunt the 3 with in first 5 numbers
# print(sub2)
# print('******')
# print(step)
# print('********')
# sub3 = a[1:-2]
# print(sub3)
# print ('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
# """
# Slicing the STRINGS
# """
# ab = 'This is a string'
# print(ab)
# print(ab[:])  # this will print the whole as [ : ] will do that
# print(ab[1:]) # this will print from 1st Index i.e 'his is a string'
# print (ab[:3]) # this will print 'Thi' from 0-2nd INDEX 
# print (ab[-4]) # 'minus' starts from last with Index 1.
# print(ab[:-1]) # this will print the whole except the last word as ':' is used and '- minus' is form back

# print(ab[::-1]) # this will reverse the string***

"""
Formatting Strings
"""
city = "Amaravathi"
state = "Andharapradesh"
print(" Welcome to  "+ city +" "+ "the capital is" +" "+ state) ## too many signs so there is a better way 

print ("Welcome to %s and CAPITAL is %s" %(city,state)) # the " %s" will use the variables and print
print ("<<<<<<<<<<<<<<<<<<<<<<<<")

myname = 'sharat'
mywifename = 'Asha'
mydaughtername ='Akshara'

print(" This is my family 'Tatineni' my name is %s and \
my betterhalf is %s '##' our beautiful \
 daughter name is %s " %(myname,mywifename,mydaughtername))
