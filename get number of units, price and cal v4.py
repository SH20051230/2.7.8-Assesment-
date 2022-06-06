# In this version I have rounded the output of price per units to 2dp
# As it's in $ and cents are very commonly rounded to 2dp
# And i have also merged the product name component into this version
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
    units = Budget_checker("Please enter the amount of units: ")
    while units <= 0:   # This loops out the choice of 0 and - choices
        units = Budget_checker("Please enter a valid number (It can not be 0): ")

    price = Budget_checker("Please enter the product price: ")
    while price <= 0:   # So is the price
        price = Budget_checker("Please enter a valid product price (it can not be 0): ")

    price_per_unit = price / units
    return price_per_unit


# Product name can't be blank
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank, and please enter a name with alpha characters")
        else:
            return response


# Main routine
product_name = not_blank("what's the name of your product that you want to compared?: ")
Price_per_unit = price_per_unit_cal()
print(f"The price per unit for this product is ${Price_per_unit:.2f}")
# Output the data when calculated
