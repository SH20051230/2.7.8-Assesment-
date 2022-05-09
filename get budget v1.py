# This is a simple program asking user's max budget available
def float_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")


budget = float_checker("what's your highest available budget?: ")

