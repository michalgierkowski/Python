

weight = float(input("Enter your weight:  "))
unit = input("Kilograms or pounds? (K or L):  ")

if unit == "K":   # if unit entered was kilograms
    weight *= 2.20    # weight gets times by 2.20
    unit = "Lbs."    # gives answer in pounds
    print(f"Your weight is: {(round(weight))}{unit}") # final result
elif unit == "L": # if unit entered was pounds
    weight /= 2.20 # weight gets divided by 2.20
    unit = "Kgs."  # gives answer in kilograms
    print(f"Your weight is: {(round(weight))}{unit}") # final result
else:
    print(f"{unit} was not valid")  # if no unit entered

# Remember to order these the way you want them to be outputted

