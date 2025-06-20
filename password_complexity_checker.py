import re

def check_strength(password):
    length_ok = len(password) >= 8
    upper_ok = re.search(r"[A-Z]", password) is not None
    lower_ok = re.search(r"[a-z]", password) is not None
    digit_ok = re.search(r"\d", password) is not None
    special_ok = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None

    score = sum([length_ok, upper_ok, lower_ok, digit_ok, special_ok])
    feedback = []

    if not length_ok:
        feedback.append("Password should be at least 8 characters long.")
    if not upper_ok:
        feedback.append("Include at least one uppercase letter.")
    if not lower_ok:
        feedback.append("Include at least one lowercase letter.")
    if not digit_ok:
        feedback.append("Include at least one digit.")
    if not special_ok:
        feedback.append("Include at least one special character (!@#$%^&* etc).")

    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    return strength_levels[score], feedback

def main():
    print("Password Strength Checker")
    print("=========================")
    password = input("Enter your password: ")

    strength, messages = check_strength(password)
    print(f"\nStrength: {strength}")
    if messages:
        print("Feedback:")
        for msg in messages:
            print(" -", msg)

if __name__ == "__main__":
    main()
