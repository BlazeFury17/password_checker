import re

def check_password_strength(password):
    feedback = []
    strength_points = 0

    # Check length
    if len(password) >= 8:
        feedback.append("✔️ Length is 8 or more characters")
        strength_points += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long")

    # Check lowercase letters
    if re.search(r'[a-z]', password):
        feedback.append("✔️ Contains lowercase letter(s)")
        strength_points += 1
    else:
        feedback.append("❌ Should include lowercase letters")

    # Check uppercase letters
    if re.search(r'[A-Z]', password):
        feedback.append("✔️ Contains uppercase letter(s)")
        strength_points += 1
    else:
        feedback.append("❌ Should include uppercase letters")

    # Check numbers
    if re.search(r'[0-9]', password):
        feedback.append("✔️ Contains number(s)")
        strength_points += 1
    else:
        feedback.append("❌ Should include numbers")

    # Check special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("✔️ Contains special character(s)")
        strength_points += 1
    else:
        feedback.append("❌ Should include special characters (!@#$%^&* etc)")

    # Final strength
    if strength_points <= 2:
        strength = "Weak ❌"
    elif strength_points == 3 or strength_points == 4:
        strength = "Moderate ⚠️"
    else:
        strength = "Strong ✅"

    return strength, feedback


# --- MAIN EXECUTION ---
if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    password = input("Enter your password: ")
    strength, feedback_list = check_password_strength(password)

    print("\n📋 Feedback:")
    for item in feedback_list:
        print(" -", item)

    print(f"\n🛡️ Password Strength: {strength}")
