================================================================================
COURSE REGISTRATION SYSTEM - README
================================================================================

Course: CPRG216 - Python Programming
Assignment: Group Project
Date Submitted: [INSERT DATE]

================================================================================
TEAM MEMBERS
================================================================================

Team Member 1:
  Name: [INSERT NAME]
  Student ID: [INSERT ID]
  Email: [INSERT EMAIL]
  Component: Student Class (student.py)

Team Member 2:
  Name: [INSERT NAME]
  Student ID: [INSERT ID]
  Email: [INSERT EMAIL]
  Component: StudentManager Class (student_manager.py)

Team Member 3:
  Name: [INSERT NAME]
  Student ID: [INSERT ID]
  Email: [INSERT EMAIL]
  Component: Course Class & CourseManager (course.py, course_manager.py)

Team Member 4:
  Name: [INSERT NAME]
  Student ID: [INSERT ID]
  Email: [INSERT EMAIL]
  Component: EnrollmentManager Class (enrollment_manager.py)

Team Member 5:
  Name: [INSERT NAME]
  Student ID: [INSERT ID]
  Email: [INSERT EMAIL]
  Component: Main Application (main.py)

================================================================================
PEER REVIEW ASSIGNMENTS
================================================================================

Student Class (student.py):
  Reviewed by: [NAME 1], [NAME 2]

StudentManager (student_manager.py):
  Reviewed by: [NAME 1], [NAME 2]

Course + CourseManager (course.py, course_manager.py):
  Reviewed by: [NAME 1], [NAME 2]

EnrollmentManager (enrollment_manager.py):
  Reviewed by: [NAME 1], [NAME 2]

Main Application (main.py):
  Reviewed by: [NAME 1], [NAME 2]

================================================================================
HOW TO RUN THE PROGRAM
================================================================================

Prerequisites:
- Python 3.x installed
- All project files in the same directory
- CSV data files in the same directory

To run:
1. Open a terminal/command prompt
2. Navigate to the project directory:
   cd path/to/project_folder

3. Run the main program:
   python main.py

4. Follow the on-screen menu prompts

================================================================================
SYSTEM FEATURES
================================================================================

Student Management:
  [X] Display all students
  [X] Search student by ID
  [X] Search student by name
  [X] Add new student
  [X] Edit student information
  [X] Remove student

Course Management:
  [X] Display all courses
  [X] Search course by code
  [X] Search courses by name
  [X] Add new course
  [X] Edit course information
  [X] Remove course

Enrollment Management:
  [X] Register student in course
  [X] Drop student from course
  [X] Display student schedule
  [X] Display course roster
  [X] Assign grades

Reports:
  [X] View all enrollments
  [X] System statistics

================================================================================
FILE STRUCTURE
================================================================================

Data Files:
  - students.csv (student records)
  - courses.csv (course catalog)
  - enrollments.csv (registration data)

Python Files:
  - student.py (Student class)
  - student_manager.py (StudentManager class)
  - course.py (Course class)
  - course_manager.py (CourseManager class)
  - enrollment_manager.py (EnrollmentManager class)
  - main.py (Main application)

Documentation:
  - README.txt (this file)
  - PEER_REVIEW_FORM_*.md (10 peer review forms)

================================================================================
TESTING INFORMATION
================================================================================

Each component was tested:
  - Individually using built-in test code
  - With peer reviews (2 reviews per component)
  - As integrated system

Test Coverage:
  [X] Valid input handling
  [X] Invalid input handling
  [X] File I/O operations
  [X] Search functions
  [X] CRUD operations
  [X] Menu navigation
  [X] Integration between components

================================================================================
KNOWN ISSUES / LIMITATIONS
================================================================================

[INSERT ANY KNOWN ISSUES HERE]

Examples:
- None - all features working as expected
- Minor: Error message could be more descriptive when...
- Major: Feature X doesn't work when...

[IF NONE, WRITE: "No known issues - all features working as expected"]

================================================================================
CHALLENGES FACED & SOLUTIONS
================================================================================

[OPTIONAL: Describe major challenges and how you solved them]

Example:
Challenge: Keeping enrollment counts in sync between CourseManager and
           EnrollmentManager
Solution: Created helper method update_enrollment_counts() that runs after
          any enrollment change

================================================================================
COLLABORATION NOTES
================================================================================

Communication Methods:
  - [INSERT: Discord, Teams, Group Chat, etc.]
  - Regular meetings: [INSERT: Days/Times]

Division of Work:
  - All team members completed their assigned component
  - Person 5 led integration testing
  - All members participated in peer reviews

Integration Process:
  - Components developed independently in Week 1
  - Peer reviews completed in Week 2
  - Integration and testing in Week 3
  - [INSERT ANY OTHER RELEVANT INFO]

================================================================================
ADDITIONAL NOTES
================================================================================

[INSERT ANY OTHER RELEVANT INFORMATION]

Examples:
- Special features we added beyond requirements
- Design decisions we made
- Areas for future improvement
- Acknowledgments

================================================================================
GRADING CHECKLIST (For instructor use)
================================================================================

Code Submission:
  [ ] All Python files included
  [ ] All CSV files included
  [ ] README.txt included

Peer Reviews:
  [ ] 10 peer review forms included (2 per component)
  [ ] Reviews are substantive and thorough
  [ ] Author responses completed

Functionality:
  [ ] Program runs without errors
  [ ] All menu options work
  [ ] Data persists correctly
  [ ] Validation and error handling present

Documentation:
  [ ] All files have author names/IDs
  [ ] Docstrings complete
  [ ] Code is well-commented

Code Quality:
  [ ] Follows PEP 8 guidelines
  [ ] Proper naming conventions
  [ ] No code duplication

================================================================================
END OF README
================================================================================
