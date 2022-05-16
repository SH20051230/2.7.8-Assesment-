# From the previous trial i have decided to developed further on this trial
# I have changed the parameters of the function and put it as a range in the main routine
# The parameters then can be used for other purposes
def Budget_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")

# Main routine
budget_range = range(1, 101)
budget = Budget_checker("what's your highest availble budget?: ")
while not 1 <= budget <= 100:
    error_message = f"please enter a regular amount of budget between 1 and 100"
    print(error_message)
    budget = Budget_checker("what's your highest available budget")


