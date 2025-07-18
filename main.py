# Import functions from the external module
from functions import calculate_average, assign_grade, calculate_gpa

# Function to add a new student record
def add_student():
    student_name = input("Enter student name: ")
    subject_count = int(input("How many subjects? "))

    marks = []
    grades = []

    # Loop to collect marks for each subject with validation
    for i in range(subject_count):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {i + 1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Mark must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    # Calculate average, grades, final grade, and GPA
    avg = calculate_average(marks)
    for mark in marks:
        grades.append(assign_grade(mark))

    final_grade = assign_grade(avg)
    gpa = calculate_gpa(grades)

    # Show student report
    print(f"\n--- Report for {student_name} ---")
    print(f"Marks: {marks}")
    print(f"Grades: {grades}")
    print(f"Average: {avg:.2f}")
    print(f"Final Grade: {final_grade}")
    print(f"GPA: {gpa:.2f}")

    # Save the record to a file
    with open("grades.txt", "a") as file:
        file.write(f"{student_name}, Marks: {marks}, Grades: {grades}, GPA: {gpa:.2f}\n")

# Function to delete a student record by name
def delete_student():
    name_to_delete = input("Enter the student's name to delete: ")
    try:
        with open("grades.txt", "r") as file:
            lines = file.readlines()

        with open("grades.txt", "w") as file:
            deleted = False
            for line in lines:
                # Keep lines that don't match the student's name
                if not line.startswith(name_to_delete + ","):
                    file.write(line)
                else:
                    deleted = True

        if deleted:
            print(f"{name_to_delete}'s record deleted.")
        else:
            print(f"No record found for {name_to_delete}.")
    except FileNotFoundError:
        print("grades.txt not found.")

# Main function to display the menu and handle user choices
def main():
    print("🎓 Welcome to the Student Grade Tracker\n")

    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. Delete a student record")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            print("Exiting Student Grade Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program only if executed directly (not imported)
if __name__ == "__main__":
    main()

