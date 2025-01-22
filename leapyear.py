# Check if a year is a leap year or a common year
year = int(input("Enter a year: "))

# Check if the year is within the Gregorian calendar period
if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    # Determine if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Leap year")
    else:
        print("Common year")

# 2000: Leap year (divisible by 400).
# 1900: Common year (divisible by 100 but not by 400).
# 2024: Leap year (divisible by 4 and not by 100).
# 2023: Common year (not divisible by 4).
# 1580:Not within the Gregorian calendar period.
# 1600: Leap year (divisible by 400).