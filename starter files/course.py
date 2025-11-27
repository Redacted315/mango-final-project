"""
Course Class - Course Registration System
==========================================

TEAM MEMBER ASSIGNED TO THIS CLASS:
Name: _______________________
Student ID: _________________
Date Completed: _____________

PURPOSE:
Represents a single course in the system with course information,
instructor details, and capacity limits.

RESPONSIBILITIES:
- Store course information (code, name, instructor, credits, capacity)
- Provide access to course data through properties
- Format course information for display and file storage
- Track enrollment count
- Validate course data

DATA FILE FORMAT (courses.csv):
course_code,course_name,instructor,credits,capacity
CPRG216,Python Programming,Dr. Anderson,3,30

"""


class Course:
    def __init__(self, course_code=None, course_name=None, instructor=None,
                 credits=None, capacity=None):
        """
        Initialize a Course object.

        Parameters:
            course_code (str): Unique course code (e.g., "CPRG216")
            course_name (str): Full name of the course
            instructor (str): Name of the instructor
            credits (int): Number of credits (1-4)
            capacity (int): Maximum number of students

        Implementation Notes:
        - Use private attributes (prefix with _)
        - Initialize _enrolled_count to 0

        Author: [Your Name]
        Date: [Date]
        Version: 1.0
        """
        # TODO: Initialize private attributes
        # TODO: Initialize _enrolled_count to 0
        pass

    @property
    def course_code(self):
        """
        Get the course code.

        Returns:
            str: The course code (e.g., "CPRG216")

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return private course_code attribute
        pass

    @course_code.setter
    def course_code(self, value):
        """
        Set the course code.

        Parameters:
            value (str): New course code (should be uppercase)

        Implementation Notes:
        - Convert to uppercase if not already

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Convert to uppercase and set private course_code attribute
        pass

    @property
    def course_name(self):
        """
        Get the course name.

        Returns:
            str: Full name of the course

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return private course_name attribute
        pass

    @course_name.setter
    def course_name(self, value):
        """
        Set the course name.

        Parameters:
            value (str): New course name

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Set private course_name attribute
        pass

    @property
    def instructor(self):
        """
        Get the instructor name.

        Returns:
            str: Name of the instructor

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return private instructor attribute
        pass

    @instructor.setter
    def instructor(self, value):
        """
        Set the instructor name.

        Parameters:
            value (str): New instructor name

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Set private instructor attribute
        pass

    @property
    def credits(self):
        """
        Get the number of credits.

        Returns:
            int: Number of credits (1-4)

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return private credits attribute
        pass

    @credits.setter
    def credits(self, value):
        """
        Set the number of credits.

        Parameters:
            value (int): Number of credits (1-4)

        Raises:
            ValueError: If credits not between 1 and 4

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Validate (1-4) and set private credits attribute
        pass

    @property
    def capacity(self):
        """
        Get the course capacity.

        Returns:
            int: Maximum number of students

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return private capacity attribute
        pass

    @capacity.setter
    def capacity(self, value):
        """
        Set the course capacity.

        Parameters:
            value (int): New maximum capacity

        Raises:
            ValueError: If capacity is negative

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Validate (>= 0) and set private capacity attribute
        pass

    @property
    def enrolled_count(self):
        """
        Get the number of students currently enrolled.

        Returns:
            int: Current enrollment count

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return private enrolled_count attribute
        pass

    def set_enrolled_count(self, count):
        """
        Set the current enrollment count.

        Used by EnrollmentManager to update enrollment numbers.

        Parameters:
            count (int): New enrollment count

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Set private enrolled_count attribute
        pass

    def is_full(self):
        """
        Check if the course is at capacity.

        Returns:
            bool: True if enrolled_count >= capacity, False otherwise

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return True if course is full, False otherwise
        pass

    def get_available_seats(self):
        """
        Get the number of available seats in the course.

        Returns:
            int: Number of seats remaining (capacity - enrolled_count)

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Calculate and return available seats
        pass

    def __str__(self):
        """
        Return a formatted string representation of the course.

        Format:
        "[CODE] {course_name} - {instructor} ({credits} credits) [{enrolled}/{capacity} enrolled]"

        Example:
        "[CPRG216] Python Programming - Dr. Anderson (3 credits) [12/30 enrolled]"

        Returns:
            str: Formatted course information

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return formatted string as specified above
        pass

    def to_csv_format(self):
        """
        Format course data for CSV file storage.

        Returns comma-separated values matching the CSV header:
        course_code,course_name,instructor,credits,capacity

        Example:
        "CPRG216,Python Programming,Dr. Anderson,3,30"

        Returns:
            str: CSV-formatted string

        Author: [Your Name]
        Date: [Date]
        """
        # TODO: Return CSV formatted string (comma-separated values)
        pass


# ==============================================================================
# TESTING CODE (Do not modify)
# ==============================================================================

def test_course_class():
    """Test the Course class implementation."""
    print("=" * 70)
    print("TESTING COURSE CLASS")
    print("=" * 70)
    print()

    # Test 1: Create course with all parameters
    print("Test 1: Creating course with all parameters...")
    c1 = Course("CPRG216", "Python Programming", "Dr. Anderson", 3, 30)
    print(f"✓ Course created: {c1}")
    print()

    # Test 2: Test property access
    print("Test 2: Testing property access...")
    print(f"  Course Code: {c1.course_code}")
    print(f"  Course Name: {c1.course_name}")
    print(f"  Instructor: {c1.instructor}")
    print(f"  Credits: {c1.credits}")
    print(f"  Capacity: {c1.capacity}")
    print(f"  Enrolled: {c1.enrolled_count}")
    print()

    # Test 3: Test enrollment tracking
    print("Test 3: Testing enrollment tracking...")
    c1.set_enrolled_count(12)
    print(f"  Enrolled Count: {c1.enrolled_count}")
    print(f"  Available Seats: {c1.get_available_seats()}")
    print(f"  Is Full? {c1.is_full()}")
    print()

    # Test 4: Test full capacity
    print("Test 4: Testing full capacity...")
    c1.set_enrolled_count(30)
    print(f"  Enrolled Count: {c1.enrolled_count}")
    print(f"  Available Seats: {c1.get_available_seats()}")
    print(f"  Is Full? {c1.is_full()}")
    print()

    # Test 5: Test CSV format
    print("Test 5: Testing CSV format...")
    c2 = Course("DMIT1508", "Database Fundamentals", "Dr. Kim", 3, 35)
    print(f"  CSV: {c2.to_csv_format()}")
    print()


if __name__ == "__main__":
    test_course_class()


# ==============================================================================
# GRADING RUBRIC
# ==============================================================================
"""
COURSE CLASS RUBRIC (20 points total)

