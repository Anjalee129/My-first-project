from functions import calculate_average, assign_grade, calculate_gpa


def main():
    print("🎓 Welcome to the Student Grade Tracker\n")

    while True:
        student_name = input("Enter student name: ")
        subject_count = int(input("How many subjects? "))

        marks = []
        grades = []

        for i in range(subject_count):
            mark = float(input(f"Enter mark for subject {i + 1}: "))
            marks.append(mark)

        avg = calculate_average(marks)
        for mark in marks:
            grades.append(assign_grade(mark))

        final_grade = assign_grade(avg)
        gpa = calculate_gpa(grades)

        # Show results
        print(f"\n--- Report for {student_name} ---")
        print(f"Marks: {marks}")
        print(f"Grades: {grades}")
        print(f"Average: {avg:.2f}")
        print(f"Final Grade: {final_grade}")
        print(f"GPA: {gpa:.2f}")

        # Write to file
        with open("grades.txt", "a") as file:
            file.write(f"{student_name} | Marks: {marks} | Grades: {grades} | GPA: {gpa:.2f}\n")

        # Ask to continue or quit
        choice = input("\nDo you want to add another student? (y/n): ")
        if choice.lower() != 'y':
            print("Exiting Student Grade Tracker. Goodbye!")
            break


if __name__ == "__main__":
    main()
