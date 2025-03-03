# Logical Operators


# Logical AND
y : int = 21;
z : int = 22;
res_01 = (y < z and z > y); # `y < z` is True (21 < 22) and `z > y` is also True (22 > 21), so the result will be True.
res_02 = (y >= z and z <= y); # `y >= z` is False (21 >= 22 is False) and `z <= y` is also False (22 <= 21 is False).
# Since both conditions are False, the AND operator returns False.
print("The result is : " , res_01);
print("The result is :" , res_02);




# Logical OR
user_name : str = "John";
user_age : int = 22;
result_03 = (user_name == "Johns" or user_age == 22);
print("The result is:" , result_03);




# Logical NOT
a :int = 19;
b : int = 200;
c = not (a < b); # Since 19 > 200 is False, `not False` becomes True
print("The result is:" , c);

