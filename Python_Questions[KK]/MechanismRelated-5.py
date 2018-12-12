"""
1) Explain the use of "with" statement?
ANS:  The advantage of using a "with" statement is that it is guaranted to close the file no matter how thenested block exists.
      If an exception occurs before the end of the block , it will close the file before the exception is caught by an outerexception handler.
      If the nested block were to contain a 'return' statement, or a 'continue' or 'break' statement, the 'with' statement would automatically close the file in those cases, too.
"""
## EXAMPLE:
"""
with open('output.txt', 'w') as f:
    f.write ('hi there!') 
           ##  The above 'with' statement wll automatically close the file after the nested block of code.
"""