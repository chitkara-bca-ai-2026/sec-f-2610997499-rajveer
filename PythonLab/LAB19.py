
import os

FILENAME = "lab19.txt"

def write_notes(filename, content):
    with open(filename, 'w') as f:
        f.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")

def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return f.read()
    return "[INFO] No notes file exists yet. Please write some notes first."

def main():
    print("="*40)
    print("STUDENT NOTES MANAGEMENT SYSTEM")
    print("="*40)

    while True:
        print("\nSelect an operation:")
        print("1. Write / Save Notes")
        print("2. View Saved Notes")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            notes = input("Enter notes to save: ")
            write_notes(FILENAME, notes)
        elif choice == '2':
            print(f"--- Notes Content ({FILENAME}) ---")
            print(read_notes(FILENAME))
        elif choice == '3':
            print("Thank you for using the Notes Management System. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()