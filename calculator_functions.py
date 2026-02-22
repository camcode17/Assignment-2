def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    if second_number == 0:
        return "Error! Division by zero is not allowed."
    return first_number / second_number


def modulus(first_number, second_number):
    if second_number == 0:
        return "Error! Modulus by zero is not allowed."
    return first_number % second_number


def power(base_number, exponent_number):
    return base_number ** exponent_number


def calculator():
    while True:
        print("\n===== CALCULATOR MENU =====")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            number_one = float(input("Enter first number: "))
            number_two = float(input("Enter second number: "))

            if choice == "1":
                result = add(number_one, number_two)
            elif choice == "2":
                result = subtract(number_one, number_two)
            elif choice == "3":
                result = multiply(number_one, number_two)
            elif choice == "4":
                result = divide(number_one, number_two)
            elif choice == "5":
                result = modulus(number_one, number_two)
            elif choice == "6":
                result = power(number_one, number_two)

            print("Result:", result)
        else:
            print("Invalid choice! Please select a valid option.")


# Call main function
calculator()