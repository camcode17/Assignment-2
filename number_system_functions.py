import math


# 1️⃣ Factorial
def factorial(number_value):
    if number_value < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, number_value + 1):
        result *= i
    return result


# 2️⃣ Prime Check
def is_prime(number_value):
    if number_value <= 1:
        return False
    if number_value == 2:
        return True
    if number_value % 2 == 0:
        return False

    for divisor in range(3, int(math.sqrt(number_value)) + 1, 2):
        if number_value % divisor == 0:
            return False
    return True


# 3️⃣ Fibonacci (nth term)
def fibonacci(position_value):
    if position_value <= 0:
        return "Invalid position"
    if position_value == 1:
        return 0
    if position_value == 2:
        return 1

    first_term = 0
    second_term = 1

    for _ in range(3, position_value + 1):
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term

    return second_term


# 4️⃣ Sum of Digits
def sum_of_digits(number_value):
    total_sum = 0
    for digit in str(abs(number_value)):
        total_sum += int(digit)
    return total_sum


# 5️⃣ Reverse Number
def reverse_number(number_value):
    reversed_value = int(str(abs(number_value))[::-1])
    return -reversed_value if number_value < 0 else reversed_value


# 6️⃣ Armstrong Number
def is_armstrong(number_value):
    digits = str(abs(number_value))
    power_value = len(digits)
    total_sum = 0

    for digit in digits:
        total_sum += int(digit) ** power_value

    return total_sum == abs(number_value)


# 7️⃣ GCD (Euclidean Algorithm)
def gcd(first_value, second_value):
    while second_value != 0:
        first_value, second_value = second_value, first_value % second_value
    return abs(first_value)


# 8️⃣ LCM
def lcm(first_value, second_value):
    return abs(first_value * second_value) // gcd(first_value, second_value)


# 9️⃣ Perfect Number
def is_perfect_number(number_value):
    if number_value <= 1:
        return False

    divisor_sum = 0
    for divisor in range(1, number_value):
        if number_value % divisor == 0:
            divisor_sum += divisor

    return divisor_sum == number_value


# 🔟 Menu System
def math_menu():
    while True:
        print("\n===== NUMBER SYSTEM MENU =====")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Number Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number Check")
        print("10. Exit")

        user_choice = input("Enter your choice (1-10): ")

        if user_choice == "10":
            print("Exiting program. Goodbye!")
            break

        elif user_choice == "1":
            value = int(input("Enter number: "))
            print("Result:", factorial(value))

        elif user_choice == "2":
            value = int(input("Enter number: "))
            print("Prime?" , is_prime(value))

        elif user_choice == "3":
            position = int(input("Enter position: "))
            print("Fibonacci term:", fibonacci(position))

        elif user_choice == "4":
            value = int(input("Enter number: "))
            print("Sum of digits:", sum_of_digits(value))

        elif user_choice == "5":
            value = int(input("Enter number: "))
            print("Reversed number:", reverse_number(value))

        elif user_choice == "6":
            value = int(input("Enter number: "))
            print("Armstrong?", is_armstrong(value))

        elif user_choice == "7":
            first = int(input("Enter first number: "))
            second = int(input("Enter second number: "))
            print("GCD:", gcd(first, second))

        elif user_choice == "8":
            first = int(input("Enter first number: "))
            second = int(input("Enter second number: "))
            print("LCM:", lcm(first, second))

        elif user_choice == "9":
            value = int(input("Enter number: "))
            print("Perfect number?", is_perfect_number(value))

        else:
            print("Invalid choice. Please try again.")


# Run Menu
math_menu()