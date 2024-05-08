import random
import string


def generate_password(length, uppercase=True, lowercase=True, digits=True, symbols=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("At least one character type must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


length = int(input("Enter the length of the password: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

try:
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    print("Generated Password:", password)
except ValueError as e:
    print(e)