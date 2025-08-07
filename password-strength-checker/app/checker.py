import re

def evaluate_password(password):
    score = 0
    issues = []

    if len(password) >= 8:
        score += 1
    else:
        issues.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        issues.append("Password should include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        issues.append("Password should include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        issues.append("Password should include at least one number.")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]", password):
        score += 1
    else:
        issues.append("Password should include at least one special character.")

    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Unacceptable"
    }.get(score, "Unknown")

    return score, strength, issues