import random

# Lists of characters
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Taking input from user
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Start with an empty password string
password = ""

# Add letters
for i in range(nr_letters):
    password += random.choice(letters)

# Add symbols
for i in range(nr_symbols):
    password += random.choice(symbols)

# Add numbers
for i in range(nr_numbers):
    password += random.choice(numbers)

print(f"Your password (easy level): {password}")

# Hard level: Shuffle the password
password_list = list(password)
random.shuffle(password_list)
hard_password = "".join(password_list)

print(f"Your final (shuffled) password: {hard_password}")
