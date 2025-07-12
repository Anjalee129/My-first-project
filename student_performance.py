# Dictionary to store student marks by subject
students_data = {
    'Hasini': {'Math': 85, 'English': 78, 'Science': 92},
    'Praveen': {'Math': 58, 'English': 64, 'Science': 70},
    'Methma': {'Math': 90, 'English': 88, 'Science': 85},
    'Dinuka': {'Math': 72, 'English': 60, 'Science': 68}
}

# Function to calculate subject-wise average for a student
def calculate_student_average(subject_marks):
    total = sum(subject_marks.values())
    return total / len(subject_marks)

# Function to find top-performing student
def find_top_student(data):
    top_student = None
    top_average = 0
    for student, subjects in data.items():
        avg = calculate_student_average(subjects)
        if avg > top_average:
            top_average = avg
            top_student = student
    return top_student, top_average

# Function to print report for all students
def print_students_report(data):
    for student, subjects in data.items():
        avg = calculate_student_average(subjects)
        print(f"{student} - Average Marks: {avg:.2f}")

# Main section
if __name__ == "__main__":
    print("STUDENT PERFORMANCE REPORT\n")
    print_students_report(students_data)
    top_student, top_avg = find_top_student(students_data)
    print(f"\nTop Performer: {top_student} with an average of {top_avg:.2f}")
