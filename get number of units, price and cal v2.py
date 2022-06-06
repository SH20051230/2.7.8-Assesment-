# I have modified the main routine by making the codes into a function
# Make the program easier to call when I need to calculate more than 1 times
def Budget_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")


# unit price calculator
def price_per_unit_cal():
    units = Budget_checker("Please enter the amount of units: ")  # input of both units and price
    price = Budget_checker("Please enter the product price: ")
    price_per_unit = price / units
    return price_per_unit



# Main routine
Price_per_unit = price_per_unit_cal()
print(f"The price per unit for this product is ${Price_per_unit}")
# Output the data when calculated
