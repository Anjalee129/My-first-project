def calculate_average(marks):
    return sum(marks) / len(marks)

def assign_grade(average):
    if average >= 75:
        return 'A'
    elif average >= 65:
        return 'B'
    elif average >= 50:
        return 'C'
    elif average >= 35:
        return 'D'
    else:
        return 'F'

def convert_grade_to_gpa(grade):
    mapping = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'F': 0.0
    }
    return mapping.get(grade.upper(), 0.0)

def calculate_gpa(grades):
    gpa_values = [convert_grade_to_gpa(g) for g in grades]
    return sum(gpa_values) / len(gpa_values)

