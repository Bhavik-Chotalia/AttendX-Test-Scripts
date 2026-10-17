# Test case for attendance marking

def mark_attendance(student_id, status):
    if student_id == "":
        return "Student ID is required"

    if status not in ["Present", "Absent"]:
        return "Invalid attendance status"

    return "Attendance marked successfully"


# Test execution
print(mark_attendance("ST101", "Present"))
print(mark_attendance("", "Present"))
print(mark_attendance("ST102", "Unknown"))