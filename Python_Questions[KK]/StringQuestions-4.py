"""
1) What is slicing in Python? Explain with example.
ANS:  The object is used to slice a given sequence (String, bytes, tuples, list or range) or 
      any object which supports sequence protocol (implements _getitem_() and _len_() method).
      
      ## slice Object represents the indices specified by range(start, stop, step)
"""
# Syntax of slice () are :
"""
slice(stop)
slice(start, stop , step) """

ab = 'This is a string'
print(ab)
print(ab[:])  # this will print the whole as [ : ] will do that
print(ab[1:]) # this will print from 1st Index i.e 'his is a string'
print (ab[:3]) # this will print 'Thi' from 0-2nd INDEX 
print (ab[-4]) # 'minus' starts from last with Index 1.
print(ab[:-1]) # this will print the whole except the last word as ':' is used and '- minus' is from back
print(ab[::-1]) # this will reverse the string***

## In order to retrieve substring from the string you have to use "slicing" operator. 
#     it's as simple as inputting the desired start postion of the string as well as the desired end postion.
cbn= 'This is the capital city of Amaravathi..' 
print(cbn[:5])
print(cbn[4:7])
print (cbn[7:12])
print (cbn[28:38])
print ("***************")
print (cbn[::-2])
print ("***************")

s = 'Hello, everybody!'
sl = slice(2)
sl2 =slice(1,2,3)
      
print (s[sl])  # Output ='sh'
print(s[sl2])  # Output= 'h'

"""
2) What is a negative index in Python?
ANS:  Negative index is used in python to index starting from the last element of the list,tuple or any other container class
      which supports indexing.
      "-1" refers to the last index & "-2 "refers to the second last index and so on.
For lists :
     array = [1,2,3,4,5]
    array[-1] = 5
For strings :
    string = "Hellow!"
    string[-2] =W
 ** This is useful when you don't have the length of the container, 
    and want to reference a position relative to the last index without having to calculate the length.
"""
"""
3) What is the best way to split a string in Python?
ANS :  "split()" method returns a list of strings after breaking the given string by the specified separator.
"""
# Syntax : str.split(seperator, maxsplit)
        # Seperator - The is a "delimiter." The string splits at this specified separator. If is not provided then any white space is a separator.
        # Maxsplit  - It is a number, which tellus us to split the string into maximum of provided number of times. If it is not provided then there is no limit.
## Example 
print ("############")
text = 'geeks for geeks'
print (text.split())      ## SPlits at space -OUTPUT= ['geeks', 'for', 'geeks']

word ='geeks, for, geeks'
print (word.split(','))   ## SPlits at ' , ' -OUTPUT= ['geeks ', ' for', ' geeks']

word = 'geeks:for:geeks'
print(word.split(':'))

word = 'CatBatSatFatOr' #*****#
print([word[i:i+3] for i in range(0, len(word), 3)]) ## Splitting at 3 -OUTPUT = ['Cat', 'Bat', 'Sat', 'Fat', 'Or']

"""
4) What is the right way to transform a Python string into a list?
ANS: The "list()" function will convert a string into a list of single-character strings.
"""
#EXAMPLE:
ab='hellow'
print(list(ab)) ## OUTPUT-['h', 'e', 'l', 'l', 'o', 'w']

## Even with out converting them to lists, strings already behave like lists in severways.
  # as we can access individual characters (as single-character strings) using brackets.
ab= 'hello'
print (ab[2]) # OUTPUT -l

## You can also loop over the characters in the string as you can loop over the elements of a list:
for ab in 'hellow':
 print (ab+ab)

"""
5) How will you convert a string to a number in Python?
ANS:  You can use the functions "int(s)" to convert a string or number to an integer.
      You may also need to use float(s) to convert a string or number to a floating point number or combination of both as follows: 
int(s)
float(s)
int(float(s))
"""
s= "1234"
i = int(s)
print( i+1)

