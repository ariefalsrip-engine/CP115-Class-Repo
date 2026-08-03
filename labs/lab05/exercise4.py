item_name = input("item name:")
price = float(input("price: RM"))
quantity = 3
tax_rate = 0.06

sub_total = price * quantity
tax_amount = sub_total * tax_rate
total_cost = sub_total + tax_amount

print(sub_total)
print(tax_amount)
print(total_cost)