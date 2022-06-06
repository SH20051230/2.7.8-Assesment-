# Added in component of number of units, price and calculation of price per unit
# Fixed component to merge into base
# Test and ensure it's working
# Functions
# check for valid input of budget entered
def Budget_checker(question, low_num, high_num):
    error_message = f"please enter a regular amount of budget between {low_num} and {high_num}"
    number = ""
    while not number:
        try:
            number = float(input(question))   # float includes decimals numbers
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


# product name can't be blank
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank, and please enter a name with alpha characters")
        else:
            return response


# unit price calculator
def price_per_unit_cal():
    price = number_checker("what's the price of the product?: ")
    units = number_checker("what's the amount of units: ")
    while price and units == 0:
        int(input("please re enter the amount"))

    price_per_unit = price / units
    return price_per_unit


# This is a normal integer checker that differ from the budget checker
# As it doesn't include the limits of budget from 1 to 100
def number_checker(question):
    number = ""
    while not number:
        try:
            answer = float(input(question))
            return answer
        except ValueError:
            print("Please enter an integer, eg:5")

# Main routine
# Get details
budget = Budget_checker("what's your highest available budget?: ", 1, 100)
# list to store all available valid units
valid_units = [["kg", "kilograms", "kilo"], ["g", "grams", "gr"], ["l", "litres", "lit"],
               ["ml", "millilitres"]]
unit_choose = unit_checker("what unit do you want to compared in?; ",valid_units)
print(f"you choose {unit_choose}")
# Calculation of the price per unit
Price_per_unit = price_per_unit_cal()
print(f"The price per unit for this product is ${Price_per_unit:.2f}")
# Loops around until escape code had been entered

# Calculation of the price per unit

# lists to store details of both unit and price

# Sorting codes that sort the list to find the cheapest choice

# Print all choices that's in range of the budget

# Print all choices that's out of the range of the budget

# Print summary details
