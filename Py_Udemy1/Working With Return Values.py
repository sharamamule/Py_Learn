"""
Whenever we write method we need to write 'dock-string' 
-like notes with in the method explaining what method is doing.

"""
def sum_nums(n1,n2):  ## dock string example :
      """
      Get sum of two numbers   
      :param n1:
      :param n2:
      :return:
      """
      return n1 + n2

sum1 = sum_nums(2,3)
sum2 = sum_nums(10,5)
string_add =sum_nums('Po ','bey') # This will concatinate and prints, hence a method can take any values strings,values once defined

print(sum1)
print(string_add)
print ("*********************")

def isMetro(city):
    l=['Hyd','Banglre','BZA','Chennai']
    if city in l:
        return True
    else:
            return False
x= isMetro('Kerala')
print(x)
