# 🎓 Student Grade Tracker

This is a beginner-friendly Python project designed to manage student records through a command-line interface. It supports adding students with marks, calculating average scores, assigning grades, computing GPA, and deleting records. All data is stored in a simple text file.

---

## ✅ Features

- Add a new student and input marks
- Automatically calculate:
  - Subject-wise grades
  - Average score
  - Final grade
  - GPA
- Delete a student record by name
- Store all records in `grades.txt`
- Modular functions with input validation
- Clean and simple user interface

---

## 📁 Project Structure

```
My-first-project/
├── functions.py       # Helper functions: grade assignment, GPA calculation
├── main.py            # Main CLI application
├── grades.txt         # Saved student records
├── README.md          # Project documentation (this file)
├── README.txt         # Original test file (optional)
```

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Anjalee129/My-first-project.git
   cd My-first-project
   ```

2. Run the application:
   ```bash
   python main.py
   ```

---

## 🧪 Sample Usage

```
🎓 Welcome to the Student Grade Tracker

Menu:
1. Add a student
2. Delete a student record
3. Exit
```

**Example Output:**
```
Enter student name: Alex
How many subjects? 3
Enter mark for subject 1: 85
Enter mark for subject 2: 90
Enter mark for subject 3: 78

--- Report for Alex ---
Marks: [85.0, 90.0, 78.0]
Grades: ['A', 'A+', 'B']
Average: 84.33
Final Grade: A
GPA: 3.67
```

---

## 👩‍💻 Author

Developed by **Anjalee129**  
Bonus feature `delete_student()` was contributed by a friend 🚀

---

## 📝 License

This project is for learning and demonstration purposes. You are welcome to reuse or modify it.

---


