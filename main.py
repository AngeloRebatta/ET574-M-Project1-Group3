# Main program for Screen Time Tracker
# Shows the menu in a loop and calls the functions in tracker.py.

import tracker


def show_menu():
    """Print the main menu options."""
    print()
    print("1. Add Screen Time Session")
    print("2. View Summary")
    print("3. View All Sessions")
    print("4. Exit")


def main():
    """Run the menu loop until the user chooses to exit."""
    print("Welcome to Screen Time Tracker!")

    while True:
        show_menu()
        # Compare as text so letters or empty input never crash the program
        choice = input("Enter choice: ").strip()

        if choice == "1":
            tracker.add_session()
        elif choice == "2":
            tracker.view_summary()
        elif choice == "3":
            tracker.view_all()
        elif choice == "4":
            break
