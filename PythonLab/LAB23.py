
import os

FILENAME = "lab23.txt"

SAMPLE_RECORDS = [("Rajveer", 85), ("Riya", 92), ("Karan", 78)]

def init_file(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            for name, marks in SAMPLE_RECORDS:
                f.write(f"{name},{marks}\n")

def store_student(filename, name, marks):
    with open(filename, 'a') as f:
        f.write(f"{name},{marks}\n")
    print(f"[SUCCESS] Record for '{name}' ({marks} marks) stored successfully.")

def display_and_calculate_average(filename):
    if not os.path.exists(filename):
        print(f"[ERROR] '{filename}' not found.")
        return

    names = []
    marks_list = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            name, marks = line.split(',')
            names.append(name)
            marks_list.append(int(marks))

    if not marks_list:
        print("[INFO] No student records found.")
        return

    print("="*17+"STUDENT MARKS LEDGER"+"="*17)
    print(f"{'No.':<6}{'Student Name':<22}{'Marks Obtained'}")
    print("-"*50)
    for i, (n, m) in enumerate(zip(names, marks_list), start=1):
        print(f"{i:<6}{n:<22}{m}")

    total_marks = sum(marks_list)
    average = total_marks / len(marks_list)
    print("="*55)
    print(f"Total Students : {len(marks_list)}")
    print(f"Total Marks    : {total_marks}")
    print(f"Class Average  : {average:.2f}")
    print("="*55)

def main():
    init_file(FILENAME)
    print("="*40)
    print("STUDENT MARKS FILE HANDLING TOOL")
    print("="*40)

    while True:
        print("\nSelect an operation:")
        print("1. Display Records & Class Average")
        print("2. Add & Store Student Marks")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            display_and_calculate_average(FILENAME)
        elif choice == '2':
            name = input("Enter Student Name: ").strip()
            if not name or ',' in name:
                print("[ERROR] Name cannot be empty or contain a comma.")
                continue
            try:
                marks = int(input("Enter Marks (0-100): "))
            except ValueError:
                print("[ERROR] Marks must be an integer.")
                continue
            if 0 <= marks <= 100:
                store_student(FILENAME, name, marks)
            else:
                print("[ERROR] Marks must be between 0 and 100.")
        elif choice == '3':
            print("Thank you for using Student Marks Tool. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()