# I have modified the previous version as I found that float division can't be 0
# I have added selection statement in this version to ensure all inputs (both price and units) are > 0
def Budget_checker(question):
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print("Please enter an integer")



def price_per_unit_cal():
    units = Budget_checker("Please enter the amount of units: ")
    while units <= 0:   # This loops out the choice of 0 and - values
        units = Budget_checker("Please enter a valid number (It can not be 0): ")

    price = Budget_checker("Please enter the product price: ")
    while price <= 0:   # So is the price
        price = Budget_checker("Please enter a valid product price (it can not be 0): ")

    price_per_unit = price / units
    return price_per_unit




# Main routine
Price_per_unit = price_per_unit_cal()
print(f"The price per unit for this product is ${Price_per_unit}")
# Output the data when calculated
