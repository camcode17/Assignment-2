def count_words(text):
    words = text.split()
    return len(words)


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


def count_consonants(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            count += 1
    return count


def reverse_text(text):
    reversed_string = ""
    for char in text:
        reversed_string = char + reversed_string
    return reversed_string


def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    reversed_text_value = cleaned[::-1]
    return cleaned == reversed_text_value


def remove_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char not in vowels:
            result += char
    return result


def word_frequency(text):
    words = text.lower().split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def longest_word(text):
    words = text.split()
    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


def analyze_text(text):
    print("\n=== TEXT ANALYSIS ===")

    print("Words:", count_words(text))
    print("Vowels:", count_vowels(text))
    print("Consonants:", count_consonants(text))
    print("Reversed:", reverse_text(text))

    if is_palindrome(text):
        print("Palindrome: Yes")
    else:
        print("Palindrome: No")

    print("Without vowels:", remove_vowels(text))

    longest = longest_word(text)
    print(f"Longest word: {longest} ({len(longest)} letters)")

    frequency = word_frequency(text)
    print("Word Frequency:", end=" ")

    for word, count in frequency.items():
        print(f"{word}: {count}", end=", ")

    print()


# -------- MAIN PROGRAM --------
user_text = input("Enter text: ")
analyze_text(user_text)