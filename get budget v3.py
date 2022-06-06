# In this Second Trial I have changed the parameters of the function
# I had put the error message and limits in side the main Routine
# Leaving only interger checker on top
def Budget_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")


# Main routine
# Put the limit in the main routine and loop around until lower or equal to 100
Max_budget = 100
budget = Budget_checker("what's your highest available budget?: ")
# keep looping around until the input is in range
while budget > 100:
    print("Please enter a regular number between 1 and 100: ")
    budget = Budget_checker("what's your highest available budget?: ")








