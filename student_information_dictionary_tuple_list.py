# Student information using Dictionary, Tuple and List

# Tuple: stores fixed attributes
attributes = ("Roll Number", "Name", "Branch", "Marks")

# List: stores student records
students = [
    (101, "Rahul", "CSE", 85),
    (102, "Amit", "IT", 78),
    (103, "Sneha", "ENTC", 90)
]

# Dictionary: stores student records using Roll Number as key
student_dict = {}

for student in students:
    student_dict[student[0]] = {
        "Name": student[1],
        "Branch": student[2],
        "Marks": student[3]
    }

# 1. Add a new student record
student_dict[104] = {
    "Name": "Priya",
    "Branch": "CSE",
    "Marks": 88
}

# 2. Delete an existing student record
del student_dict[102]

# 3. Update details of a student
student_dict[103]["Branch"] = "CSE"
student_dict[103]["Marks"] = 95

# 4. Display final student records
print("Final Student Records:")

for roll_no, details in student_dict.items():
    print("Roll Number:", roll_no)
    print("Name:", details["Name"])
    print("Branch:", details["Branch"])
    print("Marks:", details["Marks"])
    print()
