# This is a program get the input of the number of units and price
# And it will calculate the average after above two inputs had been entered
# This is the integer checker from previous development
def Budget_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")


# Main routine
# Getting input of amount of unit and price
number_of_units = Budget_checker("Please enter the amount of units: ")
price = Budget_checker("Please enter the price of the product: ")
price_per_unit = price / number_of_units
# Get the price per unit by dividing the price with the number of units
# Print the output
print(f"The price per unit is:{price_per_unit}$")
