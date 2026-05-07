import re
from entropy_calculator import calculate_entropy

def analyze_password(password):

    score = 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*()]", password):
        score += 1

    entropy = calculate_entropy(password)

    if entropy > 60:
        score += 2

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    elif score <= 6:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return {
        "score": score,
        "entropy": round(entropy,2),
        "strength": strength
    }

