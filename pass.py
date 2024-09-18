import random
import string

def generate_password(length=12, include_uppercase=True, include_lowercase=True, 
                      include_numbers=True, include_symbols=True):
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be included")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the length of the password: "))
        include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        password = generate_password(length, include_uppercase, include_lowercase, 
                                     include_numbers, include_symbols)
        print("Generated Password:", password)
    except ValueError as e:
        print("Error:", e)
