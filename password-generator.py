# Password Generator Project
import random  # noqa: F401
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',  # noqa: E501
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']  # noqa: E501
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))  # noqa: F541
nr_numbers = int(input(f"How many numbers would you like?\n"))  # noqa: F541

password_list = []
for letter in range(1, nr_letters + 1):
    password_list += random.choice(letters)

for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
password = ""
for char in password_list:
    password += char

print(password)

