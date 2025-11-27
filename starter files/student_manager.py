"""
StudentManager Class - Course Registration System
==================================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Name: _______________________
Student ID: _________________
Date Completed: _____________

PURPOSE:
Manages the collection of all students in the system. Handles loading/saving
student data from/to CSV file and provides CRUD operations (Create, Read,
Update, Delete) for students.

RESPONSIBILITIES:
- Load student data from students.csv file
- Save student data back to students.csv file
- Add new students to the system
- Remove students from the system
- Search for students by ID or name
- Display student information
- Edit existing student information

FILE DEPENDENCIES:
- students.csv (data file)
- student.py (Student class)

"""

from student import Student


class StudentManager:
    def __init__(self):
        """
        Initialize the StudentManager.

        Creates an empty list of students and loads data from students.csv file.

        Implementation Notes:
        - Initialize empty _students list (private attribute)
        - Call read_students_file() to load existing data

        Author: [Your Name]
        Date: [Date]
        Version: 1.0
        """
        # TODO: Initialize _students as empty list
        # TODO: Call read_students_file()
        pass

    @property
    def students(self):
        """
        Get the list of all students.

        Returns:
            list: List of Student objects

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return private _students list
        pass

    def read_students_file(self):
        """
        Read student data from students.csv and populate the students list.

        File Format:
        student_id,first_name,last_name,email,program,year

        Implementation Notes:
        - Open students.csv for reading
        - Skip the header line
        - For each data line, split by comma and create Student object
        - Add each Student to _students list
        - Handle FileNotFoundError if file doesn't exist

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Implement file reading
        # Hint: Use try/except for FileNotFoundError
        # Hint: Use with open() to ensure file closes properly
        # Hint: Use .strip().split(',') to parse CSV lines
        pass

    def write_students_to_file(self):
        """
        Write all student data to students.csv file.

        Writes header line followed by all students in CSV format.

        Implementation Notes:
        - Open students.csv for writing (will overwrite existing)
        - Write header: "student_id,first_name,last_name,email,program,year"
        - For each student, write their to_csv_format() output

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Implement file writing
        # Hint: Use student.to_csv_format() method
        pass

    def add_student(self):
        """
        Add a new student to the system through user input.

        Prompts user for all student information, creates a new Student
        object, adds it to the list, and saves to file.

        Prompts:
        - Enter student's first name:
        - Enter student's last name:
        - Enter student's email:
        - Enter student's program:
        - Enter student's year (1-4):

        Implementation Notes:
        - Student ID should be auto-generated (pass None to constructor)
        - Convert year input to int
        - Add student to _students list
        - Call write_students_to_file() to save
        - Print confirmation: "Student [ID] added successfully!"

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get input from user
        # TODO: Create new Student object
        # TODO: Add to _students list
        # TODO: Save to file
        # TODO: Print confirmation
        pass

    def remove_student(self):
        """
        Remove a student from the system by ID.

        Prompts user for student ID, searches for student, removes if found,
        and saves updated data to file.

        Prompts:
        - Enter student ID to remove:

        Outputs:
        - If found: "Student [Name] (ID: [ID]) removed successfully."
        - If not found: "Error: No student found with ID [ID]"

        Implementation Notes:
        - Search _students list for matching student_id
        - If found, remove from list and save to file
        - If not found, display error message

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get student ID from user
        # TODO: Search for student in _students list
        # TODO: Remove if found, save file
        # TODO: Display appropriate message
        pass

    def search_student_by_id(self):
        """
        Search for a student by their ID and display their information.

        Prompts:
        - Enter student ID to search:

        Outputs:
        - If found: Display student using display_student_info()
        - If not found: "Error: No student found with ID [ID]"

        Returns:
            Student or None: The found Student object, or None if not found

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get student ID from user (convert to int)
        # TODO: Search _students list for matching student_id
        # TODO: If found, call display_student_info() and return student
        # TODO: If not found, display error and return None
        pass

    def search_student_by_name(self):
        """
        Search for students by name (first or last) and display results.

        Searches for partial matches in both first and last names (case-insensitive).

        Prompts:
        - Enter student name to search:

        Outputs:
        - If found: Display all matching students in table format
        - If not found: "No students found matching '[name]'"

        Implementation Notes:
        - Search should be case-insensitive
        - Should find partial matches (e.g., "john" finds "Johnson")
        - Display all matching students using display_students_list()

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get search term from user
        # TODO: Search _students for matches in first_name or last_name
        # TODO: Display results or error message
        # Hint: Use .lower() for case-insensitive comparison
        # Hint: Use 'in' operator for partial matches
        pass

    def edit_student_info(self):
        """
        Edit an existing student's information.

        Prompts:
        - Enter student ID to edit:
        - Enter new first name (or press Enter to skip):
        - Enter new last name (or press Enter to skip):
        - Enter new email (or press Enter to skip):
        - Enter new program (or press Enter to skip):
        - Enter new year 1-4 (or press Enter to skip):

        Outputs:
        - If found: "Student [ID] updated successfully!"
        - If not found: "Error: No student found with ID [ID]"

        Implementation Notes:
        - Only update fields where user provides input
        - Empty input means "don't change this field"
        - Save to file after successful edit

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get student ID from user
        # TODO: Find student in _students list
        # TODO: For each attribute, prompt for new value
        # TODO: Update only if user enters something (not empty)
        # TODO: Save to file
        # Hint: Check if input.strip() to see if user entered anything
        pass

    def display_student_info(self, student):
        """
        Display detailed information for a single student.

        Format:
        ==========================================
        STUDENT INFORMATION
        ==========================================
        Student ID:   [id]
        Name:         [first] [last]
        Email:        [email]
        Program:      [program]
        Year:         [year]
        ==========================================

        Parameters:
            student (Student): The student object to display

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Print formatted student information as shown above
        pass

    def display_students_list(self):
        """
        Display all students in a formatted table.

        Format:
        ====================================================================================
        STUDENT LIST
        ====================================================================================
        ID           Name                    Email                          Program           Year
        ------------------------------------------------------------------------------------
        2023047891   Sarah Johnson          sarah.johnson@mystudent.ca     Comp Prog         1
        2023051234   Michael Chen           michael.chen@mystudent.ca      Software Dev      2
        ====================================================================================
        Total Students: [count]

        Implementation Notes:
        - Use formatting to align columns nicely
        - Truncate long program names if needed
        - Display count at the end

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Print header
        # TODO: Loop through _students and print each in table format
        # TODO: Print total count
        # Hint: Use f-strings with width specifiers for alignment
        # Example: f"{value:<15}" left-aligns in 15 character width
        pass

    def get_student_count(self):
        """
        Get the total number of students in the system.

        Returns:
            int: Number of students

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return length of _students list
        pass

    def find_student_by_id(self, student_id):
        """
        Find and return a student by their ID (helper method for other classes).

        Parameters:
            student_id (int): The student ID to search for

        Returns:
            Student or None: The Student object if found, None otherwise

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Search _students list for matching student_id
        # TODO: Return Student object if found, None otherwise
        pass


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_student_manager():
    """Test the StudentManager class implementation."""
    print("=" * 70)
    print("TESTING STUDENT MANAGER CLASS")
    print("=" * 70)
    print()

    # Test 1: Initialize and load data
    print("Test 1: Initialize StudentManager...")
    manager = StudentManager()
    print(f"✓ Manager created")
    print(f"  Students loaded: {manager.get_student_count()}")
    print()

    # Test 2: Display all students
    print("Test 2: Display all students...")
    manager.display_students_list()
    print()

    # Test 3: Search by ID
    print("Test 3: Search student by ID...")
    print("Searching for ID: 2023047891")
    manager.search_student_by_id()  # Will prompt for ID in actual use
    print()

    # Test 4: Display single student
    print("Test 4: Display single student info...")
    student = manager.find_student_by_id(2023047891)
    if student:
        manager.display_student_info(student)
    print()


