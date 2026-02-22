# Movie Ticket Pricing System

# Inputs
age = int(input("Enter age: "))
day = input("Enter day of week: ").strip().lower()
tickets = int(input("Enter number of tickets: "))

# Determine base price per ticket
if age < 3:
    price = 0
    category = "Free"
elif 3 <= age <= 12:
    price = 150
    category = "Child"
elif 13 <= age <= 59:
    price = 300
    category = "Adult"
else:
    price = 200
    category = "Senior"

# Calculate base total
base_total = price * tickets

# Check for weekend discount
if day in ["friday", "saturday", "sunday"]:
    discount = 0.20 * base_total
else:
    discount = 0

final_total = base_total - discount

# Display results
print("\n=== TICKET BILL ===")
print(f"Category: {category}")
print(f"Base price per ticket: ₹{price:.2f}")
print(f"Number of tickets: {tickets}")
print(f"Base total: ₹{base_total:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final amount: ₹{final_total:.2f}")