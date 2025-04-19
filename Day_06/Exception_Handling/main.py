# ====================Exception Handling with try, except, else, and finally=====================


# 1) =======The try Block========
print("********This example demonstrates the use of the 'try' block for exception handling*******")
# example_01
try:
    result = 10 / 0  
    print(result)
except:
	print("Error!")


# example_02
number = 20
try:
	print(num)
except NameError as n:
	print("Error Caught:" , n)

print("\n")






# 2) ========= The except Block ==========
print("*******This example demonstrates the use of the 'except' block for error handling*******")
username : str = "John"
userage: int = 29
try:
	user_data = username + userage
	print(user_data)
except TypeError as te:
	print("TypeError!")
except Exception as e:
	print("Opzzzzzzzzz!")
print("\n")







# 3) ==========The else Block============
print("*******This is an example of using the 'else' block after a try-except*******")

user_id: str = "18661"
user_password: str = "john@22yahooo.com"

correct_userid = "18661"
correct_userpassword: str = "john@22yahooo.com"

try:
    if user_id == correct_userid and user_password == correct_userpassword:
        print("Congrats! You're Login Successfully")
    else:
        raise ValueError("Invalid user_id or user_password!") 

except Exception as e:
    print(f"Error: {e}")

else:
    print("This is executed after try block, as there is no exception!")

print("\n")





# 4) ========== The finally Block =============
print("*******This is an example of using the 'finally' block*******")
abc = 21
try:
	res = abc*2
	print(f"Multiplication: {res}")
except Exception as e:
	print("Error!" , e)
finally:
	print("This will always execute")
print("\n")







# 5) Putting It All Together
print("********Here’s an example that combines all four blocks**********")
def DivisionTesting(p:int,q:int):
	try:
		result = p/q
	except ZeroDivisionError as zd:
		print("error!" , zd)
	else:
		print("Divided Successfully!" , result)
	finally:
		print("This will always execute")

DivisionTesting(10,20)
DivisionTesting(10,10)
DivisionTesting(80,0)





