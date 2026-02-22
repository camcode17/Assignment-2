# Multiplication Table Generator

number = int(input("Enter number: "))
end = int(input("Enter range (end): "))

print(f"\nMultiplication Table of {number}")

for i in range(1, end + 1):
    print(f"{number} x {i} = {number * i}")