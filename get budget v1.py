# This is a simple program asking user's max budget available
# The function that check both integers and decimals are valid
def Budget_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")

# Main routine
budget = Budget_checker("what's your highest available budget?: ")