if __name__ == "__main__":
    test_student_manager()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
STUDENT MANAGER CLASS RUBRIC (20 points total)

1. Constructor and File Loading - 4 points
   [4] Correctly initializes list and loads from file with error handling
   [3] Loads data but minor issues with error handling
   [2] Loads data but has significant issues
   [1] Constructor exists but doesn't load data properly
   [0] Not implemented or doesn't work

2. File Writing - 2 points
   [2] Correctly writes all students to CSV file with proper format
   [1] Writes to file but format issues
   [0] Not implemented or doesn't work

3. Add Student Method - 3 points
   [3] Prompts for all info, creates student, adds to list, saves to file
   [2] Works but missing some functionality
   [1] Partially working
   [0] Not implemented or doesn't work

4. Remove Student Method - 3 points
   [3] Finds student, removes from list, saves file, appropriate messages
   [2] Works but minor issues with error handling or messages
   [1] Partially working
   [0] Not implemented or doesn't work

5. Search Methods (by ID and by name) - 4 points
   [4] Both search methods work correctly with appropriate error messages
   [3] Both work but minor issues
   [2] One search method works correctly
   [1] Partially implemented
   [0] Not implemented or doesn't work

6. Edit Student Method - 2 points
   [2] Allows editing all fields, handles empty input, saves changes
   [1] Works but has issues
   [0] Not implemented or doesn't work

7. Display Methods - 2 points
   [2] Both display methods format output nicely and correctly
   [1] Display works but formatting issues
   [0] Not implemented or doesn't work

TOTAL: ___ / 20 points

NOTES:
"""
