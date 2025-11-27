# GitHub Repository Submission (Required - Not Graded)

**Course:** CPRG216 - Python Programming
**Component:** Course Registration System Group Project

---

## Overview

GitHub is the **required submission method** for this project. You must submit your project via a GitHub repository link on Brightspace.

**Important:**
- **Required:** GitHub repository link submitted to Brightspace (mandatory submission method)
-  **Optional:** LinkedIn Learning Git/GitHub course (helpful but not required)

**Why GitHub?**
- Instructor can easily download and grade your complete project
- Shows work history (helps verify everyone participated)
- Industry-standard submission method
- Professional skill useful for your career

---

## LinkedIn Learning Courses (Optional but Strongly Recommended)

### Why Take a Course?

Even if you know Git/GitHub basics, these courses will help you:
- Learn best practices for team collaboration
- Understand branching strategies
- Master pull requests and code reviews
- Work more efficiently with your team

### Recommended Courses (Choose ONE if interested)

**All courses are FREE through SAIT Library!**

#### Option 1: GitHub Essential Training: 1 The Basics (Recommended)
- **Title:** GitHub Essential Training: 1 The Basics
- **Duration:** 1 hour 2 minutes
- **Link:** [GitHub Essential Training: 1 The Basics](https://www.linkedin.com/learning/github-essential-training-1-the-basics)
- **URL:** https://www.linkedin.com/learning/github-essential-training-1-the-basics
- **Release Date:** July 24, 2023 (most current version)
- **Topics Covered:**
  - Creating repositories
  - Committing changes
  - Branching and merging
  - Pull requests
  - Collaboration features
  - GitHub interface basics

#### Option 2: Git Essential Training: The Basics (2023 Version)
- **Title:** Git Essential Training: The Basics
- **Duration:** 1 hour 23 minutes
- **Link:** [Git Essential Training](https://www.linkedin.com/learning/git-essential-training-the-basics/use-git-version-control-software-to-manage-project-code)
- **URL:** https://www.linkedin.com/learning/git-essential-training-the-basics/use-git-version-control-software-to-manage-project-code
- **Instructor:** Barbara Forbes (2023 version)
- **Topics Covered:**
  - Git fundamentals
  - Version control concepts
  - Basic Git commands
  - Working with repositories
  - Collaboration workflows

#### Option 3: Learning Git and GitHub (2021)
- **Title:** Learning Git and GitHub
- **Duration:** 1 hour 52 minutes
- **Link:** [Learning Git and GitHub](https://www.linkedin.com/learning/learning-git-and-github-14213624)
- **URL:** https://www.linkedin.com/learning/learning-git-and-github-14213624
- **Popularity:** 135,000+ views
- **Topics Covered:**
  - Git and GitHub basics
  - Repository management
  - Branching strategies
  - Collaboration features
  - Best practices

#### Option 4: Other Git/GitHub Courses
- Any other Git or GitHub course on LinkedIn Learning
- Check with instructor if unsure

### Accessing LinkedIn Learning

**As a SAIT student, you have FREE access to LinkedIn Learning!**

1. Go to SAIT Library website
2. Look for LinkedIn Learning link
3. Log in with your SAIT credentials
4. Search for the course
5. Complete the course

**Note:** There should be NO out-of-pocket expenses. Contact your instructor if you have issues accessing the courses.

### Certificate Submission (Optional)

If you complete a course and want to showcase it:
- Take a screenshot of your completion certificate
- Include it in your GitHub repository (optional)
- Mention it in your README.md

This is **not required** but shows initiative and professional development!

---

## GitHub Repository Setup (Required)

### Repository Requirements

1. **Create a Private Repository**
   - Repository name: `cprg216-registration-system-teamX` (replace X with your team number)
   - Must be PRIVATE (not public)
   - Initialize with README

2. **Add Instructor as Collaborator**
   - Add your instructor's GitHub username as a collaborator
   - Instructor username: [Instructor will provide]
   - This allows instructor to view your private repository

3. **Repository Structure**
   ```
   cprg216-registration-system-teamX/
   ├── README.md (team info and project description)
   ├── students.csv
   ├── courses.csv
   ├── enrollments.csv
   ├── student.py
   ├── student_manager.py
   ├── course.py
   ├── course_manager.py
   ├── enrollment_manager.py
   ├── main.py
   └── reviews/
       ├── review_student.md
       ├── review_student_manager.md
       ├── review_course.md
       ├── review_enrollment.md
       └── review_main.md
   ```

### Branch Strategy

**Each team member must create their own branch:**

1. **Branch naming convention:**
   ```
   <component-name>-<student-name>
   ```

   **Examples:**
   - `student-class-alice`
   - `student-manager-bob`
   - `course-classes-charlie`
   - `enrollment-manager-diana`
   - `main-application-emma`

2. **Work on your branch:**
   - All development for your component happens on YOUR branch
   - Commit regularly (not just one big commit at the end)
   - Write meaningful commit messages

3. **Commit message guidelines:**
   ```
   Good examples:
   - "Add student ID validation to __init__ method"
   - "Fix bug in search_student_by_name when name not found"
   - "Implement read_students_file with error handling"
   
   Bad examples:
   - "Update"
   - "Changes"
   - "Fixed stuff"
   ```

### Using GitHub for Code Review

**GitHub should be used for the peer review process:**

1. **When your component is ready (Dec 4):**
   - Commit all changes to your branch
   - Push your branch to GitHub
   - Create a Pull Request (PR) to main branch
   - Title PR: "Component X - Ready for Review"
   - Add description explaining what you built

2. **When assigned to review (Dec 5):**
   - Go to assigned component's Pull Request
   - Review the code on GitHub
   - Add comments directly on specific lines of code
   - Document issues using GitHub PR comments
   - Complete PEER_REVIEW_FORM.md offline, then add to repo

3. **After receiving review feedback (Dec 6-11):**
   - Address comments on your PR
   - Commit fixes to your branch
   - Reply to reviewer's comments explaining fixes
   - Request re-review when ready

4. **Integration (Dec 11):**
   - Person 5 (Main Application) merges all approved PRs into main branch
   - Test complete system
   - Fix any integration issues
   - Final commit to main branch

### Collaboration Evidence

**Your repository should show:**

✓ Each team member has their own branch
✓ Regular commits (not just one at the end)
✓ Meaningful commit messages
✓ Pull requests for each component
✓ Code review comments in PRs
✓ Responses to review feedback
✓ All branches eventually merged to main

---

## Part 3: Final Submission

### README.md Requirements

Your repository's README.md must include:

```markdown
# Course Registration System - Team [X]

## Team Members

| Name | Student ID | Component | Branch |
|------|------------|-----------|--------|
| Alice Johnson | 2023012345 | Student Class | student-class-alice |
| Bob Smith | 2023045678 | StudentManager | student-manager-bob |
| ... | ... | ... | ... |

## Project Description

[Brief description of the Course Registration System]

## How to Run

1. Clone the repository
2. Navigate to project directory
3. Run: `python main.py`
4. Follow menu prompts

## Features

- [x] Student management (add, edit, search, remove)
- [x] Course management (add, edit, search, remove)
- [x] Enrollment system with validation
- [x] Grade assignment and tracking
- [x] System reports and statistics
- [x] Data persistence (CSV files)

## Review Assignments

- Student Class reviewed by: [Name]
- StudentManager reviewed by: [Name]
- Course Classes reviewed by: [Name]
- EnrollmentManager reviewed by: [Name]
- Main Application reviewed by: [Name]

## Known Issues

[List any known bugs or limitations, or state "None"]

## Git/GitHub Usage

Each team member worked on their own branch. Pull requests were used
for code review. All components were successfully integrated into the
main branch.
```

### Brightspace Submission

**What to Submit to Brightspace (December 13):**

**Required:**
1. **GitHub Repository Link**
   - Format: `https://github.com/username/cprg216-registration-system-teamX`
   - Make sure link is accessible (instructor added as collaborator)
   - Include in your README.txt or as a separate text file

**Optional:**
2. **LinkedIn Learning Certificate** (if completed)
   - Include screenshot in your repository
   - Mention in README.md
   - Shows professional development initiative

**Submission Format:**
One team member submits on Brightspace with Part 2:
```
Team Number: [X]
GitHub Repository URL: https://github.com/[username]/cprg216-registration-system-team[X]

IMPORTANT: Instructor has been added as collaborator
Instructor can access the repository: Yes

Team Members:
- [Name 1] - [Student ID] - Branch: [branch-name]
- [Name 2] - [Student ID] - Branch: [branch-name]
- [Name 3] - [Student ID] - Branch: [branch-name]
- [Name 4] - [Student ID] - Branch: [branch-name]
- [Name 5] - [Student ID] - Branch: [branch-name]
```

---

## Submission Requirements (Not Graded)

**GitHub is simply how you submit your project - it's not worth separate points.**

### What You MUST Have:

✅ **Private GitHub repository** with your project
✅ **Instructor added as collaborator** (so instructor can access it)
✅ **Repository link submitted to Brightspace** by December 13

### What's Recommended (But Optional):

💡 Each team member uses their own branch (helps show who did what)
💡 Regular commits with clear messages (shows your work process)
💡 Pull requests for code review (good practice, optional)

### Important Notes:

- **You won't be graded on Git/GitHub usage** - it's just the submission method
- **You WILL be graded on** your code, peer reviews, and team integration
- The repository just needs to contain your complete project files
- Commit history helps verify everyone participated (academic integrity)

---

## Tips for Success

### Git/GitHub Best Practices

**Do:**
- ✓ Commit frequently (after completing each method or feature)
- ✓ Write descriptive commit messages
- ✓ Use your own branch for development
- ✓ Pull latest changes before starting work
- ✓ Review others' code thoughtfully on GitHub
- ✓ Respond to review comments

**Don't:**
- ✗ Work directly on main branch
- ✗ Commit all changes at once at the end
- ✗ Use vague commit messages like "update" or "fix"
- ✗ Force push (unless you know what you're doing)
- ✗ Ignore merge conflicts

### Common Issues & Solutions

**Issue: "I don't have Git installed"**
- Solution: Download from git-scm.com or use GitHub Desktop

**Issue: "I don't know how to use Git"**
- Solution: Complete the LinkedIn Learning course first!

**Issue: "Merge conflict"**
- Solution: Ask teammate or instructor for help, or see Git docs

**Issue: "Can't push to repository"**
- Solution: Check you're on your branch, not main. Ensure you have permissions.

**Issue: "Forgot to create branch"**
- Solution: Create branch now, move commits to it. Ask instructor for help if needed.

### Resources

- **Git Cheat Sheet:** https://education.github.com/git-cheat-sheet-education.pdf
- **GitHub Docs:** https://docs.github.com/
- **Git Tutorial:** https://git-scm.com/docs/gittutorial
- **Instructor Office Hours:** [Schedule]

---

## Frequently Asked Questions

**Q: Do I need to pay for GitHub?**
A: No. GitHub is free for students. Private repositories are free.

**Q: What if I've never used Git before?**
A: That's fine! Complete the LinkedIn Learning course, and follow the instructions here. Ask for help if needed.

**Q: Can we use GitHub Desktop instead of command line?**
A: Yes! GitHub Desktop is perfectly acceptable. Use whatever you're comfortable with.

**Q: What if someone on my team doesn't use GitHub?**
A: Everyone must participate. If someone refuses, let the instructor know. They'll lose the 5 points for GitHub component.

**Q: How many commits should I have?**
A: At least 5-10 meaningful commits. More is better. Commit after completing each significant piece of work.

**Q: Can I work on main branch?**
A: No. Each person must use their own branch. Only Person 5 merges to main during integration.

**Q: What if I mess up Git?**
A: Don't panic! Git is forgiving. Ask instructor for help. That's what office hours are for!

**Q: Do all commits need to be on separate days?**
A: No, but commits should be spread out over development period, not all in the last hour.

---

## Checklist Before Submission

GitHub Component:
- [ ] LinkedIn Learning course completed
- [ ] Certificate downloaded and submitted to Brightspace
- [ ] Private repository created with correct name
- [ ] Instructor added as collaborator
- [ ] Each team member has their own branch
- [ ] All code files committed to appropriate branches
- [ ] Pull requests created for each component
- [ ] Code review done via GitHub comments
- [ ] All approved PRs merged to main branch
- [ ] README.md completed with all information
- [ ] Repository link submitted to Brightspace
- [ ] Repository is accessible to instructor

---

**Good luck with Git and GitHub!**

This is a valuable professional skill that you'll use throughout your career.
