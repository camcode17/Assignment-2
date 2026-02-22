count = int(input("How many numbers? "))

if count <= 0:
    print("Invalid count!")
else:
    total = 0
    maximum = None
    minimum = None

    for i in range(1, count + 1):
        num = float(input(f"Enter number {i}: "))
        total += num

        if maximum is None or num > maximum:
            maximum = num

        if minimum is None or num < minimum:
            minimum = num

    average = total / count

    print("\nSum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)