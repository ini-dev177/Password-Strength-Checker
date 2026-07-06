import random
import string


def generate_password(length: int = 12) -> str:
    if length < 8:
        raise ValueError("Password length should be at least 8.")

    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    remaining_length = length - 4
    all_characters = string.ascii_letters + string.digits + string.punctuation

    password_list = [lowercase, uppercase, digit, special]
    password_list += random.choices(all_characters, k=remaining_length)

    random.shuffle(password_list)
    return "".join(password_list)
