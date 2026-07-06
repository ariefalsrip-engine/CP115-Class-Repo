kwh = float(input())
if kwh <= 100:
    utility = 0.3
else:
    if kwh > 200:
        utility = 0.75
    else:
        utility = 0.5
totalBill = kwh * utility
print(totalBill)
