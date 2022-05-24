# In this improved version i have developed further
# By put the calculator of price per unit into a function
# Makes it easier to use whenever i want
def Budget_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")


def calculate_unit_price():




# Main routine
# Getting input of amount of unit and price
number_of_units = Budget_checker("Please enter the amount of units: ")
price = Budget_checker("Please enter the price of the product: ")
# Get the price per unit by dividing the price with the number of units
# Print the output
