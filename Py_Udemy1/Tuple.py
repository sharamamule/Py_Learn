"""
TUPLE like LIST but they are 'immutable' [means can not change]
Have only 2 inbuilt - index & Count
"""

my_list= [1,2,3,4]
print(my_list)

my_list[0] =0
print(my_list) # we have changed the value of 0th to 0 from 1

my_tuple =(0,2,3,5,6,4,8,4)
print(my_tuple)

## my_tuple(2) =3 - will throw an ERROR as Tuple is Immutable.

print(my_tuple[3])
print(my_tuple[1:])
print (my_tuple.index(6)) # Index here will show the 5th value i.e 4
print(my_tuple.count(2)) # count of 2 =1 , i.e number of 2's available
