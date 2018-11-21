"""
--The 'datetime module' supplies classes for manipulating dates and times in both simple and complex ways.
-- "datetime.now(tz=None)"  : returns the current local date and time. If optional argument 'tz' is None or not specified,
   this is like 'today()'
-- "date.strftime(format)" returns a string representing the date, controlled by an explicit format string. 
   Format codes referring to hours, minutes or seconds will see 0 values.
"""
import datetime
#now = datetime.datetime.now()
print ("Current date and time : ")
print (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) ## THIS TO PRINT THE DATE WITH TIME IN SECONDS 
print (datetime.datetime.now())

import calendar     
       ### Python calendar.,month (theyear, themonth, w=0 , i=0):
                    ## THE FUNCTION RETURNS A MONTH'S CALENDAR IN A MULTI-LINE STRING USING THE " formatmonth("") OF THE TextCalendar CLASS.
                       ## ' i ' specifies the number of lines that each week will use.

y= int(input("Input the year : "))
m=int(input("Input the month : "))
print(calendar.month(y,m))