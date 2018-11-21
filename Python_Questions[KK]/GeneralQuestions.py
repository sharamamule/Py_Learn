"""
3) Does Python allow arguments Pass by Value or Pass by Reference?
Ans:   Arguments are passed neither by value and nor by reference in Python - 
       instead they are passed by "assignment".
       The parameter passed in is actually a reference to an object, 
       as opposed to reference to a fixed memory location but the reference is passed by value.
       In addition, some data types (like strings, tuples etc) are immutable whereas others are mutable.
"""
list_one = [1, 2, 3, 4]
list_two = list_one
list_one.append(5)
print(list_two)
# [1, 2, 3, 4, 5]

# Here’s what’s happening under the hood, more or less:
# 1.You create a list object with the value [1, 2, 3 ,4]. 
# 2.We’ll call this object ID 1. You then bind the name “list_one” to object ID 1.
# 3.You tell it to bind “list_two” to the same object that “list_one” is bound to. At this point, they’re both bound to object ID 1.
# 4.You modify object ID 1. Because a list is mutable, the contents can change and the both names can remain bound to ID 1.
# 5.Since both “list_one” and “list_two” are bound to object ID 1, printing either of them returns [1, 2, 3, 4, 5].


int_one = 1
int_two = int_one
int_two += 10
print(int_one)
# 1
#The same thing is happening, but the object type makes a difference:
# 1.You create an integer object with a value of 1. We’ll call this object ID 1. You then bind the name “int_one” to object ID 1.
# 2.You tell it to bind “int_two” to the same object that “int_one”is pointing to. They’re both bound to object ID 1.
# 3.You try to modify object ID 1, but it’s immutable, so you can’t change the content. Because of this, it looks at the value of object ID 1, adds 10 to it to get 11, and creates a new integer object (ID 2) with a value of 11. It then re-binds “int_two” to object ID 2, but leaves “int_one” alone.
# 4.Since “int_one” and “int_two” are now bound to different objects, printing them will give different results.
# 5.If you were to change the value of “int_two” again, it would create a third object with the new value and leave the second object in memory with no bindings. Don’t worry about wasted memory, though. That’s what garbage collection is for
