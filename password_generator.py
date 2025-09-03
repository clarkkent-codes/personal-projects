#First version using string library
import string
import secrets

def password_generator(password_length):
    password = ''

    letter = string.ascii_letters
    numbers = string.digits
    special_characters = string.punctuation
    alphabet = letter + numbers + special_characters

    for char in range(password_length):
        password += "".join(secrets.choice(alphabet))

    print("Passwrod:", password)


password_length = int(input("Enter password length: "))

password_generator(password_length)

#Second version using user defined characters
import secrets

def password_generator(password_length):
    password = ''

    character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~"

    for char in range(password_length):
        password += ''.join(secrets.choice(character_string))

    print("Password:",password)


password_length = int(input("Enter password length: "))

password_generator(password_length)