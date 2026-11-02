
def add_student(records, name, marks):
    records[name] = marks

def calculate_total(marks):
    return sum(marks.values())

def calculate_average(marks):
    return calculate_total(marks) / len(marks)

def display_records(records):
    print("\n---Student Records---")
    for name, marks in records.items():
        print(f"\nName    : {name}")
        for subject, score in marks.items():
            print(f"{subject}   : {score}")
        print(f"Total   : {calculate_total(marks)}")
        print(f"Average : {calculate_average(marks):.2f}")

def main():
    records = {}
    n = int(input("Enter number of students: "))
    s = int(input("Enter number of subjects: "))

    for i in range(n):
        name = input(f"\nEnter name of student {i + 1}: ")
        marks = {}
        for j in range(s):
            subject = input(f"  Subject {j + 1} name: ")
            marks[subject] = float(input(f"  Marks in {subject}: "))
        add_student(records, name, marks)

    display_records(records)


main()
