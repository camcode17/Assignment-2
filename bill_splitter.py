# Taking inputs
total_bill = float(input("Enter total bill: ₹"))
people = int(input("Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))

# Calculations
tax_amount = (tax_percent / 100) * total_bill
after_tax = total_bill + tax_amount

tip_amount = (tip_percent / 100) * after_tax
final_total = after_tax + tip_amount

# Avoid division by zero
if people > 0:
    per_person = final_total / people
else:
    per_person = 0

# Display results
print("\n=== BILL BREAKDOWN ===")
print(f"Subtotal: ₹{total_bill:.2f}")
print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
print(f"After tax: ₹{after_tax:.2f}")
print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
print(f"Total: ₹{final_total:.2f}")
print(f"Per person: ₹{per_person:.2f}")