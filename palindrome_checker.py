user_input = input("Enter word/number: ")

# Store original
original = user_input

# Reverse manually (step-by-step using loop)
reversed_value = ""
for char in user_input:
    reversed_value = char + reversed_value

# Case-insensitive comparison
if original.lower() == reversed_value.lower():
    result = "PALINDROME"
else:
    result = "NOT A PALINDROME"

# Display output
print("\nOriginal:", original)
print("Reversed:", reversed_value)
print("Result:", result)