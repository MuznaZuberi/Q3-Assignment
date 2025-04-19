
# =========File Handling in Python============
# File handling is essential for reading and writing data to files, enabling persistent storage. Python provides built-in functions and methods to handle files efficiently

print("*********Read Mode File*********")
try:
		file = open("mine_skills.txt", "r")
		res = file.read()
		print(res)
		file.close()

except FileNotFoundError:
    print("File not found")

except Exception as e:
	print("An error occured!" , e)
print("\n")









print("*********Readline Mode File*********")
try:
    xyz = open("mine_skills.txt", "r")
    response_01 = xyz.readlines()
    print(response_01)     
    xyz.close()

except FileNotFoundError:
    print("File Not Found")

except Exception as e:
    print("An Error Occured")

print("\n")





print("*********Readlines(): Reads all lines into a list***********")
try:
	xyz = open("mine_skills.txt" , "r")
	for line in xyz:
		print(line)
	xyz.close()

except FileNotFoundError:
	print("File Not Found")

except Exception as e:
	print("An Error Occured" , e)
print("\n")





print("*********Write Mode File*********")
try:
	doc = open("file_doc.txt" , "w")
	doc.write(" Hello Pyhton!.Python is an interpreted programming language")
	print(doc)
	doc.close()

except FileNotFoundError:
	print("File Not Found!")

except Exception as e:
	print("An Error Occured!")
print("\n")



print("*********Writelines Mode File*********")
try:
    mno = open("cities.txt", "w")
    cities = ["Karachi\n", "Lahore\n", "Islamabad\n" , "Multan\n" , "Peshawar"]
    mno.writelines(cities)
    print("Data written successfully.")
    mno.close()

except FileNotFoundError:
    print("File Not Found!")

except Exception as e:
    print("An Error Occured!", e)
print("\n")



print("************Append a new line Methods************")
try:
	with open("users.txt" , "a") as usernames:
		yen = usernames.write("Jackline \n" + "Muzna")
		print(yen)
except FileNotFoundError:
	print("FileNotFoundError!")
except Exception as e:
	print("An Error Occurred!")
print("\n")




print("*********Seek Mode File*********")
try:
	abc = open("countries.txt", "r")
	res_01 = abc.read()
	print(res_01)

	abc.seek(0) 

	res_02 = abc.read()
	print(res_02)

	abc.seek(0) 

	res_03 = abc.read()
	print(res_03)
	abc.close()

except FileNotFoundError:
	print("File Not Found")

except Exception as e:
	print("An Error Occurred!", e)
print("\n")



print("*********strip() removes leading/trailing whitespace**********")
try:
	looping = open("mine_skills.txt" , "r")
	for x in looping:
		print(x.strip())

except FileNotFoundError:
	print("FileNotFoundError!")
except Exception as e:
	print("An Error Occurred!")
print("\n")




print("************Best Practices:(Use 'with' for automatic cleanup)************")
try:
	with open("cities.txt" , "x") as file:
		print("successfully installed")
except Exception as e:
	print("file already exists!")
print("\n")




try:
	with open("file_doc.txt" , "r") as file:
		content = file.read()
		print(content)
		file.close()
except FileNotFoundError:
	print("FileNotFoundError!")
except Exception as e:
	print("An Error Occured!")




