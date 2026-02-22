# Taking user input
sentence = input("Enter a sentence: ")

# Removing leading/trailing spaces
clean_sentence = sentence.strip()

# Splitting into words
words = clean_sentence.split()

print("\nResults:")
print("Original:", clean_sentence)

# Total characters (with spaces)
print("Characters (with spaces):", len(clean_sentence))

# Total characters (without spaces)
print("Characters (without spaces):", len(clean_sentence.replace(" ", "")))

# Total words
print("Words:", len(words))

# Uppercase
print("UPPERCASE:", clean_sentence.upper())

# Lowercase
print("lowercase:", clean_sentence.lower())

# Title Case
print("Title Case:", clean_sentence.title())

# First word
if len(words) > 0:
    print("First word:", words[0])
else:
    print("First word: None")

# Last word
if len(words) > 0:
    print("Last word:", words[-1])
else:
    print("Last word: None")

# Reversed sentence
print("Reversed:", clean_sentence[::-1])