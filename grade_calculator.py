print("==============================")
print("      GRADE CALCULATOR")
print("==============================")

name = input("Enter student name: ")
grade = float(input("Enter your grade: "))

print("------------------------------")
print("Student Name:", name)
print("Grade:", grade)

if grade >= 90 and grade <= 100:
    print("Remarks: Excellent")
elif grade >= 85:
    print("Remarks: Very Good")
elif grade >= 80:
    print("Remarks: Good")
elif grade >= 75:
    print("Remarks: Passed")
elif grade >= 0:
    print("Remarks: Failed")
else:
    print("Invalid Grade")