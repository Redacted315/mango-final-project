"""
EnrollmentManager Class - Course Registration System
=====================================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Name: _______________________
Student ID: _________________
Date Completed: _____________

PURPOSE:
Manages student enrollments in courses. Handles loading/saving enrollment
data and provides operations for registering/dropping students from courses.

RESPONSIBILITIES:
- Load enrollment data from enrollments.csv file
- Save enrollment data back to enrollments.csv file
- Register students in courses (with validation)
- Drop students from courses
- Display student schedules
- Display course rosters
- Check enrollment status
- Assign/update grades

DATA FILE FORMAT (enrollments.csv):
student_id,course_code,semester,grade
2023047891,CPRG216,Fall2024,
2023051234,CPRG251,Fall2024,A

NOTE: grade field is empty until assigned

FILE DEPENDENCIES:
- enrollments.csv (data file)
- student_manager.py (StudentManager class)
- course_manager.py (CourseManager class)

"""


class EnrollmentManager:
    def __init__(self, student_manager, course_manager):
        """
        Initialize the EnrollmentManager.

        Parameters:
            student_manager (StudentManager): Reference to StudentManager
            course_manager (CourseManager): Reference to CourseManager

        Implementation Notes:
        - Store references to student_manager and course_manager
        - Initialize empty _enrollments list (stores dictionaries)
        - Call read_enrollments_file() to load existing data
        - Update course enrollment counts

        Author: [Your Name]
        Date: [Date]
        Version: 1.0
        """
        # TODO: Store manager references
        # TODO: Initialize _enrollments as empty list
        # TODO: Call read_enrollments_file()
        # TODO: Update course enrollment counts
        pass

    def read_enrollments_file(self):
        """
        Read enrollment data from enrollments.csv.

        File Format:
        student_id,course_code,semester,grade

        Each enrollment is stored as a dictionary:
        {
            'student_id': 2023047891,
            'course_code': 'CPRG216',
            'semester': 'Fall2024',
            'grade': ''  # Empty string if no grade yet
        }

        Implementation Notes:
        - Open enrollments.csv for reading
        - Skip header line
        - For each line, create a dictionary and add to _enrollments
        - Handle FileNotFoundError

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Implement file reading
        # TODO: Convert student_id to int
        # TODO: Store each enrollment as dictionary
        pass

    def write_enrollments_to_file(self):
        """
        Write all enrollment data to enrollments.csv file.

        Writes header line followed by all enrollments.

        Implementation Notes:
        - Open enrollments.csv for writing
        - Write header: "student_id,course_code,semester,grade"
        - For each enrollment dictionary, write CSV line

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Implement file writing
        pass

    def register_student_in_course(self):
        """
        Register a student in a course through user input.

        Prompts:
        - Enter student ID:
        - Enter course code:
        - Enter semester (e.g., Fall2024):

        Validation:
        - Student must exist in system
        - Course must exist in system
        - Course must not be full
        - Student must not already be enrolled in this course

        Outputs:
        - Success: "Student [Name] successfully registered in [Course Name]"
        - Error messages for validation failures

        Implementation Notes:
        - Check all validations before adding
        - Add new enrollment dictionary to _enrollments list
        - Update course enrollment count
        - Save to file

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get input from user
        # TODO: Validate student exists
        # TODO: Validate course exists
        # TODO: Check if already enrolled
        # TODO: Check if course is full
        # TODO: Add enrollment
        # TODO: Update course count
        # TODO: Save to file
        pass

    def drop_student_from_course(self):
        """
        Drop a student from a course.

        Prompts:
        - Enter student ID:
        - Enter course code:

        Validation:
        - Enrollment must exist

        Outputs:
        - Success: "Student [Name] dropped from [Course Name]"
        - Error: "Student is not enrolled in this course"

        Implementation Notes:
        - Find matching enrollment
        - Remove from _enrollments list
        - Update course enrollment count
        - Save to file

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get input from user
        # TODO: Find enrollment
        # TODO: Remove if found
        # TODO: Update course count
        # TODO: Save to file
        pass

    def display_student_schedule(self):
        """
        Display all courses a student is enrolled in.

        Prompts:
        - Enter student ID:

        Format:
        ==========================================
        SCHEDULE FOR: [Student Name]
        ==========================================
        Code      Course Name              Semester    Grade
        ----------------------------------------------------------
        CPRG216   Python Programming       Fall2024    -
        DMIT1508  Database Fundamentals    Fall2024    A
        ==========================================
        Total Courses: [count]
        Total Credits: [sum of credits]

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get student ID from user
        # TODO: Validate student exists
        # TODO: Find all enrollments for this student
        # TODO: Display in formatted table
        # TODO: Calculate and display totals
        pass

    def display_course_roster(self):
        """
        Display all students enrolled in a course.

        Prompts:
        - Enter course code:

        Format:
        ==========================================
        ROSTER FOR: [Course Code] - [Course Name]
        ==========================================
        Student ID    Name                    Year    Grade
        ----------------------------------------------------------
        2023047891    Sarah Johnson           1       -
        2023089456    Olivia Anderson         1       A
        ==========================================
        Enrolled: [count] / [capacity]

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get course code from user
        # TODO: Validate course exists
        # TODO: Find all enrollments for this course
        # TODO: Display in formatted table with student details
        # TODO: Show enrollment count
        pass

    def assign_grade(self):
        """
        Assign or update a grade for a student in a course.

        Prompts:
        - Enter student ID:
        - Enter course code:
        - Enter grade (A, A-, B+, B, B-, C+, C, C-, D, F):

        Validation:
        - Enrollment must exist
        - Grade must be valid

        Outputs:
        - Success: "Grade [grade] assigned to [Student Name] for [Course Name]"
        - Error messages for validation failures

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get input from user
        # TODO: Validate enrollment exists
        # TODO: Validate grade format
        # TODO: Update grade in enrollment dictionary
        # TODO: Save to file
        pass

    def is_student_enrolled_in_course(self, student_id, course_code):
        """
        Check if a student is enrolled in a specific course.

        Parameters:
            student_id (int): Student ID to check
            course_code (str): Course code to check

        Returns:
            bool: True if enrolled, False otherwise

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Search _enrollments for matching student_id and course_code
        pass

    def get_student_enrollments(self, student_id):
        """
        Get all enrollments for a specific student.

        Parameters:
            student_id (int): Student ID

        Returns:
            list: List of enrollment dictionaries for this student

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Filter _enrollments for matching student_id
        # TODO: Return list of matching enrollments
        pass

    def get_course_enrollments(self, course_code):
        """
        Get all enrollments for a specific course.

        Parameters:
            course_code (str): Course code

        Returns:
            list: List of enrollment dictionaries for this course

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Filter _enrollments for matching course_code
        # TODO: Return list of matching enrollments
        pass

    def get_enrollment_count_for_course(self, course_code):
        """
        Count how many students are enrolled in a course.

        Parameters:
            course_code (str): Course code

        Returns:
            int: Number of students enrolled

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Count enrollments matching course_code
        pass

    def display_all_enrollments(self):
        """
        Display all enrollments in the system.

        Format:
        =================================================================================
        ALL ENROLLMENTS
        =================================================================================
        Student ID    Student Name           Course Code    Course Name          Semester
        ---------------------------------------------------------------------------------
        2023047891    Sarah Johnson          CPRG216        Python Programming   Fall2024
        2023051234    Michael Chen           CPRG251        OOP Programming      Fall2024
        =================================================================================
        Total Enrollments: [count]

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Display all enrollments in formatted table
        # TODO: Show student and course details for each enrollment
        pass


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_enrollment_manager():
    """Test the EnrollmentManager class implementation."""
    print("=" * 70)
    print("TESTING ENROLLMENT MANAGER CLASS")
    print("=" * 70)
    print()

    # Note: This test requires StudentManager and CourseManager
    # to be implemented first

    from student_manager import StudentManager
    from course_manager import CourseManager

    print("Test 1: Initialize EnrollmentManager...")
    student_mgr = StudentManager()
    course_mgr = CourseManager()
    enrollment_mgr = EnrollmentManager(student_mgr, course_mgr)
    print("✓ Manager created")
    print()

    print("Test 2: Display all enrollments...")
    enrollment_mgr.display_all_enrollments()
    print()


