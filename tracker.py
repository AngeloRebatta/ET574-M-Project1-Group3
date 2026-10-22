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
    while True:
        app_name = input("Enter app/site name: ").strip()

        if app_name == "":
            print("App/site name cannot be empty.")
        else:
            break

    while True:
        try:
            minutes = int(input("Enter minutes spent: "))
        except ValueError:
            print("Minutes must be a number.")
            continue

        if minutes <= 0:
            print("Minutes must be greater than 0.")
        else:
            break
        
    while True:
        category = input(
            "Enter category (Social/School/Entertainment/Other): "
        ).strip().capitalize()

        if category not in ["Social", "School", "Entertainment", "Other"]:
            print("Invalid category.")
        else:
            break

    notes = input("Enter notes (optional): ")

    data.app_names.append(app_name)
    data.minutes.append(minutes)
    data.categories.append(category)
    data.notes.append(notes)

    print("Session added.")

def view_all():
    if len(data.app_names) == 0:
        print("\nNo sessions recorded yet.")
        return
    print("\nAll Sessions")
    print(f"{'#':<4}{'App/Site':<20}{'Minutes':<10}{'Category':<15}Notes")
    
    for i in range(len(data.app_names)):
        note = data.notes[i] if data.notes[i] else "-"
        print(f"{i + 1:<4}{data.app_names[i]:<20}{data.minutes[i]:<10}"
              f"{data.categories[i]:<15}{note}")



def view_summary():

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
