
Coffee = 3.50
Muffin = 2.10
Water = 1.05
Tax = 0.06

totalCoffee = (Coffee*2)
totalMuffin = (Muffin*3)
totalWater = (Water*4)
Subtotal = (totalCoffee + totalMuffin + totalWater)
totalTax = (Subtotal*Tax)
totalPrice = (Subtotal + totalTax)



receipt = f"========== RECEIPT =========\nItem\t\tPrice\tQty\tTotal\nCoffee\t\t$3.50\t2\t${totalCoffee}\nMuffin\t\t$2.10\t3\t${totalMuffin}\nWater\t\t$1.05\t4\t${totalWater}\n------------------------------\nSubtotal\t\t${Subtotal}\nTax(6%)\t\t\t${totalTax}\nTotal\t\t${totalPrice}\n==========================="
print(receipt)