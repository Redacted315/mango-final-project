# Course Registration System - Group Project Assignment

**Course:** CPRG216 - Python Programming
**Assignment Type:** Group Project
**Team Size:** 5 Students
**Total Points:** 100 points (20 points per student)
**Duration:** 2 weeks + video walkthrough

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Quick Start for Students](#quick-start-for-students)
3. [Team Organization](#team-organization)
4. [Grading Model](#grading-model)
5. [Component Specifications](#component-specifications)
6. [Peer Review Requirements](#peer-review-requirements)
7. [Timeline & Milestones](#timeline--milestones)
8. [Submission Requirements](#submission-requirements)
9. [Video Walkthrough Guide](#video-walkthrough-guide)
10. [Tips for Success](#tips-for-success)
11. [Instructor Grading Guide](#instructor-grading-guide)

---

## Project Overview

### What You're Building

A **Course Registration System** that manages students, courses, and enrollments - similar to the system you use to register for classes!

**Core Features:**
- Add, edit, remove, and search students
- Manage course catalog
- Register students in courses
- Track grades and generate reports
- Store all data in CSV files
- Menu-driven interface

### Why This Project?

Learn practical software engineering:
- Object-oriented programming (classes, properties)
- File I/O (reading/writing CSV files)
- Code organization and integration
- Quality assurance through code review
- Team collaboration

### System Requirements

**Technical:**
- Python 3.x (no external libraries needed)
- Only use concepts from Modules 1-4
- CSV files for data storage

**Functional:**
- Student management (CRUD operations)
- Course management (CRUD operations)
- Enrollment system with validation
- Reports and statistics
- Error handling and validation

---

## Quick Start for Students

### What You Need to Know Right Away

**Your Responsibilities:**
1. **Write ONE component** (25% of your grade)
2. **Review ONE component** (50% of your grade) ← **Most Important!**
3. **Help team integrate** (25% of your grade)

**Timeline:**
- **Week 1:** Build your component (Due: December 4)
- **Week 2:** Peer review, integration, fixes (Due: December 11)
- **Video Walkthrough:** December 15 (15 minutes per team)

**Critical Success Factor:**
Your grade depends MORE on reviewing well than coding well. Take code review seriously!

### First Steps (Today - End of Class)

1. **Form your team** (5 people)
2. **Choose team name/number**
3. **Assign components** - decide who codes what:
   - Person 1: Student Class
   - Person 2: StudentManager Class
   - Person 3: Course Class & CourseManager
   - Person 4: EnrollmentManager Class
   - Person 5: Main Application
4. **Set up communication** (group chat, meeting times)
5. **Complete Team Registration Form** (submit to instructor by end of class)
6. **Download all files** from the assignment folder
7. **Start coding** your assigned component

**IMPORTANT:** Reviewer assignments will be randomized and announced December 5.

### Files You'll Work With

**Data Files (provided):**
- `students.csv` - Sample student data
- `courses.csv` - Sample course data
- `enrollments.csv` - Sample enrollment data

**Code Files (you complete these):**
- `student.py` - Student class template
- `student_manager.py` - Student manager template
- `course.py` - Course class template
- `course_manager.py` - Course manager template
- `enrollment_manager.py` - Enrollment manager template
- `main.py` - Main application template

**Forms:**
- This document (ASSIGNMENT.md)
- README_TEMPLATE.txt (for final submission)

---

## Team Organization

### Component Assignment

Each team member is responsible for ONE component:

| Component | Files | Primary Responsibility | Difficulty |
|-----------|-------|----------------------|------------|
| **1. Student Class** | `student.py` | Data model for students | Beginner |
| **2. StudentManager** | `student_manager.py` | Student CRUD operations | Intermediate |
| **3. Course + CourseManager** | `course.py`, `course_manager.py` | Course operations | Intermediate |
| **4. EnrollmentManager** | `enrollment_manager.py` | Registration system | Advanced |
| **5. Main Application** | `main.py` | Menu system & integration | Advanced |

### Review Assignment

**Review assignments will be RANDOMIZED by the instructor.**

**Why random?**
- Prevents coordination or collusion between developer and reviewer
- Ensures independent, unbiased reviews
- Mirrors real-world code review where you don't choose your reviewer
- Creates fair, objective assessment process

**Timeline:**
1. **Today (class time):** Teams choose which member codes which component
2. **Submit:** Team registration form to instructor by end of class
3. **Next week:** Instructor randomly assigns reviewers (announced December 5)
4. **December 5-11:** Conduct assigned reviews

**You will NOT know who is reviewing your code until after Part 1 is submitted.**

This ensures you write the best code possible, not code that you think will "pass" a friendly review.

### Filling In Your Name

At the top of your assigned file, fill in:

```python
"""
TEAM MEMBER ASSIGNED TO THIS CLASS:
Name: Your Name Here
Student ID: 123456789
Date Completed: 2024-11-27
"""
```

---

## Grading Model

### Your 20 Points Breakdown

| Component | Weight | Points | What This Means |
|-----------|--------|--------|-----------------|
| **Code You Wrote** | 25% | 5 pts | Your component implementation |
| **Code You Reviewed** | 50% | 10 pts | QA responsibility for another component |
| **Team Integration** | 25% | 5 pts | Complete system quality |
| **TOTAL** | 100% | 20 pts | |

### Why Review Is Worth 50%

**In professional software development:**
- Code reviews catch 60-90% of bugs before production
- Reviewers are held accountable for bugs that slip through
- Senior engineers spend MORE time reviewing than coding
- Quality assurance is MORE valuable than code generation

**If you approve broken code, YOU are responsible when it fails in integration.**

This teaches real-world accountability.

### Part 1: Code You Wrote (5 points / 25%)

**What:** Build your assigned component

**Grading:**
- **5 pts:** Fully functional, well-documented, all methods work
- **4 pts:** Mostly working, minor bugs, good documentation
- **3 pts:** Core features work, some bugs, acceptable docs
- **2 pts:** Partial implementation, many bugs, poor docs
- **1 pt:** Minimal work, mostly broken
- **0 pts:** Not submitted or non-functional

### Part 2: Code You Reviewed (10 points / 50%)

**What:** Quality assurance for assigned component

**Your Duties as Reviewer:**
1. Test thoroughly (run all test cases, try to break it)
2. Verify functionality (check against specifications)
3. Check code quality (style, documentation, best practices)
4. Grade using embedded rubric (be fair and accurate)
5. Provide feedback (specific, actionable improvements)
6. Follow up (verify fixes were made)
7. Sign off (approve for integration or require revisions)

**Grading:**
- **9-10 pts:** Caught all major bugs, thorough testing, accurate assessment, verified fixes, component works perfectly
- **7-8 pts:** Caught most bugs, useful feedback, mostly accurate assessment, component mostly works
- **5-6 pts:** Caught some bugs, basic feedback, questionable assessment, component has issues
- **3-4 pts:** Missed obvious bugs, vague feedback, inaccurate assessment, component fails
- **0-2 pts:** Approved broken code, no testing, no useful feedback, complete failure

**Critical:** If the code you approved has bugs in the final project, YOUR review score drops. You are accountable.

### Part 3: Team Integration (5 points / 25%)

**What:** Complete integrated system quality

**Shared by all team members:**
- **5 pts:** All components integrate seamlessly, everything works
- **4 pts:** Minor integration issues, mostly works
- **3 pts:** Some integration problems, core features work
- **2 pts:** Poor integration, many errors
- **0-1 pts:** Doesn't integrate, doesn't run

### Example Scenarios

**Scenario A: Great Code, Poor Review**
- Code Written: 5/5 (excellent)
- Code Reviewed: 4/10 (missed bugs in component you reviewed)
- Team Quality: 3/5 (bugs caused integration issues)
- **Total: 12/20 (60%) - Fail**

**Lesson:** Writing good code isn't enough. Review seriously.

**Scenario B: Okay Code, Excellent Review**
- Code Written: 3/5 (acceptable but buggy)
- Code Reviewed: 10/10 (caught all bugs, excellent QA)
- Team Quality: 5/5 (system works great)
- **Total: 18/20 (90%) - A**

**Lesson:** Excellent review work compensates for mediocre coding.

---

## Component Specifications

### Component 1: Student Class (student.py)

**Assigned to:** `[Team Member Name]`
**Difficulty:** Beginner
**Estimated Time:** 4-5 hours

#### Purpose
Represents a single student with their personal and academic information.

#### Attributes (Private)
- `student_id` (int): 10-digit unique identifier
- `first_name` (str): First name
- `last_name` (str): Last name
- `email` (str): Email address
- `program` (str): Academic program
- `year` (int): Current year (1-4)

#### Required Methods
- `__init__()`: Constructor, auto-generate ID if None
- Properties (getters/setters) for all 6 attributes
- `__str__()`: Formatted display string
- `to_csv_format()`: Return CSV-formatted string
- `get_full_name()`: Return "First Last"

#### Validation Requirements
- Student ID must be 10 digits
- Year must be between 1 and 4
- Auto-generate random 10-digit ID (2023000000 - 2023999999) if not provided

#### Grading Rubric (5 points)
- Constructor: 1.0 point
- Properties (getters/setters): 2.0 points
- Methods (__str__, to_csv_format, get_full_name): 1.5 points
- Documentation: 0.5 points

---

### Component 2: StudentManager Class (student_manager.py)

**Assigned to:** `[Team Member Name]`
**Difficulty:** Intermediate
**Estimated Time:** 5-6 hours

#### Purpose
Manages the collection of all students. Handles loading/saving data and CRUD operations.

#### Required Methods
- `__init__()`: Initialize and load from file
- `read_students_file()`: Load from students.csv
- `write_students_to_file()`: Save to students.csv
- `add_student()`: Add new student via user input
- `remove_student()`: Remove student by ID
- `search_student_by_id()`: Find and display student
- `search_student_by_name()`: Find by name (partial match, case-insensitive)
- `edit_student_info()`: Update student information
- `display_student_info()`: Show single student details
- `display_students_list()`: Show all students in table format
- `find_student_by_id()`: Helper method for other classes

#### Key Features
- File I/O with error handling (FileNotFoundError)
- Search functions handle "not found" gracefully
- Display methods format data in readable tables
- Edit allows partial updates (skip fields)

#### Grading Rubric (5 points)
- File I/O: 1.0 point
- Add/Remove: 1.5 points
- Search methods: 1.0 point
- Edit: 0.5 points
- Display methods: 0.5 points
- Documentation: 0.5 points

---

### Component 3: Course Class & CourseManager (course.py, course_manager.py)

**Assigned to:** `[Team Member Name]`
**Difficulty:** Intermediate
**Estimated Time:** 6-7 hours (2 files)

#### Course Class (course.py)

**Attributes:**
- `course_code` (str): Unique code (e.g., "CPRG216")
- `course_name` (str): Full name
- `instructor` (str): Instructor name
- `credits` (int): Number of credits (1-4)
- `capacity` (int): Maximum students
- `enrolled_count` (int): Current enrollment

**Methods:**
- `__init__()`: Constructor
- Properties for all 6 attributes
- `is_full()`: Check if at capacity
- `get_available_seats()`: Return open spots
- `__str__()`: Formatted display
- `to_csv_format()`: CSV string

#### CourseManager Class (course_manager.py)

**Similar to StudentManager but for courses:**
- CRUD operations
- File I/O for courses.csv
- Search by code and name
- Update enrollment counts
- Display methods

#### Grading Rubric (5 points)
- Course class: 2.0 points
- CourseManager: 2.5 points
- Documentation: 0.5 points

---

### Component 4: EnrollmentManager Class (enrollment_manager.py)

**Assigned to:** `[Team Member Name]`
**Difficulty:** Advanced
**Estimated Time:** 7-8 hours

#### Purpose
Manages the relationship between students and courses. Most complex component.

#### Key Responsibilities
- Register student in course (with validation!)
- Drop student from course
- Display student's schedule
- Display course roster
- Assign/update grades
- Track enrollment counts

#### Critical Validation
When registering, must check:
- ✓ Student exists in system
- ✓ Course exists in system
- ✓ Course is not full
- ✓ Student not already enrolled in course

If any check fails, display error and don't register.

#### Data Structure
Each enrollment is a dictionary:
```python
{
    'student_id': 2023047891,
    'course_code': 'CPRG216',
    'semester': 'Fall2024',
    'grade': ''  # Empty until assigned
}
```

#### Integration Points
- Works with StudentManager to validate students
- Works with CourseManager to validate courses and update counts
- Must be initialized with references to both managers

#### Grading Rubric (5 points)
- File I/O: 0.5 points
- Register with validation: 2.0 points
- Drop student: 0.5 points
- Display schedule/roster: 1.0 point
- Assign grade: 0.5 points
- Documentation: 0.5 points

---

### Component 5: Main Application (main.py)

**Assigned to:** `[Team Member Name]`
**Difficulty:** Advanced
**Estimated Time:** 6-7 hours

#### Purpose
Ties everything together with menu-based interface. This person leads integration.

#### Required Menus

**Main Menu:**
1. Student Management →
2. Course Management →
3. Enrollment Management →
4. Reports →
5. Exit Program

**Student Management Submenu:**
1. Display all students
2. Search student by ID
3. Search student by name
4. Add new student
5. Edit student information
6. Remove student
7. Return to main menu

**Course Management Submenu:**
1. Display all courses
2. Search course by code
3. Search courses by name
4. Add new course
5. Edit course information
6. Remove course
7. Return to main menu

**Enrollment Management Submenu:**
1. Register student in course
2. Drop student from course
3. Display student schedule
4. Display course roster
5. Assign grade
6. Return to main menu

**Reports Submenu:**
1. All enrollments
2. System statistics
3. Return to main menu

#### System Statistics
Must display:
- Total students
- Total courses
- Total enrollments
- Average students per course
- Course with highest enrollment

#### Grading Rubric (5 points)
- System initialization: 0.5 points
- Main menu: 0.5 points
- Student menu: 1.0 point
- Course menu: 1.0 point
- Enrollment menu: 1.0 point
- Reports menu: 1.0 point
- User experience/error handling: 0.5 points

---

## Peer Review Requirements

### Overview

Peer review is **MANDATORY** and worth **50% of your grade**.

### Your Review Responsibilities

As the assigned reviewer for a component, you are the **Quality Assurance Lead**.

**Your job:**
1. **Test exhaustively** - Run all test cases, try to break it
2. **Check specifications** - Verify all requirements met
3. **Review code quality** - Check style, documentation, readability
4. **Use the rubric** - Grade fairly using embedded rubric
5. **Provide feedback** - Specific, actionable improvements
6. **Verify fixes** - Ensure author addressed issues
7. **Sign off** - Approve for integration or request revisions

### Review Form

Use this format (can be text file or markdown):

```
==============================================================================
PEER REVIEW FORM
==============================================================================

COMPONENT: [Component Name]
FILE(S): [Filename(s)]

AUTHOR: [Name]
REVIEWER: [Your Name]
DATE REVIEWED: [Date]

==============================================================================
TESTING PERFORMED
==============================================================================

Test 1: [Description]
Expected: [Result]
Actual: [Result]
Status: PASS/FAIL

Test 2: [Description]
Expected: [Result]
Actual: [Result]
Status: PASS/FAIL

[Add more test cases]

==============================================================================
BUGS FOUND
==============================================================================

Bug #1 (Severity: High/Med/Low):
Description: [Specific description]
Location: [Line number or method name]
How to reproduce: [Steps]

[List all bugs found]

==============================================================================
CODE QUALITY ASSESSMENT
==============================================================================

✓ = Good, ~ = Needs Improvement, ✗ = Poor

[✓] Code runs without errors
[✓] All required methods implemented
[~] Methods work as specified (see bugs above)
[✓] Input validation present
[✓] Error handling present
[✓] File I/O works correctly
[✓] Code follows PEP 8
[✓] Variable names meaningful
[✓] Proper indentation
[~] Comments explain complex logic
[✓] No unnecessary duplication
[✓] Author name/ID filled in
[✓] All methods have docstrings
[✓] Docstrings include author/date

==============================================================================
RUBRIC ASSESSMENT
==============================================================================

Using the embedded rubric in the code file:

Category 1: [Name]
Points Possible: X
Points Earned: Y
Notes: [Why this score]

[Grade all categories]

TOTAL: ____ / 5 points

==============================================================================
OVERALL ASSESSMENT
==============================================================================

Status:
[ ] APPROVED - Ready for integration
[ ] APPROVED WITH MINOR ISSUES - Works but needs small fixes
[ ] NEEDS REVISION - Significant issues must be addressed
[ ] NOT FUNCTIONAL - Major rework required

==============================================================================
FEEDBACK FOR AUTHOR
==============================================================================

What Works Well:
1. [Specific positive feedback]
2. [Specific positive feedback]
3. [Specific positive feedback]

Issues to Fix (REQUIRED):
1. [Specific issue and how to fix it]
2. [Specific issue and how to fix it]

Suggestions for Improvement (OPTIONAL):
1. [Suggestion]
2. [Suggestion]

==============================================================================
AUTHOR RESPONSE
==============================================================================

AUTHOR: [Name]
DATE: [Date]

Changes Made:
1. [What you fixed]
2. [What you fixed]

Questions/Clarifications:
[Any questions for reviewer]

==============================================================================
SIGN-OFF
==============================================================================

Reviewer: __________________ Date: __________
(I certify this review was conducted thoroughly)

Author: ____________________ Date: __________
(I acknowledge receipt and have addressed issues)
```

### What Makes a Good Review

**DO:**
- Test the code thoroughly (spend 3-4 hours)
- Point out specific bugs with line numbers
- Suggest concrete improvements
- Be constructive and respectful
- Check against the rubric
- Verify all fixes were made

**DON'T:**
- Just say "looks good" without testing
- Be vague ("it doesn't work")
- Be mean or disrespectful
- Fix the code for them (give guidance instead)
- Approve code you didn't test
- Ignore obvious problems

### Accountability

**If you approve broken code:**
- The component fails in integration
- Your review score drops significantly
- You lose points, not the author

**This is intentional.** In real software development, reviewers are held accountable for bugs that slip through.

---

## Timeline & Milestones

### Part 1: Component Development (Due December 4 in class)

**Week of November 25-29:**
- Form teams (5 students)
- Assign components and reviews
- Set up communication (group chat)
- Start coding your component

**Week of December 2-4:**
- Complete your assigned component
- Test using built-in test code
- Fill in your name/ID in file header
- Ensure component works independently

**Thursday, December 4 (IN CLASS):**
- **PART 1 DUE:** Bring your completed component to class
- Team collects all 5 components
- Person 5 begins initial integration
- **Submit to Brightspace:** Saturday, December 6 (integrated but unreviewed version)

### Part 2: Peer Review, Integration & Fixes (December 5-11)

**December 5-8 (Review Phase):**
- Each reviewer receives assigned component
- Conduct thorough testing and review
- Complete PEER_REVIEW_FORM.md
- Submit review to component author
- Use GitHub (optional) for tracking issues

**December 9-11 (Fix & Integration Phase):**
- Authors receive feedback
- Fix all identified issues
- Reviewers verify fixes
- Person 5 integrates fixed components
- Team tests complete system together
- Final bug fixes and testing

**Thursday, December 11 (IN CLASS):**
- **PART 2 DUE:** Present working integrated system
- All peer reviews completed and signed off
- All fixes verified and integrated
- **Submit to Brightspace:** Saturday, December 13 (final version with all reviews)

### Part 3: Video Walkthrough (Due December 15)

**December 12-14 (Record Video):**
- Team creates 15-minute demonstration video
- Follow VIDEO_WALKTHROUGH_GUIDE (see below)
- Show code and run comprehensive tests
- All team members participate

**Sunday, December 15:**
- **VIDEO DUE:** Submit video link/file to Brightspace
- Instructor reviews and grades

---

## Submission Requirements

### Submissions Required

This project has **TWO submissions** to Brightspace:

1. **Part 1 (December 6):** Integrated but unreviewed code
2. **Part 2 (December 13):** Final version with all reviews + video walkthrough

**Note:** Video can be submitted as part of Part 2 or separately by December 15.

### Part 1 Submission (Due: Saturday, December 6)

**What to Submit:**

**Folder structure:**
```
project_folder_part1/
├── students.csv
├── courses.csv
├── enrollments.csv
├── student.py
├── student_manager.py
├── course.py
├── course_manager.py
├── enrollment_manager.py
├── main.py
└── README.txt (partially filled)
```

**Requirements:**
- All 5 components integrated into working system
- Each file has team member name/ID filled in
- System runs without crashing
- Basic README with team member info
- **NOTE:** Peer reviews NOT required yet for Part 1

**Part 1 Checklist:**
- [ ] All 6 Python files included
- [ ] All 3 CSV files included
- [ ] All team members' names in their files
- [ ] Program runs (even if buggy)
- [ ] main.py integrates all components
- [ ] Basic README with names/components
- [ ] One person submits on Brightspace by Dec 6

### Part 2 Submission (Due: Friday, December 13)

**What to Submit:**

**Folder structure:**
```
project_folder_part2/
├── students.csv
├── courses.csv
├── enrollments.csv
├── student.py
├── student_manager.py
├── course.py
├── course_manager.py
├── enrollment_manager.py
├── main.py
├── review_student.md (or .txt)
├── review_student_manager.md
├── review_course.md
├── review_enrollment.md
├── review_main.md
└── README.txt (complete)
```

**Requirements:**
- All bugs from peer reviews fixed
- All 5 peer review forms completed and signed
- Fully functional integrated system
- Complete README with all sections
- System tested and verified by team

### README.txt Contents

Use README_TEMPLATE.txt and fill in:

```
Course Registration System - Team [Number]

TEAM MEMBERS:
1. [Name] (ID: [ID]) - Component: [Component] - Email: [Email]
2. [Name] (ID: [ID]) - Component: [Component] - Email: [Email]
3. [Name] (ID: [ID]) - Component: [Component] - Email: [Email]
4. [Name] (ID: [ID]) - Component: [Component] - Email: [Email]
5. [Name] (ID: [ID]) - Component: [Component] - Email: [Email]

REVIEW ASSIGNMENTS:
- [Component 1] reviewed by [Name]
- [Component 2] reviewed by [Name]
- [Component 3] reviewed by [Name]
- [Component 4] reviewed by [Name]
- [Component 5] reviewed by [Name]

HOW TO RUN:
1. Open terminal/command prompt
2. Navigate to project folder
3. Run: python main.py
4. Follow menu prompts

KNOWN ISSUES:
[List any known issues, or write "None"]

FEATURES COMPLETED:
[X] All student management features
[X] All course management features
[X] All enrollment features
[X] All reports
[X] Data persistence
[X] Error handling
```

**Part 2 Checklist:**
- [ ] All 6 Python files included (updated/fixed versions)
- [ ] All 3 CSV files included with sample data
- [ ] 5 peer review forms included (one per component)
- [ ] All reviews are complete, thorough, and signed
- [ ] README.txt fully completed
- [ ] All team members' names in their files
- [ ] Program runs without errors
- [ ] All menu options work correctly
- [ ] Data saves and loads correctly
- [ ] All bugs identified in reviews are fixed
- [ ] One person submits on Brightspace by Dec 13

### Part 3 Submission (Due: Sunday, December 15)

**What to Submit:**
- Video walkthrough link (YouTube unlisted, OneDrive, or direct upload)
- See "Video Walkthrough Guide" section below for complete requirements

**Submission:**
- Submit link or file to "Video Walkthrough" assignment on Brightspace
- Include team number and all member names in submission comments
- Deadline: Sunday, December 15, 2024, 11:59 PM

---

## Video Walkthrough Guide

### Overview

**Purpose:** Demonstrate your working system and prove all components function correctly.

**Duration:** 15 minutes maximum

**Participants:** All 5 team members

**Format:** Screen recording with audio narration (Zoom, OBS, QuickTime, etc.)

**Due Date:** December 15, 2024

**Submission:** Upload to YouTube (unlisted) or OneDrive and submit link to Brightspace

### Video Structure (15 minutes total)

Your video must include these sections in order:

#### 1. Team Introduction (1 minute)

**What to show:**
- Team name/number
- Each member introduces themselves: name, student ID, component assigned
- State review assignments (who reviewed what)

**Script example:**
```
"Hi, we're Team 5. I'm Alice, student ID 2023012345, and I built the Student Class.
I also reviewed Bob's StudentManager component..."
```

#### 2. Code Review (5 minutes)

**What to show:** Briefly show each Python file in your IDE/editor

**For EACH component, the assigned developer shows:**
- Open the file (student.py, student_manager.py, etc.)
- Point out their name/ID in the header comment
- Scroll through to show key methods (don't read line by line)
- Highlight one interesting piece of code or challenge solved
- Show any validation or error handling

**Example narration:**
```
"This is my StudentManager class. Here's the read_students_file method that loads
data from CSV. I added error handling here for when the file doesn't exist - it
creates a new empty list instead of crashing..."
```

**Timing:** ~1 minute per component

#### 3. Peer Review Evidence (2 minutes)

**What to show:**
- Open one or two completed PEER_REVIEW_FORM.md files
- Scroll through to show thoroughness (test cases, bugs found, feedback)
- Briefly discuss one bug that was caught and fixed

**Example narration:**
```
"Here's my review of the EnrollmentManager. I found 3 bugs during testing.
The most critical was that it didn't check if a course was full before
registering students. Diana fixed this and you'll see it working correctly
in our demonstration..."
```

#### 4. Live Demonstration (6 minutes)

**What to show:** Run `python main.py` and demonstrate ALL functionality

**REQUIRED TEST SEQUENCE:**

**A. Student Management (1.5 minutes)**
1. Display all students
2. Search student by ID (use existing: 2023047891)
3. Search student by name (partial match: "John")
4. Add new student (enter test data when prompted)
5. Display all students again (verify new student appears)
6. Edit student info (change year or program)
7. Remove student (remove the one you just added)

**B. Course Management (1.5 minutes)**
1. Display all courses
2. Search course by code (use existing: "CPRG216")
3. Add new course (enter test data)
4. Display all courses (verify new course appears)
5. Edit course (change capacity or instructor)
6. Remove course (remove the one you just added)

**C. Enrollment Management (2 minutes)**
1. Display all current enrollments
2. Register student in course:
   - Use existing student: 2023047891
   - Use existing course: DMIT1234
   - Enter semester: Fall2024
   - **Verify success message**
3. Display student schedule for that student (verify enrollment appears)
4. Display course roster for that course (verify student appears)
5. Assign grade to that enrollment (enter "A")
6. Display student schedule again (verify grade appears)
7. Drop student from course
8. Display enrollments again (verify it's removed)

**D. Error Handling Demonstrations (0.5 minutes)**

**Must test these failure scenarios:**
1. Try to register student in FULL course (should show error)
2. Try to register invalid student ID (should show error)
3. Try to register same student in same course twice (should show error)

**E. Reports (0.5 minutes)**
1. Display system statistics
2. Point out: total students, total courses, total enrollments
3. Show which course has highest enrollment

#### 5. Data Persistence Test (1 minute)

**What to show:**
1. Close/exit the program
2. Re-run `python main.py`
3. Display all students (verify data is still there)
4. Display enrollments (verify data persisted)
5. Explain: "All data saves to CSV files automatically"

### Technical Requirements

**Video Quality:**
- Screen resolution: 1280x720 minimum
- Audio: Clear voice, no background noise
- Recording: Screen + audio (no video of faces required)
- File format: MP4, MOV, or link to YouTube/OneDrive

**What to Record:**
- Your IDE/editor (for code review section)
- Terminal/command prompt (for demonstration)
- File explorer briefly (to show all files present)

**Tips:**
- Practice the demonstration first (do a dry run)
- Have test data ready
- If something breaks during recording, restart and re-record
- Edit out long pauses (keep it moving)

### Grading Criteria for Video

**Team Integration Component (5 points)** is partially based on video:

**5 points (Excellent):**
- All sections present and complete
- All required tests performed successfully
- Error handling works correctly
- Data persists correctly
- Professional presentation, clear audio
- All team members participate

**4 points (Good):**
- All sections present
- Most tests work
- Minor bugs or missing tests
- Acceptable presentation

**3 points (Acceptable):**
- Missing one section
- Some features don't work
- Poor audio or unprofessional

**2 points (Poor):**
- Missing multiple sections
- Many features broken
- Unclear demonstration

**0-1 points (Fail):**
- Video not submitted or less than 10 minutes
- System doesn't work
- Plagiarism detected

### Submission Instructions

**How to Submit:**

**Option 1: YouTube (Recommended)**
1. Upload video to YouTube
2. Set visibility to "Unlisted" (not public, not private)
3. Copy the link
4. Submit link to Brightspace in "Video Walkthrough" assignment

**Option 2: OneDrive/Google Drive**
1. Upload video file
2. Set sharing to "Anyone with link can view"
3. Copy the link
4. Submit link to Brightspace

**Option 3: Direct Upload**
1. If file is under 500MB, upload directly to Brightspace
2. Not recommended for large files (slow upload)

**Submission Details:**
- One submission per team
- Include team number and all member names in submission comments
- Double-check link works before submitting (test in incognito browser)

**Deadline:** Sunday, December 15, 2024, 11:59 PM

**Late Policy:** No extensions. Video must be submitted on time.

### Checklist Before Submitting Video

- [ ] Video is 10-15 minutes long (not shorter, not longer)
- [ ] All 5 team members introduce themselves
- [ ] All 6 Python files shown briefly
- [ ] All peer review forms mentioned/shown
- [ ] Complete demonstration of ALL menu options
- [ ] All required tests performed successfully
- [ ] Error handling demonstrated (full course, invalid ID, duplicate enrollment)
- [ ] System statistics shown
- [ ] Data persistence demonstrated (exit and restart)
- [ ] Audio is clear and understandable
- [ ] Video link works (tested in incognito browser)
- [ ] Link submitted to Brightspace before deadline

---

## Tips for Success

### For Everyone

**Start Early**
- Don't wait until December 11
- If you're stuck, ask early
- Office hours are your friend

**Communicate**
- Use group chat regularly
- Share progress updates
- Ask teammates for help

**Test Often**
- After every method, test it
- Don't wait until the end
- Use the built-in test code

**Document Everything**
- Add your name/date to docstrings
- Comment complex logic
- Keep review notes

### Component-Specific Tips

**Person 1 (Student Class):**
- Simplest component - finish early
- Your class is needed by Person 2
- Test auto-generated IDs thoroughly
- Validation is important

**Person 2 (StudentManager):**
- You need Person 1 done first
- File I/O is tricky - test carefully
- Search should handle "not found" gracefully
- Edit method should allow skipping fields

**Person 3 (Course + CourseManager):**
- Two files but similar to Person 1 & 2
- Enrollment count is tricky - coordinate with Person 4
- Test capacity limits carefully
- Course code should auto-uppercase

**Person 4 (EnrollmentManager):**
- Most complex component
- You need Person 1, 2, and 3 done
- Validation is CRITICAL - check everything
- Work closely with Person 3 on enrollment counts
- Test edge cases (full courses, duplicates)

**Person 5 (Main Application):**
- You're the integration lead
- Start planning menu structure early
- Test each menu option thoroughly
- Handle invalid input gracefully
- Make error messages helpful
- You need everyone else done first

### Review Tips

**Be Thorough**
- Spend 3-4 hours reviewing
- Test every method
- Try invalid inputs
- Check file I/O carefully

**Be Specific**
- "Method search_by_id() crashes when ID doesn't exist (line 47)"
- NOT "search doesn't work"

**Be Constructive**
- Suggest solutions, not just problems
- Acknowledge what works well
- Be respectful

**Be Accountable**
- You're responsible if you approve broken code
- Don't sign off unless you've tested thoroughly
- Verify fixes were actually made

---

## Instructor Grading Guide

### Grading Process

#### Step 1: Verify Submission (5 minutes)
- [ ] All files present
- [ ] README.txt complete
- [ ] 5 review forms included
- [ ] Names filled in files

#### Step 2: Test Complete System (10 minutes)
- Run `python main.py`
- Test each menu option
- Try invalid inputs
- Check data persistence
- Assign Team Integration score (5 pts all members)

#### Step 3: Grade Individual Components (15 minutes)

For each component:
1. Run test code at bottom of file
2. Check against specifications
3. Review documentation
4. Use embedded rubric
5. Assign Code Written score (5 pts)

#### Step 4: Assess Review Quality (10 minutes)

For each reviewer:
1. Read their review form
2. Compare to actual code quality
3. Check if they caught bugs
4. Evaluate feedback quality
5. Test if approved code works
6. Assign Code Reviewed score (10 pts)

### Total Time Per Team: ~40 minutes
### For 6 teams (30 students): ~4 hours

### Grading Rubric Summary

**Code Written (5 points):**
- 5: All features work, excellent quality
- 4: Mostly works, minor issues
- 3: Core features work, some bugs
- 2: Partial implementation
- 1: Minimal work
- 0: Not functional

**Code Reviewed (10 points):**
- 9-10: Excellent QA, caught all bugs, thorough testing
- 7-8: Good QA, caught most bugs
- 5-6: Acceptable QA, some bugs caught
- 3-4: Poor QA, missed obvious bugs
- 0-2: Failed QA, approved broken code

**Team Integration (5 points):**
- 5: Perfect integration, everything works
- 4: Minor issues
- 3: Some integration problems
- 2: Many problems
- 0-1: Doesn't work

### Red Flags

**Immediate point deductions:**
- Missing name/ID in file: -1 point
- No documentation: -2 points
- Fake review (didn't test): 0/10 review score
- Plagiarized code: 0 for entire project
- Missing files: Can't grade, 0 points

### Common Issues & Penalties

**Code Issues:**
- Crashes on invalid input: -1 point
- File I/O doesn't work: -2 points
- Missing required methods: -1 point each
- No validation: -1 point

**Review Issues:**
- Superficial review: 3-4/10 points
- Missed major bugs: -3 points
- Didn't verify fixes: -2 points
- Approved non-functional code: 0-2/10 points

### Grade Distribution

Expected distribution for well-defined assignments:
- A (18-20): 30-40% of students
- B (16-17): 30-40% of students
- C (14-15): 15-25% of students
- D (12-13): 5-10% of students
- F (<12): <5% of students

If entire team does well: All can get A's (not a curve).

### AI Detection

If using AI assistance:
- **Allowed:** Using AI to understand concepts, debug errors, explain code
- **Not Allowed:** Having AI write entire components, copy-paste AI code without understanding

**How to detect:**
- Code that's too advanced for modules covered
- Inconsistent style across methods
- Perfect code with no incremental commits
- Student can't explain their own code

**If suspected:** Ask student to explain code in person. Can't explain = 0 points.

---

## Non-Participating Team Members

### What If Someone Doesn't Do Their Work?

**This project is designed to be resilient to non-participating students.**

If a team member:
- Stops attending class
- Doesn't respond to team communications
- Fails to complete their component by December 4
- Withdraws from project participation

**The team can continue without penalty.**

### Solution Code for Missing Components

**If a teammate doesn't participate, the instructor can provide solution code.**

#### How It Works

1. **Team reports issue** (by December 4)
2. **Instructor verifies** non-participation
3. **Instructor provides solution file** for that component
4. **Team integrates** solution code into project
5. **Team documents** use of solution code in README

#### Grading Impact

**For the non-participating student:**
- Code Written: **0/5 points**
- Code Reviewed: **0/10 points** (if they don't participate in review either)
- Team Integration: **0/5 points** (if no participation)
- **Total: 0/20 (0%)**

**For the assigned reviewer** (who was supposed to review the missing component):
- Code Written: **Full points** (5/5 if they complete their own component)
- Code Reviewed: **0/10 points** (cannot earn review points for system-provided code)
- Team Integration: **Full points** (5/5 if team system works)
- **Impact:** Lower grade but not their fault

**For the rest of the team:**
- **No penalty**
- All other team members graded normally
- Team Integration score based on complete working system
- Can still earn full points if system works

#### Example Grading Scenario

**Team 3 - Alice doesn't participate:**
- Alice (non-participant): 0/20 (0%)
- Bob (was supposed to review Alice's component): Maximum 10/20 (50%) - lost 10 pts for review
- Charlie, Diana, Emma: Full grading 18-20/20 (90-100%) - no penalty

**Fairness:** Participating students aren't penalized for teammate's absence.

### Documenting System Code Usage

**In your README.txt, document:**

```
SYSTEM CODE USED:
- Component: [student_manager.py]
- Reason: [Original developer (Student Name) did not participate]
- Date provided: [December 5, 2024]
- Integrated by: [Team Member Name]
```

**In peer review form:**

```
COMPONENT: student_manager.py
AUTHOR: [Student Name - DID NOT PARTICIPATE]
REVIEWER: [Your Name]

REVIEW STATUS: SYSTEM-PROVIDED CODE
System code was used because original author did not attend class
or complete component by deadline. No review grade earned for this
component.
```

### Enhanced Docstring Format

**All methods must include development history and peer review dialogue.**

#### Required Format

```python
def method_name(self, parameters):
    """
    Brief description.

    Parameters:
        param (type): Description

    Returns:
        type: Description

    ---DEVELOPMENT HISTORY---
    AUTHOR: [Your Name]
    STUDENT ID: [Your ID]
    DATE WRITTEN: YYYY-MM-DD
    VERSION: 1.0

    ---PEER REVIEW---
    REVIEWER: [Reviewer Name]
    STUDENT ID: [Reviewer ID]
    DATE REVIEWED: YYYY-MM-DD

    REVIEW COMMENTS:
    - [Specific feedback on this method]
    - [Issues found during testing]
    - [Suggestions for improvement]

    DEVELOPER RESPONSE:
    - [How you addressed each comment]
    - [Changes made to code]
    - [Reasons if you disagreed with feedback]

    DATE FIXED: YYYY-MM-DD

    REVIEWER VERIFICATION:
    STATUS: [APPROVED / NEEDS MORE WORK]
    VERIFIED BY: [Reviewer Name]
    DATE: YYYY-MM-DD
    NOTES: [Final verification comments]
    """
    # Implementation here
    pass
```

#### Why This Format?

**Accountability Trail:**
- Proves both developer and reviewer participated
- Shows actual dialogue and problem-solving
- Documents fixes and verification
- Creates professional code review record

**Grading Evidence:**
- Instructor can see who did what
- Clear evidence of participation
- Shows quality of review feedback
- Demonstrates learning process

#### Example: Completed Method Documentation

```python
def add_student(self):
    """
    Add a new student to the system via user input.

    ---DEVELOPMENT HISTORY---
    AUTHOR: Bob Smith
    STUDENT ID: 2023045678
    DATE WRITTEN: 2024-12-02
    VERSION: 1.0

    ---PEER REVIEW---
    REVIEWER: Alice Johnson
    STUDENT ID: 2023012345
    DATE REVIEWED: 2024-12-05

    REVIEW COMMENTS:
    - Input validation missing: user could enter year=10
    - No email validation (should check for @)
    - Variable name 'yr' is unclear

    DEVELOPER RESPONSE:
    - Fixed: Added while loop to validate year is 1-4
    - Fixed: Added email validation for @ and .
    - Fixed: Renamed 'yr' to 'year'

    DATE FIXED: 2024-12-06

    REVIEWER VERIFICATION:
    STATUS: APPROVED
    VERIFIED BY: Alice Johnson
    DATE: 2024-12-07
    NOTES: All issues resolved. Validation works correctly.
    """
    # Implementation...
```

### System Code Indicators

**If solution code is provided, docstrings will show:**

```python
"""
---DEVELOPMENT HISTORY---
AUTHOR: [SYSTEM PROVIDED - No student assigned]
SOURCE: Instructor solution file
DATE PROVIDED: YYYY-MM-DD

---PEER REVIEW---
REVIEW STATUS: SYSTEM CODE - NO REVIEW GRADE EARNED
REVIEWER: [Student Name if assigned]
NOTES: Used system code due to non-participating original developer.
"""
```

**This makes it clear:**
- Code is system-provided
- No points earned for writing or reviewing it
- Legitimate use for non-participating teammate
- Not considered plagiarism

### Important Notes

**Do NOT:**
- ❌ Try to hide that you used system code (academic integrity violation)
- ❌ Claim system code as your own work
- ❌ Remove system code markers or docstrings
- ❌ Use solution code when your teammate IS participating

**DO:**
- ✓ Report non-participating teammates immediately
- ✓ Document system code usage clearly
- ✓ Keep system docstrings intact
- ✓ Integrate system code properly
- ✓ Focus on your own component and review

**Academic Integrity:**
Using system code when teammate doesn't participate = **Acceptable and documented**
Using system code when you're supposed to write it = **Plagiarism and violation**

---

## Frequently Asked Questions

### Team & Organization

**Q: Can I work with friends?**
A: Yes! Form your own teams of 5.

**Q: What if someone drops the class?**
A: Notify instructor immediately. May need to reassign components or merge teams.

**Q: What if my teammate isn't doing their work?**
A: See "Non-Participating Team Members" section below. Instructor can provide solution code so your team can continue.

**Q: Can I change components mid-project?**
A: Only in Week 1. After that, you're committed.

### Technical Questions

**Q: What Python version?**
A: Python 3.x (any recent version 3.6+)

**Q: Can I use external libraries?**
A: No. Only built-in Python libraries (csv, random, etc.)

**Q: What if CSV file doesn't exist?**
A: Your code should handle FileNotFoundError and create new file.

**Q: How do I test file I/O?**
A: Delete the CSV file, run your code, check if it creates new file.

### Grading Questions

**Q: If my code is perfect but my review is bad, can I still get an A?**
A: No. Review is 50% of your grade. Max would be 15/20 (75% = C).

**Q: What if the person refuses to fix their code?**
A: Document it. Show instructor. You won't be penalized for their refusal.

**Q: What if I miss a small bug in review?**
A: Small bugs are okay. But if you approve code without testing it and major bugs slip through, you lose points.

**Q: Do we all get the same grade?**
A: No! Individual grades based on:
  - Your component (5 pts)
  - Your review (10 pts)
  - Team integration (5 pts - same for all)

### Process Questions

**Q: How much time should I spend reviewing?**
A: 3-4 hours minimum. It's 50% of your grade.

**Q: Can I help teammates with their code?**
A: Yes! Collaboration within team is encouraged. Just don't write it for them.

**Q: What if we can't integrate the components?**
A: Person 5 leads integration. Get help from instructor during Week 3.

**Q: Can we add extra features?**
A: After all required features work, yes. But don't compromise requirements.

---

## Academic Integrity

### What's Allowed

✓ Collaborating with your team
✓ Helping teammates understand concepts
✓ Asking instructor for help
✓ Using course materials and examples
✓ Looking up Python documentation
✓ Using AI to understand concepts or debug

### What's NOT Allowed

✗ Copying code from other teams
✗ Copying code from internet without understanding
✗ Having AI write entire components for you
✗ Sharing code with other teams
✗ Submitting work you didn't write
✗ Fake reviews (saying you tested when you didn't)

### Consequences

**If academic integrity violation detected:**
- First offense: 0 on the project
- Reported to academic affairs
- May affect entire team if collaboration

**How we detect:**
- Code too advanced for modules covered
- Identical code across teams
- Student can't explain their code
- Reviews that clearly weren't done

**When in doubt:** Ask the instructor first!

---

## Final Checklist

### Before You Submit

- [ ] I filled in my name/ID at top of my file
- [ ] My code runs without errors
- [ ] Test code at bottom of my file works
- [ ] All my required methods are implemented
- [ ] I added docstrings with my name/date
- [ ] I validated user input
- [ ] I handled file errors
- [ ] I tested my code thoroughly
- [ ] I completed my assigned review
- [ ] I tested the code I reviewed
- [ ] I provided specific, helpful feedback
- [ ] I verified the author fixed issues
- [ ] I signed off on my review
- [ ] Team tested complete system
- [ ] All 6 Python files work together
- [ ] Data persists correctly
- [ ] README.txt is complete
- [ ] 5 review forms included
- [ ] One person submitted on Brightspace

---

## Contact & Support

### Getting Help

**From Your Team:**
- Group chat for quick questions
- Regular meetings for planning
- Help each other debug

**From Instructor:**
- Office hours: [Check syllabus]
- Email: [Instructor email]
- In-class help sessions

**Course Resources:**
- Modules 1-4 in course materials
- Python documentation: python.org/docs
- PEP 8 Style Guide: pep8.org

### Important Dates

- **Project Assigned:** November 25, 2024
- **Part 1 Due (In Class):** Thursday, December 4, 2024 - Components complete
- **Part 1 Brightspace Submission:** Saturday, December 6, 2024 - Integrated version
- **Part 2 Due (In Class):** Thursday, December 11, 2024 - Reviews complete, final integrated system
- **Part 2 Brightspace Submission:** Friday, December 13, 2024 - Final version with all reviews
- **Video Walkthrough Due:** Sunday, December 15, 2024, 11:59 PM
- **No Extensions:** Late work not accepted for any deadline

---

## You've Got This!

This project is challenging but achievable. Follow the timeline, communicate with your team, take review seriously, and you will succeed!

Remember:
- **25%** of your grade = code you write
- **50%** of your grade = code you review ← Most important!
- **25%** of your grade = team success

Quality assurance is MORE valuable than code generation. This prepares you for real software engineering careers.

**Good luck!** 🎓

---

*Last Updated: [Date]*
*Course: CPRG216 - Python Programming*
*Instructor: [Name]*
