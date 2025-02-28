# =============================PYTHON DATA TYPES==========================


# 1) =========SEQUENCE TYPE=============
# a) String(str)
# It's single quotation str
FullName : str = 'John Peter';
print("FullName:" , FullName);

# It's double quotation str
FatherName : str = "Peter";
print("FatherName :" , FatherName);

# It's triple quotation str
MotherName : str = """Janifer Peter""";
print("MotherName :" , MotherName);


# b) ===========List(list)=============
GIAIC_STUDENTSNAME : list[str] = ["Muzna","Zimal","Deeba","Iqra","Maila","Laiba"];
print("GIAIC_STUDENTSNAME List :" , GIAIC_STUDENTSNAME);

# c) ===========Tuple(tuple)=============
a : tuple = ("Zaviyar",19,True);
print("Tuple  Data :" , a);
print(type(a));





# 2)==============NUMERIC TYPE================
# a) =========Integer(int)==========
a : int = 9;
b: int = 21;
c  = a+b;
print("Addition:" , a+b);

# b) ===========Float(float)=============
a : float = 20.1;
b : float = .11;
print("Numbers with decimal points :" , a);
print("Numbers with decimal points :" , b);

# c) ===========Complex(complex)=============
num : complex = 9 + 2j;
print("Numbers with a real and imaginary part:" , num);








# 3) =========BOOLEAN(bool)===========
y : bool = False;
print("Represents False:", y);
z : bool = True;
print("Represents True:" , z);







# 4) =========SET(set)===========

set_01 : set = {10,30,90}
print("Mutable unordered and contains unique values:" , set_01);

set_02 : set = {1,2,3,7,8,7,9,10}
print("Mutable unordered and contains unique values" , set_02);





# 5) =========FROZENSET(frozenset)===========

abc = frozenset(["a" , "b" , "m"]);
print("Immutable version of a set:" , abc);
print(type(abc));




# 6) =========DICTIONARY(dict)===========
StudentData : dict = {"Name" : "Anam" , "Age" :27 , "Gender" : "Female"}
print("Dictionary (dict) Stores key-value pairs:" , StudentData);
print(type(StudentData));

