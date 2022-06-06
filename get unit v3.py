# This is a program that gets the unit need to be compared
# In this version I have added a few more choices of the units
# by including its full name and other short ways of write it
# And changed the testing in the main routine to an ordinary input
def unit_checker(question, valid_unit):
    unit_error = "Please enter a valid unit such as g/kg or l/ml or check your spelling"
    unit_choice = input("what unit do you want to compared in?: ").lower()
    for unit in valid_units:
        if unit_choice in unit:
            unit_choice = unit[0].title()
            return unit_choice

    print(unit_error)
    return unit_checker(question, valid_unit)


# This list contains all valid units for now
# more can be added if required in the future
# Main routine
unit_compared = "What unit do you want to compare in?: "
valid_units = [["kg", "kilograms", "kilo"], ["g", "grams", "gr"], ["l", "litres", "lit"],
               ["ml", "millilitres"]]
unit_choose = unit_checker("what unit do you want to compared in?; ", valid_units)
print(f"you choose {unit_choose}")
