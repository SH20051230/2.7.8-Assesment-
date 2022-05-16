# Imports

# Functions
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

# Main routine
budget = Budget_checker("what's your highest available budget?: ", 1, 101)
# Units to compared in

# integer checker for values

# Loops around until escape code had been entered

# Calculation of the price per unit

# lists to store details of both unit and price

# Sorting codes that sort the list to find the cheapest choice

# Print all choices that's in range of the budget

# Print all choices that's out of the range of the budget

# Print summary details
