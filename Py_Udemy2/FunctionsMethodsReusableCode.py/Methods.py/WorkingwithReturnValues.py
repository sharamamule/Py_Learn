"""
Method is a re-usable code which can perform the task we wanted to perform
Keyword = def 
"""
from test.test_concurrent_futures import _return_instance
def sum_num(n1,n2):
    return(n1 +n2)

s1=sum_num(2,3)
s2=sum_num(5,5)

print(s1)
print(s2)

def isMetro(city):
    l = ['BZA','HYD','TN','BAN']

    if city in l:
        return True
    else:
        return False

x = isMetro('BZA')
print(x)