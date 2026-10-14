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
    pass


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
