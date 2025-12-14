"""
Main Application - Course Registration System
==============================================

TEAM MEMBER ASSIGNED TO THIS FILE:
Name: Matthew Lipnicki
Student ID: 000987196
Date Completed: 12/13/2025

PURPOSE:
Main entry point for the Course Registration System. Provides menu-based
interface for accessing all system functions.

RESPONSIBILITIES:
- Initialize all manager objects
- Display main menu and submenus
- Route user selections to appropriate manager methods
- Handle program flow and user navigation
- Provide clean exit

FILE DEPENDENCIES:
- student_manager.py (StudentManager class)
- course_manager.py (CourseManager class)
- enrollment_manager.py (EnrollmentManager class)

"""

from student_manager import StudentManager
from course_manager import CourseManager
from enrollment_manager import EnrollmentManager


class RegistrationSystem:
    def __init__(self):
        """
        Initialize the Registration System.

        Creates all manager objects and links them together.

        Implementation Notes:
        - Create StudentManager instance
        - Create CourseManager instance
        - Create EnrollmentManager instance (pass student and course managers)

        Author: Matthew Lipnicki
        Date: 12/13/2025
        Version: 1.0
        """
        print("=" * 70)
        print("COURSE REGISTRATION SYSTEM")
        print("Initializing...")
        print("=" * 70)

        # Create manager instances
        self.student_manager = StudentManager()
        self.course_manager = CourseManager()
        self.enrollment_manager = EnrollmentManager(self.student_manager, self.course_manager)

        print("✓ System initialized successfully!")
        print()

    def display_main_menu(self):
        """
        Display the main menu and handle user selection.

        Main Menu Options:
        1 - Student Management
        2 - Course Management
        3 - Enrollment Management
        4 - Reports
        5 - Exit Program

        Implementation Notes:
        - Display menu in a loop until user selects exit
        - Call appropriate submenu method based on selection
        - Handle invalid input gracefully

        Author: Matthew Lipnicki
        Date: 12/13/2025
        """
        while True:
            print("=" * 70)
            print("MAIN MENU")
            print("=" * 70)
            print("1 - Student Management")
            print("2 - Course Management")
            print("3 - Enrollment Management")
            print("4 - Reports")
            print("5 - Exit Program")
            print("=" * 70)

            # Get user choice
            user_choice = input()
            # Call appropriate submenu method
            if user_choice == "1":
                self.display_student_menu()
            elif user_choice == "2":
                self.display_course_menu()
            elif user_choice == "3":
                self.display_enrollment_menu()
            elif user_choice == "4":
                self.display_reports_menu()
            # Break loop if user selects exit
            elif user_choice == "5":
                break

            # Handle invalid input
            else:
                print("Error: invalid input")
                continue

    def display_student_menu(self):
        """
        Display the student management submenu.

        Student Menu Options:
        1 - Display all students
        2 - Search student by ID
        3 - Search student by name
        4 - Add new student
        5 - Edit student information
        6 - Remove student
        7 - Return to main menu

        Implementation Notes:
        - Loop until user selects return option
        - Call appropriate StudentManager methods
        - Handle invalid input

        Author: Matthew Lipnicki
        Date: 12/13/2005
        """
        while True:
            print("\n" + "=" * 70)
            print("STUDENT MANAGEMENT")
            print("=" * 70)
            print("1 - Display all students")
            print("2 - Search student by ID")
            print("3 - Search student by name")
            print("4 - Add new student")
            print("5 - Edit student information")
            print("6 - Remove student")
            print("7 - Return to main menu")
            print("=" * 70)
            # Get user choice
            user_choice = input()
            # Call appropriate student_manager methods
            if user_choice == "1":
                self.student_manager.display_students_list()
            elif user_choice == "2":
                self.student_manager.search_student_by_id()
            elif user_choice == "3":
                self.student_manager.search_student_by_name()
            elif user_choice == "4":
                self.student_manager.add_student()
            elif user_choice == "5":
                self.student_manager.edit_student_info()
            elif user_choice == "6":
                self.student_manager.remove_student()
            # Break loop if user selects return
            elif user_choice == "7":
                break
            # Handle invalid input
            else:
                print("Error: invalid input")
                continue

    def display_course_menu(self):
        """
        Display the course management submenu.

        Course Menu Options:
        1 - Display all courses
        2 - Search course by code
        3 - Search courses by name
        4 - Add new course
        5 - Edit course information
        6 - Remove course
        7 - Return to main menu

        Implementation Notes:
        - Loop until user selects return option
        - Call appropriate CourseManager methods
        - Handle invalid input

        Author: Matthew Lipnicki
        Date: 12/13/2025
        """
        while True:
            print("\n" + "=" * 70)
            print("COURSE MANAGEMENT")
            print("=" * 70)
            print("1 - Display all courses")
            print("2 - Search course by code")
            print("3 - Search courses by name")
            print("4 - Add new course")
            print("5 - Edit course information")
            print("6 - Remove course")
            print("7 - Return to main menu")
            print("=" * 70)

            # Get user choice
            user_choice = input()
            # TODO: Call appropriate course_manager methods
            if user_choice == "1":
                self.course_manager.display_courses_list()
            elif user_choice == "2":
                self.course_manager.search_course_by_code()
            elif user_choice == "3":
                self.course_manager.search_courses_by_name()
            elif user_choice == "4":
                self.course_manager.add_course()
            elif user_choice == "5":
                self.course_manager.edit_course_info()
            elif user_choice == "6":
                self.course_manager.remove_course()
            # TODO: Break loop if user selects return
            elif user_choice == "7":
                break
            # TODO: Handle invalid input
            else:
                print("Error: invalid input")
                continue

    def display_enrollment_menu(self):
        """
        Display the enrollment management submenu.

        Enrollment Menu Options:
        1 - Register student in course
        2 - Drop student from course
        3 - Display student schedule
        4 - Display course roster
        5 - Assign grade
        6 - Return to main menu

        Implementation Notes:
        - Loop until user selects return option
        - Call appropriate EnrollmentManager methods
        - Handle invalid input

        Author: Matthew Lipnicki
        Date: 12/13/2025
        """
        while True:
            print("\n" + "=" * 70)
            print("ENROLLMENT MANAGEMENT")
            print("=" * 70)
            print("1 - Register student in course")
            print("2 - Drop student from course")
            print("3 - Display student schedule")
            print("4 - Display course roster")
            print("5 - Assign grade")
            print("6 - Return to main menu")
            print("=" * 70)

            # Get user choice
            user_choice = input()
            # Call appropriate enrollment_manager methods
            if user_choice == "1":
                self.enrollment_manager.register_student_in_course()
            elif user_choice == "2":
                self.enrollment_manager.drop_student_from_course()
            elif user_choice == "3":
                self.enrollment_manager.display_student_schedule()
            elif user_choice == "4":
                self.enrollment_manager.display_course_roster()
            elif user_choice == "5":
                self.enrollment_manager.assign_grade()
            # Break loop if user selects return
            elif user_choice == "6":
                break
            # Handle invalid input
            else:
                print("Error: invalid input")
                continue

    def display_reports_menu(self):
        """
        Display the reports submenu.

        Reports Menu Options:
        1 - All enrollments
        2 - System statistics
        3 - Return to main menu

        Statistics should include:
        - Total students
        - Total courses
        - Total enrollments
        - Average students per course
        - Courses with highest enrollment

        Implementation Notes:
        - Loop until user selects return option
        - Call display methods from managers
        - Calculate and display statistics

        Author: Matthew Lipnicki
        Date: 12/13/2025
        """
        while True:
            print("\n" + "=" * 70)
            print("REPORTS")
            print("=" * 70)
            print("1 - All enrollments")
            print("2 - System statistics")
            print("3 - Return to main menu")
            print("=" * 70)

            # Get user choice
            user_choice = input()
            # Display appropriate reports
            if user_choice == "1":# all enrollments
                self.enrollment_manager.display_all_enrollments()
            elif user_choice == "2":
            # TODO: Calculate statistics for option 2
                pass
            # Break loop if user selects return
            elif user_choice == "3":
                break
            else:
                print("Error: invalid input")
                continue


    def display_statistics(self):
        """
        Display system statistics.

        Shows:
        - Total number of students
        - Total number of courses
        - Total number of enrollments
        - Average students per course
        - Course with highest enrollment

        Author: Matthew Lipnicki
        Date: 12/13/2025
        """
        print("\n" + "=" * 70)
        print("SYSTEM STATISTICS")
        print("=" * 70)

        # TODO: Get counts from managers
        num_of_students = self.student_manager.get_student_count()
        num_of_courses = self.course_manager.get_course_count()
        num_of_enrollments = self.enrollment_manager.get_number_of_enrollments()

        # TODO: Calculate averages
        # students per course
        avg_students_per_course = num_of_students / num_of_courses
        # TODO: Find course with highest enrollment
        courses = self.course_manager.courses()
        highest_enrollment_course = None
        enrollments = 0
        for course in courses:
            n = course.enrolled_count()
            if n > enrollments:
                enrollments = n
                highest_enrollment_course = course
        # TODO: Display formatted statistics
        course_name = highest_enrollment_course.course_name()
        course_code = highest_enrollment_course.course_code()
        print(f"Total number of students: {num_of_students}")
        print(f"Total number of courses: {num_of_courses}")
        print(f"Total number of enrollments: {num_of_enrollments}")
        print(f"Average students per course: {avg_students_per_course}")
        print(f"Course with highest enrollment: {course_name} ({course_code}) with {enrollments} enrollments")
        print()

    def run(self):
        """
        Start the registration system.

        Entry point for the application. Displays welcome message
        and starts the main menu loop.

        Author: Matthew Lipnicki
        Date: 12/13/2025
        """
        print("\n" + "=" * 70)
        print("WELCOME TO THE COURSE REGISTRATION SYSTEM")
        print("=" * 70)
        print()

        # Call display_main_menu() to start the application
        self.display_main_menu()

        # When user exits
        print("\n" + "=" * 70)
        print("Thank you for using the Course Registration System!")
        print("=" * 70)


