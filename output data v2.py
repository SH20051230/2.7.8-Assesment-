# merged version with my own functions and developed further
# This is for append details to list and while loop to get more product details components
# I have changed some inputs with my functions in order to work
# on unexpected inputs
# Functions

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





valid_units = [["kg", "kilograms", "kilo"], ["g", "grams", "gr"], ["l", "litres", "lit"],
               ["ml", "millilitres"]]
# Main routine
all_products = []
valid_list = False
while not valid_list:
    product_item = []   # The list that holds each product details
    product_name = not_blank("what's the name of the product")
    product_item.append(product_name)
    print()
    if product_name == "x":  # Break the loop when x entered
        valid_list = True
        all_products.sort(key=lambda x: x[3])   # sort list by unit price put cheapest at position 0
        print(f"we recommend {all_products[0][0]} at {all_products[0][3]} per unit price as the best choice\n"
              f"The full list had been printed below: \n")
        for i in all_products:
            print(f"{i[2]} units of {i[0]} at ${i[3]} per unit")
    else:   # If more items had been added
        product_cost = Budget_checker(f"what's the price of {product_name}: $")  # Get the price of the product
        product_item.append(product_cost)    # Add price to the list
        print()
        # Get the unit and unit amount of the product
        unit_compared = unit_checker("what unit do you want to compared: ", valid_units)
        print(f"you choose {unit_compared}")
        product_qty = Budget_checker(f"how much {product_name} are you buying (eg: qty or mls, gms or kgs etc): ")
        product_item.append(product_qty)
        unit_value = product_cost/product_qty  # calculate the unit price
        product_item.append(unit_value)  # append details to list
        print()
        all_products.append(product_item)  # add items list into the main list
        print("This is the current list of items")
        print(all_products)  # print the main list
