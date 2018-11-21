"""
File I/O
'W' -> Write-Only Mode
'r' -> Read-Only Mode
'r+' -> Read And Write Mode
'a' -> Append Mode
"""
my_list = [1,2,3]

my_file=open("firstfile.txt","w")

for item in my_list:
    my_file.write(str(item)+ "\n") ## "\N"- WILL ALLWAYS PRINTS IN THE NEXT LINE

my_file.close()


my_dictionary = {'Make':'Audi','Model':'A4'}

my_file = open ("CardDetails.txt","w")

my_file.write(str(my_dictionary['Make'])+ "\n")
my_file.write(str(my_dictionary['Model'])+ "\n")

my_file.close()

my_file= open("Tatineni.txt", "w")
my_file.write (str("My Surname is Tatineni: "+ "\n"))
my_file.write (str("My Nams is Sharat : "+ "\n"))
my_file.write (str("I am married to Asha : "+ "\n"))
my_file.write (str("We have a beautiful daughter : "+ "\n"))
my_file.write (str("Her name is Akshara: "+ "\n"))

my_file.close()