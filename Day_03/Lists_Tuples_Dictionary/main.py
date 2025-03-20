# 1) ===============Lists in Python(Python provides powerful sequence types: lists and tuples. These data structures help store and manage collections of data efficiently)===============

# a) Creating  lists with different data types
GIAIC_Students_Name = ["John" , "Elon" , "Ellie" , "Janifer" , "Nick"]
print(f"GIAIC_Students_List: {GIAIC_Students_Name}")

Mutli_Type_List = [21 , "Twitter" , "Github" , True , 9100 , "Facebook"]
print(f"Mutli_Type_List: {Mutli_Type_List}")

ID_CARD_no = [2911 , 9811 , 3882 , 8771]
print(f"ID: {ID_CARD_no}")
print("\n")




# b) Accessing List Elements(You can access elements using indexing (starting from 0) and negative indexing (starting from -1))
Fruits : str = ["Orange" , "Pineapple" , "Mango" , "Banana" , "Grapes" , "Peach" , "Strawberry"]
print(Fruits)
print(Fruits[3]) # Output Banana
print(Fruits[-6]) # Output Pineapple
print("\n")




# c) Modifying Lists(Lists are mutable, meaning their elements can be changed)
fruits: str = ["Mango" , "Banana" , "Grapes" , "Peach"]
print(f"Before Modifying Fruits_list:{fruits}")
fruits[2] = "Cherry" # replacing Grapes with Cherry
print(f"After Modifying Fruits_list:{fruits}")
print("\n")




# d) List Slicing(Extract multiple elements using slicing)
Users_name : str = ["Zayn" , "Zehan" , "Zimal" , "Izma"]
print(f"Facebook Users Name{Users_name}")
print(Users_name[0:2]) # Output ["Zayn" , "Zehan"]
print("\n")




# e) Common List Methods(Appending and Extending Lists)
# Using Append Method 
Guest_list : str = ["Sundus" , "Izma" , "Erha"]
print(f"Before Guest_list:{Guest_list}")
Guest_list.append("Alaya") # Adds a single element "Alaya" to the end
print(f"After Guest_list:{Guest_list}")


# Using Entend Method
Guest_list : str = ["Sundus" , "Izma" , "Erha"]
print(f"Before Guest_list:{Guest_list}")
Guest_list.extend(["Alaya" , "Ushba" , "Zarnab", "Manahil"])  # Adds multiple elements
print(f"After Guest_list:{Guest_list}")
print("\n")





# f) Removing Elements(In Python, remove() and pop() are two distinct methods used to manipulate lists. While they may seem similar, they have different purposes and behaviors)
# The remove() method does not return any value
Guest_list : str = ["Sundus" , "Izma" , "Erha"]
print(f"Before Guest_list:{Guest_list}")
Guest_list.remove("Erha") # Removes 'Erha' # run multiple times to see error as "Erha" is already removed
print(f"After Remove Guest_list:{Guest_list}")



# Pop Method(The pop() method is used to delete an item at a specified index from a list. If no index is provided, it removes and returns the last item in the list)
# The pop() method returns the item that was removed from the list
Guest_list : str = ["Sundus" , "Izma" , "Erha"]
print(f"Before Guest_list:{Guest_list}")
deleted = Guest_list.pop(1)
print(deleted)
print(f"After Pop Guest_list:{Guest_list}")
print("\n")




# g) Sorting a List
# 1. Sorting (Ascending Order "smaller to greater")
numbers : int = [9 , 7 , 299 , 100 , 81 , 2 , 1 , 0 , 76]
print(f"Unsorted Numbers list:{numbers}")
numbers.sort()
print(f"Sorted Ascending Order Numbers List:{numbers}")
print("\n")

# 2. Sorting (Descending Order "greater to smaller")
numbers : int = [9 , 7 , 299 , 100 , 81 , 2 , 1 , 0 , 76]
print(f"Unsorted Numbers List:{numbers}")
numbers.sort(reverse = True)
print(f"Sorted Descending Order Numbers List:{numbers}")
print("\n")

# 3. Sorting by String Length
courses :str = ["Web Designing" , "Graphic Designing" , "SEO"]
print(f"Before:{courses}")
courses.sort(key = len)
print(f"After{courses}")
print("\n")

