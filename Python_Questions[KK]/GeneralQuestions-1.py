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
# 3.You try to modify object ID 1, but it’s immutable, so you can’t change the content. Because of this, it looks at the value of object ID 1, 
# adds 10 to it to get 11, and creates a new integer object (ID 2) with a value of 11. It then re-binds “int_two” to object ID 2, but leaves “int_one” alone.
# 4.Since “int_one” and “int_two” are now bound to different objects, printing them will give different results.
# 5.If you were to change the value of “int_two” again, it would create a third object with the new value and leave the second object in memory with no bindings. 
# Don’t worry about wasted memory, though. That’s what garbage collection is for.

"""
4) Why is the “pass” keyword used for in Python?
Ans: In python prgoramming, 'Pass' is a null statement.The difference between a comment and 'pass' statement in Python is that, 
     while the interpreter ignores a comment entirely, 'pass' is not ignored.
     Nothing happens when pass is executed. It results into no operation (NOP).
"""
# Suppose we have a loop or a function that is not implemented yet, but we want to implement it in future.
# They can not have an empty body. The interpreter would complain.
# So, we use the 'pass' statement to construct a body that does nothing.
# pass is just a placeholder for functionality to be added later.
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

"""
5) Why is <__init__.py> module used for?
Ans:  Files named_init_.py are used to mark directories on disk as a Python pacakage directories. If you have the files
      mydir/spam/__init__.py
      mydir/spam/module.py
   and mydir is on your path, you can import the code in module.py as :
    import spam.module
      or
    from spam import module
    --> If you remove the __init__.py file, Python will no longer look for submodules inside that directory, 
        so attempts to import the module will fail.
    --> The __init__.py file is usually empty, but can be used to export selected portions of the package under more convenient names, 
         hold convenience functions, etc. Given the example above, the contents of the __init__ module can be accessed as  
                      import spam
"""
"""
6) Differentiate between .py and .pyc files?
Ans:  Python compiles the ".py" files and saves it as ".pyc" files , 
      so it can reference them in subsequent invocations. 
      The .pyc contain the compiled bytecode of Python source files,which is what the Python interpreter compiles the source to. 
      This code is then executed by Python's virtual machine .
    Example : For example, When you run myprog.py source file, 
              the python interpreter first looks to see if any 'myprog.pyc' (which is the byte-code compiled version of 'myprog.py') exists,
              and if it is more recent than 'myprog.py'. If so, the interpreter runs it. 
              If it does not exist, or 'myprog.py' is more recent than it (meaning you have changed the source file), 
              the interpreter first compiles 'myprog.py' to 'myprog.pyc'. 
"""
"""
7) Explain how Python does Compile-time and Run-time code checking?
Ans:  Python performs some amount of compile-time checking, 
      but most of the checks such as type, name, etc are postponed until "code execution". 
      Consequently, if the Python code references a user -defined function that does not exist,
      the code will compile successfully. In fact, the code will fail with an exception only when the code execution path references the function which does not exists.
      Examples of 'Compile time errors' -Syntax errors-Typechecking errors-Compiler crashes (Rarely)
      Examples of 'Run time errors' -Division by zero-Dereferencing a null pointer -Running out of memory
"""
"""
8) How memory is managed in Python?
Ans:  --> Memory management in Python involves a private heap containing all Python objects and data structures
          Interpreter takes care of Python heap and that the programmer has no access to it.
      --> The Allocation of heap space for Python objects is done by Python memory manager.
          The Core API of Python provides some tools for the programmer to code reliable and more robust program.
      --> Python also has a build-in garbage collector which recycles all the unused memory. When an object is no longer referenced by the program,
          the heap space it occupies can be freed.The garbage collector determines objects which are no longer
          referenced by the sprogram frees the occupied memory and make is available to the heap space.
      --> The gc module defines functions to enable/disable garbage collector:
"""
# gc.enable() -Enables automatic garbage collection.
# gc.disable() -Disables automatic garbage collection.

"""
9) what is the use of "setup.py" in python
Ans:  "setup.py" is a python file, which usually tells you that the module/package you are about to install has been packaged and distributed with Distutils, 
       which is the standard for distributing Python Modules.
    This allows you to easily install Python packages.
"""
# Often it's enough to write: " python setup.py install "  #  and the module will install itself.

"""
10) what is the use of __init__==__main__: condition in python?
Ans:  In Python all modules have some built-in attributes. "__name__" is one of them.
    --> Case 1: Running the module directly :
                If you run the module directly in a standalone program then in that case the value of " __name__" attribute is set to "__main__"
    --> Case 2: Using the module with import :
                If you use the module in another program (using the import function), 
                then in that case the value of "__name__" attribute is set to the filename of the module.  
"""   
# Example: Create a file with name "my_module.py"
foo = 100

def hello():
    print("i am from my_module.py")
if __name__ == "__main__":
    print ("Executing as main program")
    print("Value of __name__ is: ", __name__)
    hello() 
    # Here we have defined a new module "my_module" . 
""" OUT-PUT :
# Executing as main program
# Value of __name__ is:  __main__
# i am from my_module.py
--> here we are creating a new module and executing it as main program so the value of "__name__" is set to '__main__' . 
    As a result if condition satisfies and "hello() " function gets called.
"""
# Now create a new file called "using_module.py"  and write the following code
# import my_module
 
# print(my_module.foo)
# my_module.hello()
 
# print(my_module.__name__)
""" OUT-PUT :
100
i am from my_module.py
my_module
--> As you can see now if statement in my_module  fails to execute because the value of __name__  is set to 'my_module'
"""