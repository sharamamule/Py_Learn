"""
Tuple 
--is like LIST but they are Immutable * - only reason we use 'TUPLE' instead of LIST
  means you can't change them
--> A tuple is container which holds a series of comma separated values (items or elements) between parentheses such as an (x, y) co-ordinate. 
   Tuples are like lists, except they are immutable (i.e. you cannot change its content once created) and can hold mix data types.
"""

my_tuple = (1,2,4,4,5,2,2,2,3) # exactly like list but  we use " () " perenthisis
print(my_tuple)

print(my_tuple[1])

print(my_tuple[1:2])
print(my_tuple[2:])
print(my_tuple.index(2)) # fninding Index of Tuple

print(my_tuple.count(2)) # this will print the number times '2' is there in tuple