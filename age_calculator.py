from datetime import datetime

# Get today's date
today = datetime.now()

# User input
day = int(input("Enter birth day (DD): "))
month = int(input("Enter birth month (MM): "))
year = int(input("Enter birth year (YYYY): "))

# Create birth date object
birth_date = datetime(year, month, day)

# Calculate exact difference
difference = today - birth_date

# Exact age in days
total_days = difference.days
age_years = total_days // 365
age_months = age_years * 12
age_hours = total_days * 24
age_minutes = age_hours * 60
years_to_100 = 100 - age_years

# Display results
print("\nResults:")
print("Exact Age:", age_years, "years")
print("Total Days Lived:", total_days)
print("Age in Months:", age_months)
print("Age in Hours:", age_hours)
print("Age in Minutes:", age_minutes)
print("Years until 100:", years_to_100)