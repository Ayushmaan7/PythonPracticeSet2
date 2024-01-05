import random
import string

def generate_random_password(length=12):
    # Define the character sets for letters, numbers, and symbols
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # Combine the character sets
    all_characters = letters + numbers + symbols

    # Generate a random password by sampling from the combined characters
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    # Example usage: generate a random password of length 12
    generated_password = generate_random_password()
    print(f"Generated Password: {generated_password}")
