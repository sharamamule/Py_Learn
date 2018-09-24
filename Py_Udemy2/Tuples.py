"""
Tuple 
--is like LIST but they are Immutable * - only reason we use 'TUPLE' instead of LIST
  means you can't change them
"""

my_tuple = (1,2,4,4,5,2,2,2,3) # exactly like list but  we use " () " perenthisis
print(my_tuple)

print(my_tuple[1])

print(my_tuple[1:2])
print(my_tuple[2:])
print(my_tuple.index(2)) # fninding Index of Tuple

print(my_tuple.count(2)) # this will print the number times '2' is there in tuple