# =============================PYTHON SPECIAL KEYWORDS==========================


# 1)  Control Flow Keywords(if, elif, else , for, while, break, continue, pass)


# a) if, elif, else Statement
username : str = "Zaviyar Khan";
if username == "Hassan":
	print("Hello Myself:" , username);

elif username == "Zaid Khan":
	print("Hello Myself:" , username);

elif username == "Saim Khan":
	print("Hello Myself:" , username);


elif username == "Zaviyar Khan":
	print("Hi! Myself:" , username);

elif username == "Arbaz Khan":
	print("Hello Myself:" , username);

else:
	print("Opzzzzzzzzzzz Invalid username!");







# b) Loop(for loop)
Courses : list[str] = ["HTML" , "CSS" , "TYPESCRIPT", "JAVASCRIPT" , "REACT.JS" , "TAILWINDCSS" , "NEXT.JS"];
for c in Courses:
	print("✅ All our courses are fully accessible and available for enrollment" , c);










# c) WhileLoop (while loop)  
PinCode : int = 9100;
Attempt : int = 2;

while Attempt:
    if int(input("Enter Your 4 digit pincode:")) == PinCode:
        print("✅Attempt Granted!");
        break

    Attempt -= 1
    print(f"❌ Wrong PIN! {Attempt} attempts left.");

else:
    print("🔒 Your account is locked!");









# d) Break (break)  
products = ["Laptop", "Mobile", "Tablet", "Headphones"]

for item in products:
    if item == "Headphones":
        print(f"{item} found in stock!")
        break
else:
    print("Product not found.");








# e) Continue (continue)  
Fruits : list[str] = ["Apple" , "Mango" , "Banana" , "Orange" , "Grapes" , "Cheery" , "Strwaberry"];

for f in Fruits:
    if f == ["Mango" , "Cheery"]:
        continue
    print(f"Fruits in Stock{f}");








# f) Pass (pass)  
def UpcomingFeature():
    pass 
print("🚀 New feature is under development. Stay tuned!")
