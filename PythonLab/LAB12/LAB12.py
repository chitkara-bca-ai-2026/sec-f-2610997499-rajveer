

sentence = input("Enter a sentence: ")


words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in sentence:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

letters = vowels + consonants
vowel_percent = (vowels / letters * 100) if letters > 0 else 0


print("DOCUMENT ANALYSIS REPORT")
print(f"Sentence: {sentence}")
print(f"Total characters: {len(sentence)}")

print()

print("---Character Breakdown---")
print(f"Words:              {words}")
print(f"Vowels:             {vowels}")
print(f"Consonants:         {consonants}")
print(f"Digits:             {digits}")
print(f"Spaces:             {spaces}")
print(f"Special characters: {special}")

print()

print("---Summary---")
print(f"Total letters: {letters}")
print(f"Vowel percentage: {vowel_percent:.1f}%")

print()

print("Analysis Complete!")
