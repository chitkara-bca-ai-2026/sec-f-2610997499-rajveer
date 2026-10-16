

print("=" * 40)
print("      CLOTHING STORE BILLING SYSTEM")
print("=" * 40)


customer = input("Enter Customer Name: ")
garment = input("Enter Garment Name: ")
price = float(input("Enter Price of one garment: "))
quantity = int(input("Enter Number of Garments: "))

total = price * quantity


print()
print("=" * 40)
print("                  BILL")
print("=" * 40)
print(f"  Customer Name  : {customer}")
print(f"  Garment Name   : {garment}")
print(f"  Price per Unit : Rs. {price}")
print(f"  Quantity       : {quantity}")
print(f"  Total Amount   : Rs. {total}")
print("=" * 40)

