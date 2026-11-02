

year = int(input("Enter year: "))

if year <= 0:
    print("Error: Year must be a positive number greater than 0.")
    exit()

if year % 100 == 0:
    if year % 400 == 0:
        leap = True
        reason = "Century year divisible by 400"
    else:
        leap = False
        reason = "Century year not divisible by 400"
elif year % 4 == 0:
    leap = True
    reason = "Divisible by 4 and not a century year"
else:
    leap = False
    reason = "Not divisible by 4"

if leap:
    status = "LEAP YEAR"
    days_in_year = 366
    days_in_feb = 29
else:
    status = "COMMON YEAR"
    days_in_year = 365
    days_in_feb = 28

print()

print(f"Year: {year}")
print(f"Status: {status}")
print(f"Days in Year: {days_in_year} days")
print(f"Days in February: {days_in_feb} days")
print(f"Reason: {reason}")
