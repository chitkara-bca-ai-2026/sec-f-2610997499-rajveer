
name = input("Enter Student Name : ")
roll = input("Enter Roll Number  : ")


print()
print("---Enter Marks for 5 Subjects (0-100)---")


total = 0.0
failed = False


for i in range(1, 6):
    marks = float(input(f"Enter marks for Subject {i}: "))
    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100.")
        exit()
    if marks < 40:
        failed = True
    total += marks

percentage = (total / 500) * 100

if failed:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"
else:
    result = "PASS"
    if percentage >= 90:
        grade, remark = "A+", "Outstanding"
    elif percentage >= 80:
        grade, remark = "A", "Excellent"
    elif percentage >= 70:
        grade, remark = "B", "Very Good"
    elif percentage >= 60:
        grade, remark = "C", "Good"
    elif percentage >= 50:
        grade, remark = "D", "Satisfactory"
    elif percentage >= 40:
        grade, remark = "E", "Pass"
    else:
        grade, remark = "F", "Fail"

print()

print("                STUDENT REPORT CARD")
print(f"  Student Name : {name}")
print(f"  Roll Number  : {roll}")
print(f"  Total Marks  : {total} / 500.0")
print(f"  Percentage   : {percentage:.2f}%")
print(f"  Result       : {result}")
print(f"  Grade        : {grade}")
print(f"  Remarks      : {remark}")
