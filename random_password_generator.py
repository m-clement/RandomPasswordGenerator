import string
import random

# Combine ASCII letters, digits, and punctuation to form the character set for password generation
characters = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password():
    """Generate a random password based on user's desired length."""
    # Get the desired password length from the user
    password_length = int(input("Enter your desired password length: "))

    # Shuffle the characters for randomness
    random.shuffle(characters)

    # Construct the password using random characters
    password = [random.choice(characters) for _ in range(password_length)]

    # Shuffle the password again to ensure randomness
    random.shuffle(password)

    # Convert the password list to a string and display it
    print("".join(password))

# Prompt the user to decide if they want to generate a password
option = input("Would you like to generate a password? (y/n): ")

if option == "y":
    generate_password()
elif option == "n":
    print("Understandable, have a nice day")
    quit()
else:
    print("Invalid input. Please try again.")
