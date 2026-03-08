import secrets
import string

def generate_password(length, upper, lower, numbers, symbols, exclude):

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*()_+-=[]{}|;:,.<>?"

    ambiguous = "O0lI1"

    if exclude:
        uppercase = ''.join(c for c in uppercase if c not in ambiguous)
        lowercase = ''.join(c for c in lowercase if c not in ambiguous)
        digits = ''.join(c for c in digits if c not in ambiguous)

    pool = ""
    password = []

    if upper:
        pool += uppercase
        password.append(secrets.choice(uppercase))

    if lower:
        pool += lowercase
        password.append(secrets.choice(lowercase))

    if numbers:
        pool += digits
        password.append(secrets.choice(digits))

    if symbols:
        pool += special
        password.append(secrets.choice(special))

    for _ in range(length - len(password)):
        password.append(secrets.choice(pool))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def check_strength(password):

    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(c.isupper() for c in password):
        score += 1

    if any(c.islower() for c in password):
        score += 1

    if any(c.isdigit() for c in password):
        score += 1

    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"
