# This version I have added a limit of max budget
# This avoid the uer entering numbers that's too high
# The function that checks if the input is an integer or not
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


