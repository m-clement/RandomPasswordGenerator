import string
import random

characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    password_length = int(input("Enter your desired password length: "))

    random.shuffle(characters)

    password = []
    
    for i in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)

option = input("Would you like  to generate a password? (y/n): ")

if option == "y":
    generate_password()
elif option == "n":
    print("Understandable, have a nice day")
    quit()
else:
    print("Invalid input. Please try again.")