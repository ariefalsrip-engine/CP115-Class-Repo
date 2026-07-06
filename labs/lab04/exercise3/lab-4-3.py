hours = float(input())
if hours <= 2:
    mallCharges = 0
else:
    if hours > 5:
        mallCharges = 3
    else:
        mallCharges = 2
parkingFee = hours * mallCharges
if parkingFee >= 30:
    parkingFee = 30
print(parkingFee)
