# 1) ==========Set(Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage)========
# The set is :
# a Unordered
# b Unindexed
# c Unchangable
# Set are mutable


num_set_01 : set = {20,40,60,80}
num_set_02 :set = {100,300,600,900,1000}

print(f"Set_01 : {num_set_01}")
print(f"Set_02 : {num_set_02}")
print("Type of set :" , type(num_set_01) , type(num_set_02))
print(f"Set_01 is equalto Set_02: {num_set_01 == num_set_02}") # Output False
print("\n")






# It can hold multiple data types at once
multi_data_types : set = {1.2 , "Goudling" , False , 100 , ("Iphone" , "Android") , True}
print(f"Set can hold multi data types : {multi_data_types}")
print("\n")






# The set is unordered
sets : set = {"Web Designing" , "Graphics Designing" , "App Development" , "Digital Marketing"}
print(f"Set is unordered : {sets}")
print("\n")






# Add or Remove Method In Set(you can use the  remove() methods to remove items and the add() methods to add new item)
remove_items : set = {"MNO" , "PQR" , "ABC"}
print(f"Before Remove Items : {remove_items}")
remove_items.remove("MNO")
print(f"After Remove Items : {remove_items}")
print("\n")


add_items : set = {20 , 90 , 100 , "Zehan" , "Zimal" , True , 12.0}
print(f"Before Add Items : {add_items}")
add_items.add(False)
print(f"After Add Items : {add_items}")
print("\n")




# Use difference_update() method to remove multiple element at once
Fruits : set = {"Orange" , "Pineapple" , "Grapes" , "Mango" , "Banana" , "Cherry"}
print(f"Before Fruits : {Fruits}")
Fruits.difference_update({"Mango", "Pineapple"})
print(f"After Fruits : {Fruits}")
Fruits.update({"Peach"})
print(f"Updated Fruits List : {Fruits}")
print("\n")





# Using the union() method
myset_01 : set = {1,2,3,5,4,9}
myset_02: set = {1 ,1,8,2,10}
print(f"Before : {myset_01, myset_02}")
res = myset_01.union(myset_02)
print(f"After using union : {res}")
print("\n")




# Using the | operato Method
myset_01 : set = {1,2,3,5,4,9}
myset_02: set = {1 ,1,8,2,10}
print(f"Before : {myset_01, myset_02}")
an_res = myset_02 | myset_01
print(f"After using | : {an_res}")
print("\n")









# 2) ==========Frozenset(Immutable cannot be modified after creation)===========
# set: Supports methods like add(), remove(), discard(), clear(), pop(), update()
# frozenset: Does not support any modification methods
greet : frozenset = ("Hi" , "Hello" , "Hey")
print(greet)

message : frozenset = frozenset([12,11,10,9])
print(message)
print("\n")









# ====================Set Methods========================
myset : set = {"Hello World!" , "Hello Python" , "Hello TypeScript"}
another_set : set = {22, 1, 19 , "Hello World!" , "Next.js"}
print(f"Set Method : {myset}")
myset.add("Hello Next.js") # Add a new  item in a set of list
print(f"Set Add Method : {myset}") 
myset.remove("Hello World!") # Remove an item in a set of list
print(f"Set Remove Method : {myset}")
print(f"Greetings : {myset}")
myset.difference_update(["Hello TypeScript" , "Hello Python"]) # Remove mutliple items in a set of list
print(f"Set Difference Update Method : {myset}")
uni = myset.union(another_set) # Merge an item in a multiple set of list
print(f"Union Method : {uni}")
resp = myset|another_set
print(f"| Method : {resp}") # Merge an item in a multiple set of list
print("\n")





str_set : set  = {"A" , "B" , "C" }
mix_set : set = {11,21,91,"A" , "E"}
verb = str_set.symmetric_difference(mix_set) # Return a set that contains only unique items from both sets
print(f"Symmetric Difference Method : {verb}")
print("\n")





sub_set : set = {12.22 , 91 , 100 , 200}
sup_set : set = {100 , 300 , 410 , 12,22 , 91}
xyz = sub_set.issubset(sup_set) # Return True if all items in set x are present in set y
print(f"IsSubset : {xyz}")
print("\n")





pqr_01 : set = {20 , 11 , 10 , 100 } 
pqr_02 : set = {10 , 100 , 20 , 11}
mno = pqr_01.issuperset(pqr_02) # Return True if all items in set x are present in set y
print(f"IsSuperset : {mno}")
print("\n")




pqr : set = {10 , 20 , 30} 
response = pqr.pop()
print(f"Pop Method : {response}")