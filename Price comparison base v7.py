


# Functions
# check for valid input of budget entered
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


# Check for valid input of unit entered
def unit_checker(question, valid_unit):
    unit_error = "Please enter a valid unit such as g/kg or l/ml or check your spelling"
    unit_choice = input("what unit do you want to compared in?: ").lower()
    for unit in valid_units:
        if unit_choice in unit:
            unit_choice = unit[0].title()
            return unit_choice

    print(unit_error)
    return unit_checker(question, valid_unit)


def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank, and please enter a name with alpha characters")
        else:
            return response


def price_per_unit_cal():
    price = number_checker("what's the price of the product?: ")
    units = number_checker("what's the amount of units: ")
    while price and units == 0:
        int(input("please re enter the amount"))

    price_per_unit = price / units
    return price_per_unit


# This is a normal integer checker that differ from the budget checker
# As it doesn't include the limits of budget from 1 to 100
def number_checker(question):
    number = ""
    while not number:
        try:
            answer = float(input(question))
            return answer
        except ValueError:
            print("Please enter an integer, eg:5")





# Main routine
# Get details
budget = Budget_checker("what's your highest available budget?: ", 1, 101)
# list to store all available valid units
valid_units = [["kg", "kilograms", "kilo"], ["g", "grams", "gr"], ["l", "litres", "lit"],
               ["ml", "millilitres"]]
# Calculation of the price per unit
# Loops around until escape code had been entered
all_products = []
valid_list = False
while not valid_list:
    # lists to store details of both unit and price
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
        product_cost = number_checker(f"what's the price of {product_name}: $")  # Get the price of the product
        product_item.append(product_cost)    # Add price to the list
        print()
        # Get the unit and unit amount of the product
        unit_choose = unit_checker("what unit do you want to compared in?; ", valid_units)
        print(f"you choose {unit_choose}")
        product_qty = number_checker(f"how much {product_name} are you buying (eg: qty or mls, gms or kgs etc): ")
        product_item.append(product_qty)
        unit_value = product_cost/product_qty  # calculate the unit price
        product_item.append(unit_value)  # append details to list
        print()
        all_products.append(product_item)  # add items list into the main list
        print("This is the current list of items, (name, price, units and unit price")
        print(all_products)  # print the main list

# Print all choices that's in range of the budget

# Print all choices that's out of the range of the budget

# print(f"The price per unit for this product is ${Price_per_unit:.2f}")
