

product_name = input("Enter Product Name : ")
price = float(input("Enter Price        : "))
quantity = int(input("Enter Quantity     : "))

total_price = price * quantity
amount_str = str(total_price)

print()

print(f"{'TYPE CASTING SUMMARY':^50}")
print(f"{'Variable':<17}{'Value':<17}{'Python Type'}")
print(f"{'product_name':<17}{product_name:<17}{type(product_name)}")
print(f"{'price':<17}{price:<17}{type(price)}")
print(f"{'quantity':<17}{quantity:<17}{type(quantity)}")
print(f"{'total_price':<17}{total_price:<17}{type(total_price)}")
print(f"{'amount_str':<17}{amount_str:<17}{type(amount_str)}")

print()
print(f"{'TAX INVOICE':^50}")
print(f"  Product Name   : {product_name}")
print(f"  Price per Unit : Rs. {price:.2f}")
print(f"  Quantity       : {quantity}")
print(f"  Invoice Total  : Rs. {amount_str}")
