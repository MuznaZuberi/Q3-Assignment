#  Identity Operators


Students_name : list[str] = ["Anam" , "Zimal" , "Abresh" , "Sundus"];
print(Students_name[0] == "Sundus"); # Output False
print(Students_name[-1] == "Sundus"); # Output True


num_01 : list[int] = [10,20,30,80];
num_02 : list[int] = [20,10,70,80];
print(num_01 is num_02); # Output False


Fruit_01 : list[str] = ["Apple" , "Mango" , "Grapes"];
Fruit_02 : list[str] = ["Apple" , "Mango" , "Grapes"];
print(Fruit_01 is not Fruit_02);
print("\n---------\n");
print(f"Fruit_01 ID:" , id(Fruit_01));
print(f"Fruit_02 ID:" , id(Fruit_02));

