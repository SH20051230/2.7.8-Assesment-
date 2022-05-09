# This is a simple program asking user's max budget available
# The function that force the user to enter a budget
def not_blank(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You need to enter the budget you would like to spent: ")
        else:
            return response


# Main routine
budget = not_blank("what's your highest available budget?: ")

