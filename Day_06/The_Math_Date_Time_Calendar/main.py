import math
import time
import calendar
from datetime import date
import datetime
# =================The Math & Date Time Calendar=====================

# 1) Getting the Current Time
print("****Getting the Current Time****")
CurrentTime = time.localtime(time.time())
print("Current Local Time" , CurrentTime)
print("\n")



# 2) Getting the Formatted Time (using asctime() function)
print("*****Getting the Formatted Time******")
FormatedTime= time.asctime( time.localtime(time.time()) )
print ("Local current time :", FormatedTime)
print("\n")


# 3) Getting the Calendar for a Month
print("******Getting the Calendar for a Month********")
cale = calendar.month(2025 , 4)
print("Here is the calendar for April 2025:")
print(cale)
print("\n")



# 4) The Date Time
print("*****Getting The Date****")
Date = date(2025 , 4 , 11) 
print("Today Date:" , Date)
print("\n")



# 5) The DateTime
print("*****Getting The DateTime******")
x = datetime.datetime.now() #The date contains year, month, day, hour, minute, second, and microsecond.
print(x)
print("\n")





# =============Python Math Module============
print("======= Python Math Module =======")

# a) pow() raises a number to a power
print("**** pow() Method *****")
print(f"Power of 3 is = {pow(4 , 3)}")
print("\n")


# b) round() rounds a number to a specified number of decimal places
print("***** round() Method ******")
print(f"Round Figure (3.14169)  = {round(3.14169 , 3)}")
print("\n")


# c) max() returns the largest of a set of numbers
print("***** max() Method *******")
print(f"Max Value (10,29,100,100000,900,1) is = {max(10,29,100,100000,900,1)}")
print("\n")


# d) min() returns the smallest of a set of numbers
print("***** min() Method ******")
print(f"Min Value (19 , 100 , 1290, 3) is = {min(19 , 100 , 1290, 3)}")
print("\n")


# e) math.sin() returns the sine of an angle in radians
print("***** sin() Method *******")
print(f"math.sin(math.pi/2) = {math.sin(math.pi/2)}") 
print("\n")



# f) math.cos() returns the cosine of an angle in radians
print("***** sin() Method *******")
print(f"math.cos(0) = {math.cos(0)}")
print("\n")



# g) math.tan() returns the tangent of an angle in radians
print("***** tan() Method *******")
print(f"math.tan(math.pi/4) = {math.tan(math.pi/4)}")
print("\n")



# h) math.sqrt() returns the square root of a number
print("***** sqrt() Method *******")
print(f"math.sqrt(81) = {math.sqrt(81)}")
print("\n")


# i) math.factorial() returns the factorial of a number
print("****** math.factorial() Method ******")
print(f"factorial(7) = {math.factorial(7)}")
print("\n")


# j) math.log() returns the natural logarithm of a number
print("***** log() Method *****")
print(math.log(2 , 4))
print(math.log(20))
print(math.log(19.3))
print("\n")


# k) # math.log10() returns the base-10 logarithm of a number
print("**** math.log10() Method *****")
print(math.log10(20))
print("\n")



# l) math.exp() returns the value of e raised to a power
print("**** math.exp() Method *****")
print(f"math.exp(2) = {math.exp(2)}") 
print("\n")



# m) math.ceil() returns the smallest integer greater than or equal to a number
print("**** math.ceil() Method ****")
print(f"math.ceil(20.18) = {math.ceil(29.3)}")
print("\n")



# n) math.floor() returns the largest integer less than or equal to a number
print("******* math.floor() Method ********")
print(math.floor(100.11))
print(f"floor rounds towards negative infinity (-2091.10) = {math.floor(-2091.10)}")
print("\n")



# 0) math.pi is a constant representing the ratio of a circle's circumference to its diameter
print("******* math.pi Method ******")
print(f"math.pi = {math.pi}")
print("\n")


# p)  math.e is a constant representing the base of the natural logarithm
print("****** math.e Method ******")
print(f"math.e = {math.e}")
print("\n")



# q)  math.tau is a constant representing the ratio of a circle's circumference to its radius
print("****** math.tau Method *****")
print(f"math.tau = {math.tau}")
print("\n")



# r)  math.inf is a constant representing infinity
print("**** math.inf Method *****")
print(f"math.inf =  {math.inf}") 
print("\n")




# s)  math.nan is a constant representing "not a number"
print("******** math.nan Method ********")
print(f"math.nan =  {math.nan}")