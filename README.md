# Project1 – Screen Time Tracker

**ET-574 Prof. Sun**  
**QUEENSBOROUGH COMMUNITY COLLEGE**  
**The City University of New York**  
**Department of Engineering Technology**

# Project I: Screen Time Tracker

## Description

Track your daily screen-time sessions in a console-based Python program.

## Topics Covered

- Console Output & Input
- Variables, Strings, and Numbers
- Functions
- Lists
- Loops and Logic
- GitHub Repository /Version Control, Codespaces Copilot, Issue Tracking

## File Structure

screen_time_tracker/

├── main.py                # Entry point with the menu loop

├── tracker.py             # Functions to complete

├── data.py                # In-memory data storage using parallel lists

├── README.md              # Project description and instructions

└── .github/

    └── issue_tracking.csv # Issue tracking


# Project Tasks

## 1. Menu System (main.py)

Build a menu loop with options:

- Add Screen Time Session
- View summary
- View All Sessions
- Exit

## 2. Add Screen Time Session (tracker.py)

Prompt for app/site name, minutes, category, and notes. Append to parallel lists in 'data.py'

## 3. View All Sessions

Print each entry in a formatted list using parallel lists

## 4. Summary Report

Show total minutes, total number of sessions, average minutes per session, maximum minutes spent in a single session, minimum minutes spent in a single session


## Example Console Output

Welcome to Screen Time Tracker!

1. Add Screen Time Session
2. View Summary
3. View All Sessions
4. Exit

Enter choice: 1

Enter app/site name: YouTube

Enter minutes spent: 25

Enter category (Social/School/Entertainment/Other): Entertainment

Enter notes (optional): Music playlist

Session added.


# Requirements

- Use functions to organize your code
- Use parallel lists to track sessions (no dictionaries for storage)
- Use GitHub for your group repository and the workflow you practiced in HW2 or HW3. One of the team members in the group will recreate a GitHub repository for each group and add all other group members as collaborators. Also add the instructor, jsunStation as a collaborator.
- Maintain the issue_tracking.csv in the repository for the entire project. Use issue tracking to record all issues and tasks. The issue_tracking.csv template was provided and reviewed in HW2—your group must add it to the repository and keep it updated.
- The issue tracking records plus the repository’s commit history serve as proof of work; submissions missing either will be considered incomplete.
- Include at least 6 commits on GitHub
- Use Copilot to assist with writing or reviewing code


# Group Project Format (2/3 Students per Group)

This project will be completed in teams of two or three. While responsibilities are divided, all members are equally accountable for the success, functionality, and quality of the entire program.


# Assigned Responsibilities

Each student will take primary responsibility for one component:

### Student A – Main Menu & Program Flow (main.py)

Develop and maintain the menu interface and overall program control logic. Ensure correct function calls and module integration.

### Student B – Add Session Function (tracker.py)

Implement the add_session() function, including thorough input validation and error handling.

### Student C – Summary & View Functions (tracker.py)

Implement the view_all() and view_summary() functions, including accurate calculations and clear output formatting.


# Shared Responsibilities (Required for All Members)

All team members must:

- Maintain and correctly update the parallel lists in data.py
- Actively use GitHub for version control (regular commits, meaningful commit messages, pull requests, and issue tracking)
- Participate in code reviews and provide constructive feedback
- Use GitHub Copilot responsibly as a development aid—not as a replacement for understanding
- Test the full program and verify that all components work together properly


# Accountability & Evaluation

- Every member is responsible for understanding the entire codebase—not just their assigned section.
- During evaluation, each student must be able to explain:
  - How the full system works
  - How different modules interact
  - Design decisions made by the team
  - Their individual contributions
- Inability to explain other parts of the project may result in an individual grade reduction.

This is a collaborative software development project. Division of tasks does not reduce shared responsibility.


# GitHub Submission

1. The repository name must strictly follow the naming convention below:

<Course Name>-<Section Name>-<Project1>-<Your Group Name>

2. Make sure to add all group members as collaborators.

3. Add jsunStation (the instructor’s GitHub username) as a collaborator.

4. Create issuetracker.csv.


# Screenshot Submission

Submit one PDF or Word document to Brightspace that includes the following screenshots showing your team project 1 work:

## 1. Collaborators

Screenshot of collaborators page in GitHub.

## 2. Source Code

Screenshots of the final source code for the assignment in Codespaces.

## 3. Commit History

Screenshots of the GitHub commit history tab for your individual or team repository.

The commit history must clearly show:

- Six or more commits over time
- Commit messages that accurately describe and match your work

## 4. Program Output / Results

Screenshots of the program running successfully in the Codespaces terminal, showing the program output and test results.

## 5. Issue Tracker

Screenshots of the issue tracker displayed in GitHub. The screenshots must clearly show:

- Each task/issue being opened and closed
- The associated commit ID for each task/issue
- Since this is a group project, please coordinate with your teammates and document your work in the GitHub issue tracker. If a group member does not complete their tasks, retain and attach your communication records. Take necessary steps to ensure the project is finished on time.
