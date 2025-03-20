# =============Control Flow==============(Control flow refers to the order in which statements are executed in a program. In Python, decision-making is achieved using if, elif, and else statements, along with comparison and logical operators)

# ===================If Statement====================
# 1) The if Statement(The if statement is used to execute a block of code only if a condition is True)

name : str = "John Ellie";
if name == "John Ellie":
	print("Hello" , name);


print("\n")



# ===================Else Statement=====================
# 2) The else Statement (The else statement is used to execute a block of code if the if condition is False)

user_email : str = "John22@gmail.com";
user_password : int = 2991;

if user_email == "John22@.com" and user_password == 299:
	print(f"User Name: {user_email} User Password: {user_password}");

else:
	print("Opzzzzzz Invalid user_email & user_password");





print("\n")




# ==============Elif Statement==================
# The elif Statement(The elif statement is used to check multiple conditions. It stands for else if)
student_name : str = "Muzna Amir";
student_age : int = 24;
is_developer : bool = "Full Stack Developer";

if student_name == "Nick" and student_age == 21 and is_developer == "Full Stack Developer":
	print(f"Hi! I'm {student_name} My age is : {student_age} and I'm Full Stack Developer{is_developer}")

elif student_name == "Ellie" and student_age == 19 and is_developer == "Full Stack Developer":
	print(f"Hi! I'm {student_name} My age is : {student_age} and I'm Full Stack Developer{is_developer}")


elif student_name == "Muzna Amir" and student_age == 24 and is_developer == "Full Stack Developer":
	print(f"Hi! I'm {student_name} Mine age is {student_age} and I'm {is_developer}")


elif student_name == "Cristopher" and student_age == 17 and is_developer == "Full Stack Developer":
	print(f"Hi! I'm {student_name} My age is : {student_age} and I'm Full Stack Developer{is_developer}")


else:
	print("Invalid Student Info!");






print("\n")




# ===============Nested Statement====================
# Nested if Statements

# Example_01
num : float = 20.1;
if num < 20.2:
	if num == 20.1:
		print(f"This is {num} float")

	else:
		print("Inner Condition Falied")

else:
	print("Outer Condition Falied") 



print("\n")


# Example_02
course : str = "WEB Developement";
if course != "Graphic Designing":
	if course == "WEB Developement":
		print(f"Hurry up! Book your slot. Our {course} course is now available.")
	else:
		print("Course isn't available!")
else:
	print("All slots are full!")








# ==============Loops============(Loops are used to repeat a block of code multiple times. Python supports two types of loops)
# 1) =====for loop======(Used to iterate over a sequence (e.g., lists, strings, or ranges).) 

guest_list :str = ["Zimal" , "Izma" , "Ushba" , "Sundus" , "Mikal" , "Zunaiba"]
for guest in guest_list:
	print(f"Hi! {guest} You are cordially invited to a delightful dinner looking forward to your presence! 😊")


print("\n")


if "Unaiba"  not in guest_list:
	print(f"Dear Unaiba Apologies for the confusion, but this dinner invitation wasn’t intended for you. Hope to meet another time! 😊") 



print("\n")



admin_name : str = "Moin";
for admin in admin_name:
	print(admin)



print("\n")


num_looping  = range(20);
for n in num_looping:
	print(f"It's number : {n}")



print("\n")






# 2) =======while Loop=========(The while loop repeats a block of code as long as a condition is True)
count : int = 1;
while count <= 10:
	print(count)
	count += 1


print("\n")


count : int = 2;
while count <= 6:
	print(count)
	count += 2




print("\n")






# 3) ==========Controlling Loops===============(Python provides two keywords (break & continue) to control loops)
for r in range(18):
	if r == 10:
		break
	print(r);



print("\n")



for rg in range(10):
	if rg == 4:
		continue
	print(rg);





print("\n")






# 4) ============Nested Loops===============
for tab in range(1,4):
	print(tab)
	for tabs in range(1,11):
		print(f"{tab} x {tabs} = {tab * tabs}")
