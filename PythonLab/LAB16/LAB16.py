
history = []


def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b==0:
        return "ERROR"
    return a / b

def modulus(a,b):
    if b==0:
        return "ERROR"
    return a % b

def power(base, exp=2):
    return base**exp

def get_numbers():
    a, b = input("Enter two numbers: ").split()
    return float(a), float(b)

while True:
    print("\n1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")
    choice = input("Enter your choice (1-8): ")


    if choice == "1":
        a, b = get_numbers()
        result = f"{a}+{b} = {add(a, b)}"

    elif choice == "2":
        a, b = get_numbers()
        result = f"{a}-{b} = {subtract(a, b)}"

    elif choice == "3":
        a, b = get_numbers()
        result = f"{a}*{b} = {multiply(a, b)}"

    elif choice == "4":
        a, b = get_numbers()
        result = f"{a}/{b} = {divide(a, b)}"

    elif choice == "5":
        a, b = get_numbers()
        result = f"{a}%{b} = {modulus(a, b)}"

    elif choice == "6":
        a, b = get_numbers()
        result = f"{a}^{b} = {power(a, b)}"

    elif choice == "7":
        for item in history:
            print(item)
        continue

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
        continue

    print("[RESULT]", result)
    history.append(result)
