# This is just a version of my testing
# This code does not include in the assesment

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
    while units == 0:   # This loops out the choice of 0
        units = Budget_checker("Please enter a valid number (It can not be 0): ")

    price = Budget_checker("Please enter the product price: ")
    while price == 0:   # Same for price
        price = Budget_checker("Please enter a valid product price (it can not be 0): ")

    price_per_unit = price / units
    return price_per_unit




def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank, and please enter a name with alpha characters")
        else:
            return response



def unit_checker(question, valid_unit):
    unit_error = "Please enter a valid unit such as g/kg or l/ml or check your spelling"
    unit_choice = input("what unit do you want to compared in?: ").lower()
    for unit in valid_units:
        if unit_choice in unit:
            unit_choice = unit[0].title()
            return unit_choice

    print(unit_error)
    return unit_checker(question, valid_unit)



# Main routine
valid_units = [["kg", "kilograms", "kilo"], ["g", "grams", "gr"], ["l", "litres", "lit"],
               ["ml", "millilitres"]]
name_list = []
unit_price_list = []
products_details = []
details_list = []
valid_list = False
# While loop for multiple products test (this will be developed further as another component)
# "X" is the break key
budget = Budget_checker("what's your highest avaliable budget? ")
while not valid_list:
    # All information needed under the while loop
    product_name = not_blank("what's the name of the product? ")
    products_details.append(product_name)
    unit_compared = unit_checker("what unit do you want to compared in? ", valid_units)
    Price_per_unit = price_per_unit_cal()
    products_details.append(Price_per_unit)
    print(f"The {product_name} is cost ${Price_per_unit} per {unit_compared}")
    valid = input("continue by press anything or stopped by pressing X").lower()
    details_list.append(products_details)

    # If == "X" stop the loop, anything else restart the loop
    if valid == "x":
        break
    else:
        continue

print(details_list)
# Output the data for testing purpose
for p in details_list:
    print(p[0], "cost", p[1], "dollars per unit price")

# Save one product detals as one list and then save it in to another list
# Print the list pf list 
