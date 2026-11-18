
import os

FILENAME = "lab21.txt"

SAMPLE_TEXT = (
    "My name is Rajveer and I am a college student.\n"
    "I am pursuing BCA with a specialisation in AI and ML at Chitkara University.\n"
    "I started my first semester in 2026 and I am learning Python.\n"
    "I am practising file handling in Python through my lab exercises.\n"
)

def init_document(filename):
    if not os.path.exists(filename):
        with open(filename, 'w') as f:
            f.write(SAMPLE_TEXT)

def get_document_statistics(filename):
    with open(filename, 'r') as f:
        content = f.read()
    lines = content.splitlines()

    line_count = len(lines)
    word_count = len(content.split())
    char_count = len(content)
    return (line_count, word_count, char_count)

def display_document(filename):
    print(f"---Document Preview ({filename})---")
    with open(filename, 'r') as f:
        for number, line in enumerate(f, start=1):
            print(f"{number:3d} | {line.rstrip()}")

def main():
    init_document(FILENAME)
    print("="*40)
    print("DOCUMENT STATISTICS ANALYZER")
    print("="*40)

    while True:
        print("\nSelect an operation:")
        print("1. Calculate Document Statistics")
        print("2. Display Document Content")
        print("3. Exit")

        choice = input("\nEnter choice (1-3): ").strip()

        if choice == '1':
            if not os.path.exists(FILENAME):
                print(f"[ERROR] '{FILENAME}' not found.")
                continue
            lines, words, chars = get_document_statistics(FILENAME)
            print("="*17+"DOCUMENT REPORT"+"="*17)
            print(f"Target File      : {FILENAME}")
            print(f"Total Lines      : {lines}")
            print(f"Total Words      : {words}")
            print(f"Total Characters : {chars}")
            print("=" * 50)
        elif choice == '2':
            if not os.path.exists(FILENAME):
                print(f"[ERROR] '{FILENAME}' not found.")
                continue
            display_document(FILENAME)
        elif choice == '3':
            print("Thank you for using Document Statistics Analyzer. Goodbye!")
            break
        else:
            print("[ERROR] Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()