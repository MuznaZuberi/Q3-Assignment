# Basic Import
from modules import studentname
print(f"Name : {studentname}")



# Import with Alias (as)

from modules import Countries as c
print(f"Countries : {c}")
		


# Import Specific Functions or Variables (from ... import ...)
from  modules import user_info , multiplication 
print(f"UserData : {user_info}")
print(f"Multiplication : {multiplication(9,9)}")



# Import Everything (from module import *) (Not recommended for large modules)
from  main import *
