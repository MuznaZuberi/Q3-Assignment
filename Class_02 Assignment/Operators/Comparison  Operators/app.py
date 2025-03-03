#  Comparison Operators

# 	Equal ==
a : str = "abc";
b : str = "abc";
c  = a ==b;
print("This result is:" , c); # Output: True, cuz because both values are the same



# 	Not Equal !=
a : str = "abc";
b : str = "abc";
c  = a !=b;
print("This result is:" , c); # Output: False, cuz because both values are the same



# 	Less than <
a : int = 31;
b : int = 11;
c  = a < b;
print("This result is:" , c);# Output: False, because `a` is greater than `b`



# 	Greater than >
a : int = 10;
b : int = 3;
c  = a > b;
print("This result is:" , c);# Output: True, because `a` is greater than `b`



# 	Greaterthan Equal >=
a : int = 10;
b : int = 30;
c  = b >= a; # Checking if `b` is greater than or equal to `a`
print("This result is:" , c); # Output: True, because `b` is greater than `a`



# 	Lessthan Equal <=
a : int = 2;
b : int = 2;
c  = a <= b ; # Checking if `a` is less than or equal to `b`
print("This result is:" , c); #Output: True, because `a` is equal to `b`