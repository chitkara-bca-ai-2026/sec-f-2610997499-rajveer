

username = input("Enter your username: ")
password = input("Enter your password: ")

long_enough = len(password) >= 8
has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)

print("PASSWORD VALIDATION REPORT")
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

print()

print("---Validation Rules---")
print(f"[{'PASS' if long_enough else 'FAIL'}] Minimum 8 characters ({len(password)} characters)")
print(f"[{'PASS' if has_digit else 'FAIL'}] At least one digit")
print(f"[{'PASS' if has_upper else 'FAIL'}] At least one uppercase letter")

print()

print("---Result---")

if long_enough and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID")
