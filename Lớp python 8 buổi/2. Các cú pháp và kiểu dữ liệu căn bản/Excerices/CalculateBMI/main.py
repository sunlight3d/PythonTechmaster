from pprint import pprint

# weightInKilograms = 50
# heightInMeters = 1.65
try:
    weightInKilograms = float(input("Enter weight in kg = "))
except Exception:
    pass

try:
    heightInMeters = float(input("Enter height in meter = "))
except Exception:
    pass

bmi = weightInKilograms / (heightInMeters * heightInMeters)
print("bmi = "+str(bmi))
if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else:
    print("Obese")