# In this version i have added in my product name input
# And with the function that can check if the name is valid and not blank
# And test it make sure it's working correctly


# Functions
# check for valid input of budget entered
def Budget_checker(question, low_num, high_num):
    error_message = f"please enter a regular amount of budget between {low_num} and {high_num}"
    number = ""
    while not number:
        try:
            number = float(input(question))
            while number >= low_num and number <= high_num:
                return number
            else:
                print(error_message)
                number = None            # If the number isn't in range print error messages
        except ValueError:
            print("Please enter an integer")


# Check for valid input of unit entered
def unit_checker(question, valid_unit):
    unit_error = "Please enter a valid unit such as g/kg or l/ml or check your spelling"
    unit_choice = input("what unit do you want to compared in?: ").lower()
    for unit in valid_units:
        if unit_choice in unit:
            unit_choice = unit[0].title()
            return unit_choice

    print(unit_error)
    return unit_checker(question, valid_unit)



def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank, and please enter a name with alpha characters")
        else:
            return response




# Main routine
# Get details
budget = Budget_checker("what's your highest available budget?: ", 1, 100)
product_name = not_blank("what's the name of your product that you want to compared?: ")
unit_compared = "What unit do you want to compare in?: "
valid_units = [["kg", "kilograms", "kilo"], ["g", "grams", "gr"], ["l", "litres", "lit"],
               ["ml", "millilitres"]]
unit_choose = unit_checker("what unit do you want to compared in?; " ,valid_units)
print(f"you choose {unit_choose}")


# Loops around until escape code had been entered

# Calculation of the price per unit

# lists to store details of both unit and price

# Sorting codes that sort the list to find the cheapest choice

# Print all choices that's in range of the budget

# Print all choices that's out of the range of the budget

# Print summary details
