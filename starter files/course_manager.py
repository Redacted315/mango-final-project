"""
CourseManager Class - Course Registration System
=================================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Name: _______________________
Student ID: _________________
Date Completed: _____________

PURPOSE:
Manages the collection of all courses in the system. Handles loading/saving
course data from/to CSV file and provides CRUD operations for courses.

RESPONSIBILITIES:
- Load course data from courses.csv file
- Save course data back to courses.csv file
- Add new courses to the system
- Remove courses from the system
- Search for courses by code or name
- Display course information
- Edit existing course information
- Update enrollment counts

FILE DEPENDENCIES:
- courses.csv (data file)
- course.py (Course class)
- enrollments.csv (to count enrollments)

"""

from course import Course


class CourseManager:
    def __init__(self):
        """
        Initialize the CourseManager.

        Creates an empty list of courses and loads data from courses.csv file.

        Implementation Notes:
        - Initialize empty _courses list (private attribute)
        - Call read_courses_file() to load existing data

        Author: [Your Name]
        Date: [Date]
        Version: 1.0
        """
        # TODO: Initialize _courses as empty list
        # TODO: Call read_courses_file()
        pass

    @property
    def courses(self):
        """
        Get the list of all courses.

        Returns:
            list: List of Course objects

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return private _courses list
        pass

    def read_courses_file(self):
        """
        Read course data from courses.csv and populate the courses list.

        File Format:
        course_code,course_name,instructor,credits,capacity

        Implementation Notes:
        - Open courses.csv for reading
        - Skip the header line
        - For each data line, split by comma and create Course object
        - Add each Course to _courses list
        - Handle FileNotFoundError if file doesn't exist

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Implement file reading
        # Hint: Use try/except for FileNotFoundError
        # Hint: Convert credits and capacity to int
        pass

    def write_courses_to_file(self):
        """
        Write all course data to courses.csv file.

        Writes header line followed by all courses in CSV format.

        Implementation Notes:
        - Open courses.csv for writing (will overwrite existing)
        - Write header: "course_code,course_name,instructor,credits,capacity"
        - For each course, write their to_csv_format() output

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Implement file writing
        pass

    def add_course(self):
        """
        Add a new course to the system through user input.

        Prompts:
        - Enter course code (e.g., CPRG216):
        - Enter course name:
        - Enter instructor name:
        - Enter number of credits (1-4):
        - Enter course capacity:

        Implementation Notes:
        - Check if course code already exists before adding
        - Convert credits and capacity to int
        - Add course to _courses list
        - Call write_courses_to_file() to save
        - Print confirmation or error message

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get input from user
        # TODO: Check for duplicate course code
        # TODO: Create new Course object
        # TODO: Add to _courses list
        # TODO: Save to file
        pass

    def remove_course(self):
        """
        Remove a course from the system by course code.

        Prompts:
        - Enter course code to remove:

        Outputs:
        - If found: "Course [CODE] - [NAME] removed successfully."
        - If not found: "Error: No course found with code [CODE]"

        Implementation Notes:
        - Search _courses list for matching course_code
        - If found, remove from list and save to file
        - If not found, display error message

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get course code from user
        # TODO: Search for course in _courses list
        # TODO: Remove if found, save file
        # TODO: Display appropriate message
        pass

    def search_course_by_code(self):
        """
        Search for a course by its code and display its information.

        Prompts:
        - Enter course code to search:

        Outputs:
        - If found: Display course using display_course_info()
        - If not found: "Error: No course found with code [CODE]"

        Returns:
            Course or None: The found Course object, or None if not found

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get course code from user (convert to uppercase)
        # TODO: Search _courses list for matching course_code
        # TODO: If found, call display_course_info() and return course
        # TODO: If not found, display error and return None
        pass

    def search_courses_by_name(self):
        """
        Search for courses by name and display results.

        Searches for partial matches in course names (case-insensitive).

        Prompts:
        - Enter course name to search:

        Outputs:
        - If found: Display all matching courses
        - If not found: "No courses found matching '[name]'"

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get search term from user
        # TODO: Search _courses for matches in course_name
        # TODO: Display results or error message
        pass

    def edit_course_info(self):
        """
        Edit an existing course's information.

        Prompts:
        - Enter course code to edit:
        - Enter new course name (or press Enter to skip):
        - Enter new instructor (or press Enter to skip):
        - Enter new credits 1-4 (or press Enter to skip):
        - Enter new capacity (or press Enter to skip):

        Outputs:
        - If found: "Course [CODE] updated successfully!"
        - If not found: "Error: No course found with code [CODE]"

        Implementation Notes:
        - Only update fields where user provides input
        - Save to file after successful edit

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Get course code from user
        # TODO: Find course in _courses list
        # TODO: For each attribute, prompt for new value
        # TODO: Update only if user enters something
        # TODO: Save to file
        pass

    def display_course_info(self, course):
        """
        Display detailed information for a single course.

        Format:
        ==========================================
        COURSE INFORMATION
        ==========================================
        Course Code:  [code]
        Course Name:  [name]
        Instructor:   [instructor]
        Credits:      [credits]
        Capacity:     [capacity]
        Enrolled:     [enrolled_count]
        Available:    [available seats]
        Status:       [Full/Available]
        ==========================================

        Parameters:
            course (Course): The course object to display

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Print formatted course information as shown above
        # Hint: Use course.is_full() to determine status
        pass

    def display_courses_list(self):
        """
        Display all courses in a formatted table.

        Format:
        ============================================================================================
        COURSE LIST
        ============================================================================================
        Code      Course Name                  Instructor        Credits  Enrolled  Capacity  Status
        --------------------------------------------------------------------------------------------
        CPRG216   Python Programming           Dr. Anderson      3        12        30        Open
        CPRG251   OOP Programming              Prof. Martinez    4        25        25        Full
        ============================================================================================
        Total Courses: [count]

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Print header
        # TODO: Loop through _courses and print each in table format
        # TODO: Print total count
        pass

    def get_course_count(self):
        """
        Get the total number of courses in the system.

        Returns:
            int: Number of courses

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return length of _courses list
        pass

    def find_course_by_code(self, course_code):
        """
        Find and return a course by its code (helper method for other classes).

        Parameters:
            course_code (str): The course code to search for

        Returns:
            Course or None: The Course object if found, None otherwise

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Search _courses list for matching course_code (case-insensitive)
        # TODO: Return Course object if found, None otherwise
        pass

    def update_enrollment_counts(self, enrollment_manager):
        """
        Update enrollment counts for all courses based on actual enrollments.

        Parameters:
            enrollment_manager: EnrollmentManager object to get enrollment data

        Implementation Notes:
        - For each course, count how many enrollments exist
        - Call course.set_enrolled_count() with the count

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: For each course in _courses
        # TODO: Count enrollments for that course
        # TODO: Update course's enrolled_count
        pass


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_course_manager():
    """Test the CourseManager class implementation."""
    print("=" * 70)
    print("TESTING COURSE MANAGER CLASS")
    print("=" * 70)
    print()

    # Test 1: Initialize and load data
    print("Test 1: Initialize CourseManager...")
    manager = CourseManager()
    print(f"✓ Manager created")
    print(f"  Courses loaded: {manager.get_course_count()}")
    print()

    # Test 2: Display all courses
    print("Test 2: Display all courses...")
    manager.display_courses_list()
    print()

    # Test 3: Find course by code
    print("Test 3: Find course by code...")
    course = manager.find_course_by_code("CPRG216")
    if course:
        print(f"✓ Found: {course}")
        manager.display_course_info(course)
    print()


if __name__ == "__main__":
    test_course_manager()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
COURSE MANAGER CLASS RUBRIC (20 points total)

1. Constructor and File Loading - 4 points
   [4] Correctly initializes list and loads from file with error handling
   [3] Loads data but minor issues
   [2] Loads data but significant issues
   [1] Constructor exists but doesn't load properly
   [0] Not implemented or doesn't work

2. File Writing - 2 points
   [2] Correctly writes all courses to CSV file
   [1] Writes to file but format issues
   [0] Not implemented or doesn't work

3. Add Course Method - 3 points
   [3] Prompts for all info, checks duplicates, adds to list, saves
   [2] Works but missing some functionality
   [1] Partially working
   [0] Not implemented

4. Remove Course Method - 2 points
   [2] Finds course, removes, saves, appropriate messages
   [1] Works but issues
   [0] Not implemented

5. Search Methods - 3 points
   [3] Both search methods work correctly
   [2] Both work but minor issues
   [1] One works correctly
   [0] Not implemented

6. Edit Course Method - 2 points
   [2] Allows editing all fields, handles empty input, saves
   [1] Works but issues
   [0] Not implemented

7. Display Methods - 2 points
   [2] Both display methods format correctly
   [1] Display works but formatting issues
   [0] Not implemented

8. Helper Methods - 2 points
   [2] find_course_by_code() and update_enrollment_counts() work
   [1] One method works
   [0] Not implemented

TOTAL: ___ / 20 points

NOTES:
"""
