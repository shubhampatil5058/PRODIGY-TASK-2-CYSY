import string
def check_password_strength(password):
    length_criteria = 8 
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True
    
    length_ok = len(password) >= length_criteria
    has_upper_lower = has_upper and has_lower
    has_digit_special = has_digit and has_special
    
    if length_ok and has_upper_lower and has_digit_special:
        return "Strong password"
    elif length_ok and has_upper_lower:
        return "Moderate password"
    else:
        return "Weak password"

while True:
    password = input("Enter your password (or type 'exit' to quit): ")
    
    if password.lower() == 'exit':
        break
    
    strength = check_password_strength(password)
    print(f"Password strength: {strength}")
