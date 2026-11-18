
import os

FILENAME = "lab20.txt"

SAMPLE_ENTRIES = [
    "09:00 AM - System server startup verified.",
    "10:30 AM - Morning attendance synchronized.",
    "02:15 PM - Network security patch applied.",
]

def init_log(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            for entry in SAMPLE_ENTRIES:
                f.write(entry + '\n')

def append_entry(filename, entry):
    with open(filename, 'a') as f:
        f.write(entry + '\n')
    print(f"[SUCCESS] New entry logged to '{filename}'.")

def display_log(filename):
    with open(filename, 'r') as f:
        entries = [line.rstrip('\n') for line in f if line.strip()]

    print("="*15+"DAILY LOG BOOK"+"="*15)
    for i, entry in enumerate(entries, start=1):
        print(f"[{i:02d}] {entry}")
    print(f"\nTotal Logged Entries: {len(entries)}")
    print("="*40)

def main():
    init_log(FILENAME)
    print("="*40)
    print("OFFICE DAILY LOG BOOK")
    print("="*40)

    while True:
        print("\nSelect an operation:")
        print("1. Add Log Entry")
        print("2. Display Complete Log")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            entry = input("Enter log entry: ").strip()
            if entry:
                append_entry(FILENAME, entry)
            else:
                print("[ERROR] Entry cannot be empty.")
        elif choice == '2':
            display_log(FILENAME)
        elif choice == '3':
            print("Thank you for using the Daily Log Book. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()