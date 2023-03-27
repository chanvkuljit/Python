"""Write a program to generate random password which shall combine upper case alphabets, 
lower case alphabets,  digits and special characters. 
You shall prepare separate dictionary items called “lower”, “upper”, “digits”, “special” 
and values shall be stored accordingly. 
From this array, based on the user’s choice random password shall be generated. 
You shall make sure that atleast one character is selected from all specified choices.
Use dictionary / list as applicable"""

import random

# Define the character sets
char_sets = {
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "special": "!@#$%^&*()_+-={}[];\',./<>?:\"|"
}

# Prompt the user for password length
length = int(input("Enter password length: "))

"""# Ensure that the password length is at least 4 characters
if length < 4:
    print("Password length must be at least 4")
    exit()"""

# Generate the password
password = ""

# Choose one character from each set
for char_set in char_sets.values():
    password += random.choice(char_set)

# Choose remaining characters randomly
for i in range(length - 4):
    choice = random.choice(list(char_sets.values()))
    password += random.choice(choice)

# Shuffle the characters in the password
password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)

# Print the password
print("Your random password is:", password)
