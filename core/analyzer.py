import re

def check_password_strength(password):
    feedback = []
    is_strong = True

    if len(password) < 8:
        feedback.append("Password is too short (minimum 8 characters required).")
        is_strong = False

    if not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        feedback.append("Missing a combination of uppercase and lowercase letters.")
        is_strong = False

    if re.search(r"\d", password):
        if len(re.findall(r"\d", password)) > len(password) * 0.7:
            feedback.append("High density of numbers makes the password easily predictable.")
            is_strong = False
    else:
        feedback.append("Does not contain any numbers.")
        is_strong = False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        feedback.append("Missing special characters.")
        is_strong = False

    return is_strong, feedback
