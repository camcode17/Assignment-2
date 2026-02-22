# Leap Year Checker Program

year = int(input("Enter a year: "))

print("\n=== RESULT ===")

if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year}: Leap Year")
        print("Reason: Divisible by 4 and not divisible by 100.")
    elif year % 400 == 0:
        print(f"{year}: Leap Year")
        print("Reason: Divisible by 4, divisible by 100, and also divisible by 400.")
    else:
        print(f"{year}: NOT a Leap Year")
        print("Reason: Divisible by 100 but not divisible by 400.")
else:
    print(f"{year}: NOT a Leap Year")
    print("Reason: Not divisible by 4.")