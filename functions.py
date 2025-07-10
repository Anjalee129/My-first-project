# Function to calculate the average of a list of marks
def calculate_average(marks):
    return sum(marks) / len(marks)

# Function to assign a letter grade based on the average mark
def assign_grade(average):
    if average >= 75:
        return 'A'       # Excellent
    elif average >= 65:
        return 'B'       # Good
    elif average >= 50:
        return 'C'       # Pass
    elif average >= 35:
        return 'D'       # Weak pass
    else:
        return 'F'       # Fail

# Helper function to convert a letter grade into GPA value
def convert_grade_to_gpa(grade):
    mapping = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return mapping.get(grade.upper(), 0.0)  # Defaults to 0.0 if grade is not found

# Function to calculate the GPA from a list of letter grades
def calculate_gpa(grades):
    gpa_values = [convert_grade_to_gpa(g) for g in grades]  # Convert each grade to GPA
    return sum(gpa_values) / len(gpa_values)                # Return the average GPA