1. Constructor (__init__) - 3 points
   [3] All attributes initialized correctly including enrolled_count
   [2] Most attributes initialized, minor issues
   [1] Constructor exists but major issues
   [0] Constructor not implemented or doesn't work

2. Properties (Getters) - 4 points
   [4] All 6 properties implemented correctly (course_code, course_name, instructor, credits, capacity, enrolled_count)
   [3] 5 properties working correctly
   [2] 3-4 properties working correctly
   [1] 1-2 properties working
   [0] No working properties

3. Properties (Setters) - 4 points
   [4] All 5 setters implemented with appropriate validation
   [3] 4 setters working correctly
   [2] 2-3 setters working correctly
   [1] 1 setter working
   [0] No working setters

4. Enrollment Methods - 3 points
   [3] is_full() and get_available_seats() work correctly
   [2] Both implemented but minor issues
   [1] One method working
   [0] Not implemented or doesn't work

5. __str__ Method - 2 points
   [2] Returns properly formatted string exactly as specified
   [1] Returns string but format issues
   [0] Not implemented or doesn't work

6. to_csv_format() Method - 2 points
   [2] Returns properly formatted CSV string matching file format
   [1] Returns CSV but format issues
   [0] Not implemented or doesn't work

7. Documentation - 2 points
   [2] All methods have complete docstrings with author/date
   [1] Most methods documented
   [0] Missing or incomplete documentation

TOTAL: ___ / 20 points

NOTES:
"""
