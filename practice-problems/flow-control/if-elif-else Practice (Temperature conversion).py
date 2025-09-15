
temp = float(input("Enter a temperature:  "))
scale = input("Celsius or Fahrneheit? (C or F):  ")

if scale == "C":    # if input was "C"
    temp = (temp * 1.8) + 32   # do this arthmetic 
    scale = "F"
    print(f"Your temperature converted is: {round(temp,1)} {scale}")  # prints out input converted to "Fahrneheit"


elif scale == "F":  # if input was "F"
    temp = (temp - 32) * 0.5556  # do this arthmetic
    scale = "C"
    print(f"Your temperature converted is: {round(temp,1)} {scale}") # prints out input converted to "Celsius"
 
else:
    print(f"Please enter a valid {scale}.")  # if all conditions skipped
