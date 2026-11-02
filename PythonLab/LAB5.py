
import math


value = float(input("Enter a numerical value: "))
exponent = float(input("Enter an exponent: "))
decimal = float(input("Enter a decimal measurement: "))

power = math.pow(value, exponent)
root = math.sqrt(value)
upper = math.ceil(decimal)
lower = math.floor(decimal)

print()

print("--- Results ---")
print(f"  Value             : {value}")
print(f"  Exponent          : {exponent}")
print(f"  Power (pow)       : {power}")
print(f"  Square Root (sqrt): {root:.4f}")
print(f"  Decimal Value     : {decimal}")
print(f"  Ceil Value        : {upper}")
print(f"  Floor Value       : {lower}")
