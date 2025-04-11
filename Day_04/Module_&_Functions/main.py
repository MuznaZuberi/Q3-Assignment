 # ==========================Module & Functions(A module in Python is a file that contains Python code (functions, classes, variables, or even runnable code) and is used to organize and reuse code efficiently)====================

 # =======Types of Modules in Python======
 # 1) Built-in Modules(Standard Module)
 # 2) User Defined Modules(Custom Module)
 # 3) External Modules(Third Party Library)




# 1) ==========Built-in Modules(Standard Module)==============
# . Pre-installed modules in Python
# . math, random, os, sys
import math , random
print(math.sqrt(100)) 
print(random.randint(1,20)) #generate random number between 1 to 20



# 2) ===========User Defined Modules(Custom Module)=========
def user_data(name : str , gender : str , age : int): # With parameters
	print(f"Name : {name}  , Gender :  {gender} ,  Age : {age}")


def greeting(): # Without Parameters
	print("Hello Python!")
print("\n")

def addition(a,b): # parameters
	return a+b
print(addition(10,20)) # With arguments
print("\n")



personal_details = {
	"name" : "Arifa Amir Zubairi",
	"age" : 21,
	"gender" : "Female",
	"nationality" : "Pakistan",
	"city" : "Karachi",
}

print(personal_details)
print("\n")




# 3)  =============External Modules (Third-party Libraries)==============
# . Installed via pip (pip install module_name).
# . Example: numpy, pandas, requests






# =============Syntax to Define a Python Function==============
print("**********Syntax to Define a Python Function:************")

# EX_01
def greet():
	print("Hello Janifer! hope you are doing well")
greet()
print("\n")




# EX_02
def data(name : str , age: int , isdeveloper : bool):
	return name , age , isdeveloper
print(data("Ellie" , 29 , True))
print("\n")




# EX_03
num_01 : int = 10
num_02 : int = 91
def abc():
	if num_01 == 10 and num_02 == 91:
		print(f"Addition : {num_01 + num_02}")
	else:
		print("Opzzzzzzzz Invalid Integer!")

abc()
print("\n")




# EX_04
x : float = 20.9
def floating():
	x = 22.11
	y = x
	return y
print(floating())
print("\n")




# EX_05
def looping():
	for r in range(10):
		print(f"Num : {r}")
looping()
print("\n")




# EX_06
def Invitation():
	guest : list = ["Alaya" , "Aizal" , "Amal"]
	for g in guest:
		if g in "Aiman":
			print(f"Hello!{g}")
		elif g in "Amal":
			print(f"Hello!{g} wellcome to the birthdaY party")
Invitation()
print("\n")





# EX_06
def UpperCase():
	message = "hello world!"
	print(message.upper())
	print(message.lower())
	print(message.title())
UpperCase()
print("\n")



# EX_07
def add(*m):
	return sum(m)

print(f"Sum of total: {add(10,20,1000,29991)}")
print("\n")




# EX_08
# Default Arguments
def default_func(a : int , b = 10):
	return a+b
print(default_func(10,90))
print("\n")


def info(user_name : str = "Ushba"):
	return user_name
print(info("Izma"))
print("\n")





#EX_09
# Optional Arguments
def optional_func(a:int , b = 0):
	return a+b
print(optional_func(1))
print(optional_func(1000,22))
print("\n")




# EX_10
print("******** '/' Positional-only arguments*******")
def PositionalArgu(a:int , b:int , / , c:int):
	return a+b+c
print(PositionalArgu(20,20,c=100))
print("\n")




# EX_11
print("******** '*' Keyword-only arguments*******")
def KeywordArgu(*, a:int , b:int , c:int):
	return a*b*c
print(KeywordArgu(a=20,b=20,c=100))