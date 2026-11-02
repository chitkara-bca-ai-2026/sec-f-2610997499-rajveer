

students = {
    "101": {"Name": "Rajveer", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Pratyaksh", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Laksh", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]},
}


while True:
    print()
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    print()
    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        print()
        print("---Enrolled Student Records---")
        for roll, info in students.items():
            print(f"Roll No: {roll}  | Name: {info['Name']:<10} | Branch: {info['Branch']} | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        print()
        if student:
            print(f"[FOUND] Record for Roll No {roll}:")
            print(f"  Name     : {student['Name']}")
            print(f"  Branch   : {student['Branch']}")
            print(f"  Semester : {student['Semester']}")
            print(f"  Marks    : {student['Marks']}")
        else:
            print(f"[ERROR] No student found with Roll No {roll}.")

    elif choice == "3":
        print()
        print("---Register New Student---")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print(f"[ERROR] Roll No {roll} already exists.")
            continue
        name = input("Enter Student Name: ")
        branch = input("Enter Branch (e.g. BCA AI): ")
        semester = input("Enter Semester: ")
        print("Enter marks obtained in 3 subjects:")
        marks = []
        for i in range(1, 4):
            marks.append(int(input(f"  Subject {i}: ")))
        students[roll] = {"Name": name, "Branch": branch, "Semester": semester, "Marks": marks}
        print()
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        student = students.get(roll)
        if not student:
            print(f"[ERROR] No student found with Roll No {roll}.")
            continue
        print(f"Current details for {student['Name']} (Roll {roll}):")
        print(f"1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
        field = input("Choose field to update (1 for Branch, 2 for Semester): ")
        if field == "1":
            student["Branch"] = input("Enter new branch: ")
            print(f"[SUCCESS] Branch updated to '{student['Branch']}'.")
        elif field == "2":
            student["Semester"] = input("Enter new semester: ")
            print(f"[SUCCESS] Semester updated to '{student['Semester']}'.")
        else:
            print("[ERROR] Invalid field choice.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")
        student = students.get(roll)
        print()
        if student:
            total = sum(student["Marks"])
            average = total / len(student["Marks"])
            maximum = len(student["Marks"]) * 100
            result = "PASS" if average >= 40 else "FAIL"
            print("=" * 16 + " ACADEMIC REPORT " + "=" * 16)
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks  : {total} / {maximum}")
            print(f"Average Marks: {average:.2f}%")
            print(f"Final Result : {result}")
            print("=" * 48)
        else:
            print(f"[ERROR] No student found with Roll No {roll}.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")
        removed = students.pop(roll, None)
        print()
        if removed:
            print(f"[SUCCESS] Record for '{removed['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print(f"[ERROR] No student found with Roll No {roll}.")

    elif choice == "7":
        print()
        print("Thank you for using Student Information System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number from 1 to 7.")
