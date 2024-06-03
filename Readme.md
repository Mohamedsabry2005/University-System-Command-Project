## University Management System

This Python command-line application provides a user-friendly interface for managing student data, grades, and courses within a university setting.

**Features:**

* **Data Management:**
    * Generate Excel files for data export and import.
    * Add, edit (update and delete), and view student information.
    * Manage course enrollments and withdrawals.
* **Grade Management:**
    * Enter, update, and delete student grades for individual courses.
    * Calculate the GPA (Grade Point Average) for each student.
* **Data Analysis:**
    * Compute statistics for courses (maximum, minimum, median, and average grades).
    * Sort students by their IDs for easy organization.
* **User Interface Enhancements:**
    * Utilize the `questionary` library for interactive user input.
    * Employ the `prettytable` library to format and display data in a clear and readable manner.

**Getting Started:**

1. **Prerequisites:**
    * Python 3 ([https://www.python.org/downloads/](https://www.python.org/downloads/))
    * `questionary` library: `pip install questionary`
    * `prettytable` library: `pip install prettytable`
2. **Installation:**
    * Clone this repository or download the project files.
    * Navigate to the project directory in your terminal.
3. **Usage:**
    * Run the main script using `python project.py`.
    * Follow the on-screen instructions to interact with the system.

**Example Usage:**

![demo project Gif](./demoProject.gif)

```
$ python project.py

Welcome to Our University system:

? Select operation:  (Use arrow keys)
  » Show excel file
    Courses
    Students
    Exit

```

**Contribution:**

Feel free to contribute to this project by:

* Reporting bugs or suggesting improvements through pull requests.
* Extending the functionalities based on your needs.

**Credits:**

* This project utilizes the following libraries:
    * `questionary` ([https://questionary.readthedocs.io/en/stable/](https://questionary.readthedocs.io/en/stable/))
    * `prettytable` ([https://pypi.org/project/prettytable/](https://pypi.org/project/prettytable/))


**Enjoy using the University Management System!**
