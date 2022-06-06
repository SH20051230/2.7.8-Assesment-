# This is a program that gets the unit need to be compared
# In this version i have developed the program further
# By making generic variable name so it makes the function more flexible
# And it can be used to check valid units for any lists
def unit_checker(question, valid_unit):
    unit_error = "Please enter a valid unit such as g/kg or l/ml"
    unit_choice = input("what unit do you want to compared in?: ").lower()
    for unit in valid_units:
        if unit_choice in unit:
            unit_choice = unit[0].title()
            return unit_choice

    print(unit_error)
    return unit_checker(question, valid_unit)


# Main routine
# This is just for testing purposes
unit_compared = "What unit do you want to compare in?: "
valid_units = [["kg"], ["g"], ["l"], ["ml"]]
for test in range(6):
    print(f"you choose {unit_checker(unit_compared, valid_units)}")