# 4. Sorting by Last Character 
animals : str = ["Elephant" , "Lion" , "Zebra"]
print(f"Before:{animals}")
animals.sort(key=lambda  word:word[-1])
print(f"After{animals}")
print("\n")

# 5. Reverse Sorting
alphabets : str = ["A" , "B" , "C"]
print(f"Before Reverse{alphabets}")
alphabets.reverse()
print(f"After Reverse{alphabets}")
print("\n")




# h) Using list comprehension

# Without if condition
cube: list = [x**3 for x in [1, 2, 3, 4, 5] ] #  if x > 3 place this if condition and see
print(cube, " : ", type(cube))  # Output: [1, 8, 27, 64, 125]

# With if condition
cube: list = [x**3 for x in [1, 2, 3, 4, 5] if x>4 ] #  if x > 4 place this if condition and see
print(cube, " : ", type(cube))  # Output: [1, 8, 27, 64, 125]

# With another if condition
cube: list = [x**3 for x in [1, 2, 3, 4, 5] if x>6 ] #  if x > 6 place this if condition and see
print(cube)  # Output: []
print("\n")













# 2) =========Tuples in Python(In Python, a tuple is an immutable data type. This means that once a tuple is created, its elements cannot be changed, added, or removed)=========
tuple_01 : tuple = tuple(["Toyota", "Benz" , "Carolla"])
print(f"List Of Cars: {tuple_01}")
# tuple_01[2] = "Civi" # TypeError: 'tuple' object does not support item assignment 
print("\n")


grade_list_01 : tuple = ["A", "B" , "C"]
grade_list_02 :tuple= ["D" , "E" , "F"]
print(f"Grade A to C: {id(grade_list_01)}") # Unique ID
print(f"Grade D to F: {id(grade_list_02)}") # Unique ID
print(grade_list_01 == grade_list_02) # Output False
print(grade_list_02 != grade_list_01) # Output True
print("\n")


# Applying Tuple Data Type With Multiple Methoods In 'Python'
multi_tuple_types : tuple = (21 , True , "Jack" , 29.99 , 12.99)
print(f"Tuple Mutli Data Types: {multi_tuple_types}")
print(f"Tuple Access Element: {multi_tuple_types[2]}")
print(f"Tuple Slicing: {multi_tuple_types[1:4]}")
print(f"Tuple Length: {len(multi_tuple_types)}")
print(f"Is True In Multi Tuple Types?: {'Jack' in multi_tuple_types}")
concatination = multi_tuple_types + tuple_01
print(f"Concatinate: {concatination}")
repeated = tuple_01*2
print(f"Repeating Tuple: {repeated}")
print(f"Nested Tuple : {multi_tuple_types , tuple_01}")
print("\n")















# 3) ==========Dictionaries in Python(A dictionary is a collection of key-value pairs)============
# # Create a dictionary to store a person's details
student_data : dict = {
	"Name" : "Peter",
	"Age" : 21,
	"Gender" : "Male",
    "Qualification" : "Master's",
    "Nationality" : "UAE",
    "Email" : "muznazuberi@gmail.com",
}

print(student_data)
print("\n")



# Accessing Values (with the help if .(dot notation) , [](square bracket notation))
print(f"Student Age : {student_data.get('Age')}")
print(f"Student Name : {student_data['Name']}")
print("\n")



# Modifying a Dictionary
student_data["Email"] = "muznazubairi123@gamil.com"
print(f"Modifying StudentData : {student_data}")
print("\n")



# Deleting Items
del student_data["Age"]
print(f"Student Data After Deleting The Key Of Age : {student_data}")
print("\n")



# Iterating Over a Dictionary
for key, value in student_data.items():
	print(key , ":" , value)
print("\n")




# Testing If Else Statement
names : str = input("Enter Your Name:")
if names == student_data["Name"]:
	print(f"Hi! My name is : {student_data['Name']}")
else:
	print("Invalid!")
print("\n")




#  Nested Dictionaries
fb_user_data : dict = {
	"user_name" : "Kellin",
	"user_password" : 29881,
	"more_info" : {"user_age" : 29 , "user_email": "kell@yahooo.com"}
}
print(fb_user_data)
print(fb_user_data["more_info"])
print(fb_user_data["more_info"]["user_age"])
