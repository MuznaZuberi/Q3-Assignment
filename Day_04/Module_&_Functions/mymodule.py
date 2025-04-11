from main import user_data , personal_details
user_data("Muzna" , "Female" , 24)
print(personal_details)
print(f"User Name: {personal_details.get('name')}") # data access using '.' notation
print(f"User Nationality: {personal_details['nationality']}") # data access using '[]' squarebracket notation
