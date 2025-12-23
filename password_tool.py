import re

def check_password_strength(password):
    length_error = len(password) < 8
    searches = {
        "digit": re.search(r"\d", password) is None,
        "uppercase": re.search(r"[A-Z]", password) is None,
        "lowercase": re.search(r"[a-z]", password) is None,
        "symbol": re.search(r"\W", password) is None
    }
    
    # Logic to calculate score
    score = 0
    feedback = []
    
    if length_error:
        feedback.append("❌ Password is too short (min 8 chars)")
    else:
        score += 1
        
    if searches["digit"]:
        feedback.append("❌ Missing numbers")
    else:
        score += 1
        
    if searches["uppercase"]:
        feedback.append("❌ Missing uppercase letters")
    else:
        score += 1
        
    if searches["lowercase"]:
        feedback.append("❌ Missing lowercase letters")
    else:
        score += 1
        
    if searches["symbol"]:
        feedback.append("❌ Missing special characters (@, #, $, etc.)")
    else:
        score += 1

    # Determine Strength Level
    print("\n--- PASSWORD ANALYSIS ---")
    if score == 5:
        print("Strength: ✅ STRONG")
    elif score >= 3:
        print("Strength: ⚠️ MEDIUM")
    else:
        print("Strength: ❌ WEAK")
        
    # Print suggestions if any
    if feedback:
        print("\nSuggestions to improve:")
        for item in feedback:
            print(item)

def main():
    print("--- Password Complexity Checker ---")
    while True:
        pwd = input("\nEnter a password to check (or 'q' to quit): ")
        if pwd.lower() == 'q':
            break
        check_password_strength(pwd)

if __name__ == "__main__":
    main()