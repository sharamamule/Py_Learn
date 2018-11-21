"""
File I/O
Reading a file -> .read()
Reading libe by line -> .readline()
"""
my_file=open("Tatineni.txt","r")

print(str(my_file.read()))

my_file.close

print(" Line by line ========>")

my_file_line= open("Tatineni.txt", "r")
print(str(my_file_line.readline())) ## THIS WILL READ LINE BY LINE FROM THE TEXT
print(str(my_file_line.readline())) ## iF WE WANT TO READ EACH EVERY WE USE 'FOR-LOOP' ETC