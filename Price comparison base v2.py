# In this version i have merged my budget checker function inside it
# And tested to make sure it's working correctly as expected

# Imports

# Functions
def Budget_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")


budget_range = range(1, 101)
budget = Budget_checker("what's your highest availble budget?: ")
while not 1 <= budget <= 100:
    error_message = f"please enter a regular amount of budget between 1 and 100"
    print(error_message)
    budget = Budget_checker("what's your highest available budget")
# Main routine
budget = Budget_checker("what's your highest available budget?: ")
# Units to compared in

# integer checker for values

# Loops around until escape code had been entered

# Calculation of the price per unit

# lists to store details of both unit and price

# Sorting codes that sort the list to find the cheapest choice

# Print all choices that's in range of the budget

# Print all choices that's out of the range of the budget

# Print summary details
