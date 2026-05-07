def generate_suggestions(password):

    tips = []

    if len(password) < 12:
        tips.append("Increase password length to at least 12 characters")

    if not any(c.isupper() for c in password):
        tips.append("Add uppercase letters")

    if not any(c.isdigit() for c in password):
        tips.append("Include numbers")

    if not any(not c.isalnum() for c in password):
        tips.append("Add special characters")

    return tips

