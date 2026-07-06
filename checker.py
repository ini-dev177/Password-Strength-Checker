import re
import math
import string


COMMON_PASSWORDS = {
    "123456",
    "password",
    "123456789",
    "12345678",
    "qwerty",
    "abc123",
    "111111",
    "123123",
    "admin",
    "letmein",
    "welcome",
    "iloveyou",
    "password123",
}


def calculate_entropy(password: str) -> float:
    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0 or len(password) == 0:
        return 0.0

    return round(len(password) * math.log2(pool_size), 2)


def get_feedback(password: str) -> list:
    feedback = []

    if len(password) < 8:
        feedback.append("Password is too short. Use at least 8 characters.")
    if not any(c.islower() for c in password):
        feedback.append("Add at least one lowercase letter.")
    if not any(c.isupper() for c in password):
        feedback.append("Add at least one uppercase letter.")
    if not any(c.isdigit() for c in password):
        feedback.append("Add at least one digit.")
    if not any(c in string.punctuation for c in password):
        feedback.append("Add at least one special character.")
    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common and easy to guess.")
    if re.search(r"(.)\1\1", password):
        feedback.append("Avoid repeated characters like 'aaa' or '111'.")
    if re.search(r"(123|abc|qwerty)", password.lower()):
        feedback.append("Avoid predictable patterns like '123', 'abc', or 'qwerty'.")

    return feedback


def score_password(password: str) -> tuple:
    score = 0

    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if password.lower() in COMMON_PASSWORDS:
        score -= 2
    if re.search(r"(.)\1\1", password):
        score -= 1
    if re.search(r"(123|abc|qwerty)", password.lower()):
        score -= 1

    score = max(0, min(score, 6))

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength


def check_password_strength(password: str) -> dict:
    score, strength = score_password(password)
    entropy = calculate_entropy(password)
    feedback = get_feedback(password)

    return {
        "password": password,
        "length": len(password),
        "score": score,
        "strength": strength,
        "entropy_bits": entropy,
        "feedback": feedback if feedback else ["Good password. No major issues found."],
    }
