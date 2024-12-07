import random
import string

def generate_password(length):
    if length < 4:  # Ensure the password can include all character types
        raise ValueError("Password length must be at least 4.")

    # Define character pools
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digits = random.choice(string.digits)
    special_chars = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")

    # Ensure the password includes at least one of each type
    initial_password = uppercase + lowercase + digits + special_chars

    # Fill the remaining length with random characters from all pools
    all_characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    remaining_password = "".join(random.choices(all_characters, k=length - 4))

    # Combine and shuffle to randomize the order
    password = list(initial_password + remaining_password)
    random.shuffle(password)

    return "".join(password)

# Example usage
print(generate_password(12))  # Generate a 12-character random password
