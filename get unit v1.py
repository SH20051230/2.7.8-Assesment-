# This is a program that gets the unit need to be compared
def unit_checker():
    unit_error = "Please enter a valid unit such as g/kg or l/ml"
    valid_units = [["kg"], ["g"], ["l"], ["ml"]]
    unit_choice = input("what unit do you want to compared in?: ").lower()
    for unit in valid_units:
        if unit_choice in unit:
            unit_choice = unit[0].title()
            return unit_choice

    print(unit_error)
    return unit_checker()


# Main routine
# This is just for testing purposes
for test in range(6):
    print(f"you choose {unit_checker()}")
