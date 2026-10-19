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

    if len(data.app_names) == 0:
        print("\nNo sessions recorded yet.")
        return
    print("\nAll Sessions")
    print(f"{'#':<4}{'App/Site':<20}{'Minutes':<10}{'Category':<15}Notes")
    
    for i in range(len(data.app_names)):
        note = data.notes[i] if data.notes[i] else "-"
        print(f"{i + 1:<4}{data.app_names[i]:<19}{data.minutes[i]:<10}"
              f"{data.categories[i]:<15}{note}")



def view_summary():
    """Print a summary report of all saved sessions.

    Student C (Marcus).
    Shows total minutes, total number of sessions, average minutes per
    session, and the maximum and minimum minutes in a single session.
    Prints a message instead if there are no sessions.
    """

    if len(data.minutes) == 0:
        print("\nNo sessions recorded yet.")
        return

    total = sum(data.minutes)
    count = len(data.minutes)
    average = total / count

    print("\nSummary Report")
    print("-" * 30)
    print(f"Total minutes:        {total}")
    print(f"Total sessions:       {count}")
    print(f"Average per session:  {average:.1f}")
    print(f"Longest session:      {max(data.minutes)}")
    print(f"Shortest session:     {min(data.minutes)}")
