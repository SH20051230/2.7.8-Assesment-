unit = input("What unit you want to compared in? eg: g/kg: ").lower()
valid_unit = ["g", "kg", "l", "ml"]
while unit not in valid_unit:
    print("please enter a valid unit eg: g/kg or l/ml")
else:
    print(f"valid input you are comparing in {unit}")
