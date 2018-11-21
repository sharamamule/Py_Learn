"""11.
Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 
Sample function : abs()
Expected Result : 
abs(number) -> number
Return the absolute value of the argument.
"""
print ("*"*20+ 'Solution 11:')

print(abs.__doc__)   ## SOLUTION-1

func_help= input("Enter a valid Python function name:") ## SOLUTION:2
display=help(func_help)
print(display)

"""12.
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module. 
"""
print ("*"*20+ 'Solution 12:')