if __name__ == "__main__":
    test_enrollment_manager()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
ENROLLMENT MANAGER CLASS RUBRIC (20 points total)

1. Constructor and File Loading - 3 points
   [3] Correctly initializes, loads file, updates course counts
   [2] Loads but minor issues
   [1] Partial implementation
   [0] Not implemented

2. File Writing - 2 points
   [2] Correctly writes enrollments to CSV
   [1] Writes but format issues
   [0] Not implemented

3. Register Student Method - 4 points
   [4] All validations work (student exists, course exists, not full, not duplicate)
   [3] Most validations work
   [2] Some validations work
   [1] Registers but no validation
   [0] Not implemented

4. Drop Student Method - 2 points
   [2] Finds enrollment, removes, updates count, saves
   [1] Works but issues
   [0] Not implemented

5. Display Schedule Method - 3 points
   [3] Shows all student courses with formatted table and totals
   [2] Shows courses but formatting/totals issues
   [1] Partial implementation
   [0] Not implemented

6. Display Roster Method - 3 points
   [3] Shows all course students with formatted table
   [2] Shows students but formatting issues
   [1] Partial implementation
   [0] Not implemented

7. Assign Grade Method - 2 points
   [2] Validates enrollment, updates grade, saves
   [1] Works but validation issues
   [0] Not implemented

8. Helper Methods - 1 point
   [1] All helper methods work correctly
   [0] Missing or not working

TOTAL: ___ / 20 points

NOTES:
"""
