"""
EnrollmentManager Class - Course Registration System
=====================================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Name: Matthew Lipnicki
Student ID: 000987196
Date Completed: 12/12/2025

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

        Author: Matthew Lipnicki
        Date: 12/10/2025
        Version: 1.0
        """
        # Store manager references as class variables
        self.student_manager = student_manager
        self.course_manager = course_manager
        # Initialize _enrollments as empty list
        self._enrollments = []
        # Call read_enrollments_file()
        self.read_enrollments_file()
        # TODO: Update course enrollment counts
        # locally? the course.enrolled_count? there should be no need to update on initialization
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

        Author: Matthew Lipnicki
        Date: 12/10/2025
        """
        # read enrollments.csv
        try:
            with open('data\\enrollments.csv', 'r') as enrollments_file:
                result = []
                for line in enrollments_file:
                    row_data = line.split(",")
                    result.append(row_data)
            # Convert student_id to int
            for row in result[1:]: # start at second item to skip header
                row[0] = int(row[0])        
            # add each enrollment as dictionary to self._enrollments
                self._enrollments.append({'student_id': row[0],
                                          'course_code': row[1],
                                          'semester': row[2],
                                          'grade': row[3].removesuffix("\n")})
        except FileNotFoundError:
            print("Error: The specified file was not found.")

    def write_enrollments_to_file(self):
        """
        Write all enrollment data to enrollments.csv file.

        Writes header line followed by all enrollments.

        Implementation Notes:
        - Open enrollments.csv for writing
        - Write header: "student_id,course_code,semester,grade"
        - For each enrollment dictionary, write CSV line

        Author: Matthew Lipnicki
        Date: 12/10/2025
        """
        with open("data\\enrollments.csv", 'w') as enrollments_file:
            enrollments_file.write("student_id,course_code,semester,grade\n")
            for enrollment in self._enrollments:
                enrollments_file.write(f"{enrollment['student_id']},{enrollment['course_code']},{enrollment['semester']},{enrollment['grade']}\n")
        
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

        Author: Matthew Lipnicki
        Date: 12/10/2025
        """
        # Get input from user
        registrant_id = input("Enter student ID: ")
        registrant_course_code = input("Enter course code: ")
        registrant_semester = input("Enter semester (e.g., Fall2024): ")
        try:
        # Validate student exists
            student = self.student_manager.find_student_by_id(registrant_id)
            if student is None:
                raise LookupError("student ID not found")
        # Validate course exists
            course = self.course_manager.find_course_by_code(registrant_course_code)
            if course is None:
                raise LookupError("course code not found")
        # Check if already enrolled
            for enrollment in self._enrollments:
                if enrollment['student_id'] == registrant_id:
                    if enrollment['course_code'] == registrant_course_code:
                        raise PermissionError("student is already enrolled in course")
        # Check if course is full
            if course.is_full():
                raise PermissionError("course is already full")
        # Add enrollment
            self._enrollments.append({"student_id": registrant_id,
                                      "course_code": registrant_course_code,
                                      "semester": registrant_semester,
                                      "grade": ''})
        # Update course count
            course.set_enrolled_count(course.enrolled_count + 1)
        # Save to file
            self.write_enrollments_to_file()
        
        except LookupError as error:
            print(error)
        except PermissionError as error:
            print(error)

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

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Get input from user
        student_id = input("Enter student ID: ")
        course_code = input("Enter course code: ")
        # Find enrollment
        enrollment_to_drop = None
        idx_to_drop = None
        for idx, enrollment in enumerate(self._enrollments):
            if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
                enrollment_to_drop = enrollment
                idx_to_drop = idx
        # Remove if found
        if enrollment_to_drop != None:
            del self._enrollments[idx_to_drop]
        # Update course count
        course = self.course_manager.find_course_by_code(course_code)
        course.set_enrolled_count(course.enrolled_count() - 1)
        # Save to file
        self.write_enrollments_to_file()

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

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Get student ID from user
        student_id = input("Enter student ID: ")
        # Validate student exists
        student = self.student_manager.find_student_by_id(student_id)
        if student == None:
            print("Error: Student does not exist")
            return
        # Find all enrollments for this student
        student_enrollments = []
        for enrollment in self._enrollments:
            if enrollment["student_id"] == student_id:
                student_enrollments.append(enrollment)
        # Display in formatted table
        print(f"==========================================\nSCHEDULE FOR: [{student.get_full_name()}]\n==========================================")
        print(f"Code      Course Name              Semester    Grade")
        print(f"----------------------------------------------------------")
        total_credits = 0
        for enrollment in student_enrollments:
            course = self.course_manager.find_course_by_code(enrollment["course_code"])
            course_code = enrollment["course_code"]
            course_name = course.course_name()
            semester = enrollment["semester"]
            grade = enrollment["grade"]
            total_credits += course.credits()
            print(f"{course_code}" + " "*(17-len(course_code)) + f"{course_name}" + " "*(25-len(course_name)) + f"{semester}" + " "*(12-len(semester)) + grade)
        print("==========================================")
        # Calculate and display totals
        total_courses = len(student_enrollments)
        print(f"Total Courses: {total_courses}")
        print(f"Total Credits: {total_credits}")

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

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Get course code from user
        course_code = input("Enter course code: ")
        # Validate course exists
        course = self.course_manager.find_course_by_code(course_code)
        if  course == None:
            print(f"Error: course {course_code} not found")
            return
        # Find all enrollments for this course
        enrollments_in_course = []
        for enrollment in self._enrollments:
            if enrollment["course_code"] == course_code:
                enrollments_in_course.append(enrollment)
        # Display in formatted table with student details :)
        # header
        print(f"==========================================\nROSTER FOR: [{course_code}] - [{course.course_name()}]\n==========================================")
        #table header
        print("Student ID    Name                    Year    Grade")
        print("----------------------------------------------------------")
        for enrollment in enrollments_in_course:
            student = self.student_manager.find_student_by_id(enrollment["student_id"])
            student_name = student.get_full_name()

            print(f"{enrollment["student_id"]}" + " "*4 + student_name + " "*(24-len(student_name)) + f"{student.year()}" + " "*7 + enrollment["grade"])
        # Show enrollment count
        capacity = course.capacity()
        enrolled = course.enrolled_count()
        print("==========================================")
        print(f"Enrolled: {enrolled} / {capacity}")

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

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Get input from user
        student_id = input("Enter student ID: ")
        course_code = input("Enter course code: ")
        grade = input("Enter grade (A, A-, B+, B, B-, C+, C, C-, D, F): ")
        # Validate enrollment exists
        if not self.is_student_enrolled_in_course(student_id, course_code):
            print(f"Error: Student {student_id} is not enrolled in course {course_code}")
            return
        # Validate grade format
        valid_grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D", "F"]
        if not grade in valid_grades:
            print("Error: Invalid Grade. Must be A, A-, B+, B, B-, C+, C, C-, D, F")
            return
        # Update grade in enrollment dictionary
        for enrollment in self._enrollments:
            if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
                enrollment["grade"] = grade
        # Save to file
        self.write_enrollments_to_file()

    def is_student_enrolled_in_course(self, student_id, course_code):
        """
        Check if a student is enrolled in a specific course.

        Parameters:
            student_id (int): Student ID to check
            course_code (str): Course code to check

        Returns:
            bool: True if enrolled, False otherwise

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Search _enrollments for matching student_id and course_code
        for enrollment in self._enrollments:
            if enrollment["student_id"] == student_id and enrollment["course_code"] == course_code:
                return True
        return False

    def get_student_enrollments(self, student_id):
        """
        Get all enrollments for a specific student.

        Parameters:
            student_id (int): Student ID

        Returns:
            list: List of enrollment dictionaries for this student

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Filter _enrollments for matching student_id
        students_enrollments = []
        for enrollment in self._enrollments:
            if enrollment["student_id"] == student_id:
                students_enrollments.append(enrollment)
        # Return list of matching enrollments
        return students_enrollments

    def get_course_enrollments(self, course_code):
        """
        Get all enrollments for a specific course.

        Parameters:
            course_code (str): Course code

        Returns:
            list: List of enrollment dictionaries for this course

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Filter _enrollments for matching course_code
        list_of_enrollments = []
        for enrollment in self._enrollments:
            if enrollment["course_code"] == course_code:
                list_of_enrollments.append(enrollment)
        # Return list of matching enrollments
        return list_of_enrollments

    def get_enrollment_count_for_course(self, course_code):
        """
        Count how many students are enrolled in a course.

        Parameters:
            course_code (str): Course code

        Returns:
            int: Number of students enrolled

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Count enrollments matching course_code
        count = 0
        for enrollment in self._enrollments:
            if enrollment["course_code"] == course_code:
                count += 1
        return count

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

        Author: Matthew Lipnicki
        Date: 12/12/2025
        """
        # Display all enrollments in formatted table
        print("=================================================================================\nALL ENROLLMENTS\n=================================================================================")
        print("Student ID    Student Name           Course Code    Course Name          Semester")
        print("---------------------------------------------------------------------------------")
        for enrollment in self._enrollments:
            student = self.student_manager.find_student_by_id(enrollment["student_id"])
            course = self.course_manager.find_course_by_code(enrollment["course_code"])
            student_name = student.get_full_name()
            course_code = enrollment["course_code"]
            course_name = course.course_name()
            semester = enrollment["semester"]
            print(f"{enrollment["student_id"]}" + "    " + f"{student_name}" + " "*(23-len(student_name)) + f"{course_code}" + " "*(15-len(course_code)) + f"{course_name}" + " "*(21-len(course_name)) + f"{semester}")
        print("=================================================================================")
        print(f"Total Enrollments: {len(self._enrollments)}")

    def get_number_of_enrollments(self):
        return len(self._enrollments)

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
