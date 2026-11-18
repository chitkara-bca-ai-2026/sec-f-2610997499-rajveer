
import os

FILENAME = "lab22.txt"

SAMPLE_TEXT = (
    "My name is Rajveer and I am a college student.\n"
    "I am pursuing BCA with a specialisation in AI and ML at Chitkara University.\n"
    "I started my first semester in 2026 and I am learning Python.\n"
    "I am practising file handling in Python through my lab exercises.\n"
)

def init_report(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(SAMPLE_TEXT)

def search_keyword(filename, keyword):
    total = 0
    print(f"---Search Results for '{keyword}'---")
    with open(filename, 'r') as f:
        for line_no, line in enumerate(f, start=1):
            if keyword.lower() in line.lower():
                matches = line.lower().count(keyword.lower())
                total += matches
                print(f"Line {line_no:2d} ({matches} match): {line.rstrip()}")

    if total > 0:
        print(f"\n[FOUND] Total occurrences of '{keyword}': {total}")
    else:
        print(f"\n[NOT FOUND] '{keyword}' does not appear in the document.")
    return total

def display_document(filename):
    print(f"---Full Report Document ({filename})---")
    with open(filename, 'r') as f:
        for line_no, line in enumerate(f, start=1):
            print(f"{line_no:2d} | {line.rstrip()}")

def main():
    init_report(FILENAME)
    print("="*40)
    print("KEYWORD SEARCH UTILITY")
    print("="*40)

    while True:
        print("\nSelect an operation:")
        print("1. Search Keyword in Document")
        print("2. View Full Document")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            keyword = input("Enter keyword to search: ").strip()
            if keyword:
                search_keyword(FILENAME, keyword)
            else:
                print("[ERROR] Keyword cannot be empty.")
        elif choice == '2':
            display_document(FILENAME)
        elif choice == '3':
            print("Thank you for using Keyword Search Utility. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()