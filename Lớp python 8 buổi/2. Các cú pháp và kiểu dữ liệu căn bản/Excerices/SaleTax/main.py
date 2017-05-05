from pprint import pprint

# weightInKilograms = 50
# heightInMeters = 1.65
try:
    inputPrice = float(input("Your input price = "))
except Exception:
    pass

try:
    salePrice = float(input("Your sale price = "))
except Exception:
    pass

TAX_PERCENT = 0.1
profit = (salePrice - inputPrice) * TAX_PERCENT
print("Profit = "+str(profit))
if profit < 0:
    print("profit < 0")
elif profit > 0:
    print("profit > 0")
else:
    print("profit = 0")