import math

# -------- PART 1: Check Single Number --------
num = int(input("Enter a number: "))

if num <= 1:
    print(f"{num} is NOT a prime number")

elif num == 2:
    print("2 is a PRIME number")

elif num % 2 == 0:
    print(f"{num} is NOT a prime number")

else:
    is_prime = True
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{num} is a PRIME number")
    else:
        print(f"{num} is NOT a prime number")


# -------- PART 2: Prime Numbers in Range --------
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", end=" ")

for number in range(start, end + 1):
    if number > 1:
        prime = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                prime = False
                break
        if prime:
            print(number, end=" ")