# ==============================================================================
# PROGRAM ENTRY POINT (Do not modify)
# ==============================================================================

def main():
    """
    Main function - creates and runs the registration system.
    """
    system = RegistrationSystem()
    system.run()


if __name__ == "__main__":
    main()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
MAIN APPLICATION RUBRIC (20 points total)

1. System Initialization - 3 points
   [3] All managers created and linked correctly
   [2] Managers created but linking issues
   [1] Partial initialization
   [0] Not implemented

2. Main Menu - 3 points
   [3] Menu displays correctly, routes to all submenus, handles invalid input
   [2] Works but minor issues
   [1] Partial functionality
   [0] Not implemented

3. Student Management Menu - 3 points
   [3] All 7 options work correctly, proper routing to student_manager
   [2] Most options work
   [1] Some options work
   [0] Not implemented

4. Course Management Menu - 3 points
   [3] All 7 options work correctly, proper routing to course_manager
   [2] Most options work
   [1] Some options work
   [0] Not implemented

5. Enrollment Management Menu - 3 points
   [3] All 6 options work correctly, proper routing to enrollment_manager
   [2] Most options work
   [1] Some options work
   [0] Not implemented

6. Reports Menu - 3 points
   [3] Both reports work correctly with accurate statistics
   [2] Reports work but calculation issues
   [1] One report works
   [0] Not implemented

7. User Experience - 2 points
   [2] Clean interface, clear messages, error handling throughout
   [1] Functional but UX issues
   [0] Poor or no error handling

TOTAL: ___ / 20 points

NOTES:
"""
