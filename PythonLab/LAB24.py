
import csv
import os

FILENAME = "lab24.csv"
SAMPLE_ROWS = [
    (101, "Rajveer", "Python", 85),
    (102, "Laksh", "Python", 92),
    (103, "Karan", "Python", 45),
    (104, "Soham", "Python", 78),
    (105, "Rohit", "Python", 38),
    (106, "Tejas", "Python", 62),
]

def init_csv(filename):
    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["RollNo", "Name", "Subject", "Marks"])
            writer.writerows(SAMPLE_ROWS)

def print_table(rows):
    print(f"{'Roll No':<10}{'Name':<15}{'Subject':<12}{'Marks'}")
    print("-" * 45)
    for row in rows:
        print(f"{row['RollNo']:<10}{row['Name']:<15}{row['Subject']:<12}{row['Marks']}")

def read_all_students(filename):
    with open(filename, 'r', newline='') as f:
        rows = list(csv.DictReader(f))

    print("=" * 10 + "ALL ENROLLED STUDENTS" + "=" * 10)
    print_table(rows)
    print("=" * 45)
    print(f"Total Records: {len(rows)}")

def filter_students_above_threshold(filename, threshold=50):
    with open(filename, 'r', newline='') as f:
        matched = [row for row in csv.DictReader(f) if int(row['Marks']) > threshold]

    print("="*8+f"STUDENTS WITH MARKS>{threshold}"+"="*8)
    print_table(matched)
    print("=" * 45)
    print(f"Qualified Students Count: {len(matched)}")

def main():
    init_csv(FILENAME)
    print("="*40)
    print("STUDENT RESULT ANALYSIS SYSTEM")
    print("="*40)

    while True:
        print("\nSelect an operation:")
        print("1. Display All Students from CSV")
        print("2. Filter Students (Marks > 50)")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            read_all_students(FILENAME)
        elif choice == '2':
            filter_students_above_threshold(FILENAME)
        elif choice == '3':
            print("Thank you for using Student Result Analysis System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()