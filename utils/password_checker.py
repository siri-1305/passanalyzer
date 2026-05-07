import re

def analyze_password(password):

    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters")

    if re.search("[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters")

    if re.search("[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters")

    if re.search("[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers")

    if re.search("[@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Add special characters")

    if score <=2:
        strength="Weak"
    elif score<=4:
        strength="Medium"
    else:
        strength="Strong"

    return {

        "score":score,
        "strength":strength,
        "suggestions":suggestions

    }

