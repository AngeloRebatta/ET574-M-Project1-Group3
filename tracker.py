# Functions for Screen Time Tracker
# add_session(), view_all(), and view_summary() will be implemented here.

import data


def add_session():
    """Ask the user for a new screen time session and save it.

    Student B (Angelo).
    Prompts for app/site name, minutes, category and notes, validates
    each value, then appends them to the four parallel lists in data.py
    (all four together, only after every value is valid) and prints
    "Session added."
    """
    app_name = input("Enter app/site name: ")
    if app_name == "":
        print("App/site name cannot be empty.")
        return

    try:
        minutes = int(input("Enter minutes spent: "))
    except ValueError:
        print("Minutes must be a number.")
        return

    if minutes <= 0:
        print("Minutes must be greater than 0.")
        return
        
    category = input("Enter category (Social/School/Entertainment/Other): ")

    if category not in ["Social", "School", "Entertainment", "Other"]:
        print("Invalid category.")
        return

    notes = input("Enter notes (optional): ")

    data.app_names.append(app_name)
    data.minutes.append(minutes)
    data.categories.append(category)
    data.notes.append(notes)

    print("Session added.")

def view_all():
    """Print every saved session as a formatted list.

    Student C (Marcus).
    Loops over the parallel lists in data.py using the same index for
    each list. Prints a message instead if there are no sessions.
    """
    pass


def view_summary():
    """Print a summary report of all saved sessions.

    Student C (Marcus).
    Shows total minutes, total number of sessions, average minutes per
    session, and the maximum and minimum minutes in a single session.
    Prints a message instead if there are no sessions.
    """
    pass
