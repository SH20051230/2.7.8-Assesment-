# Copied version of Code
# This is for append details to list and while loop to get more product details
# Main routine
all_products = []
valid_list = False
while not valid_list:
    product_item = []   # The list that holds each product details
    product_name = input("what's the product name: or press x to terminate the program")
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
        product_cost = float(input(f"what's the price of {product_name}: $"))  # Get the price of the product
        product_item.append(product_cost)    # Add price to the list
        print()
        # Get the unit amount of the product
        product_qty = int(input(f"how much {product_name} are you buying (eg: qty or mls, gms or kgs etc): "))
        product_item.append(product_qty)
        unit_value = product_cost/product_qty  # calculate the unit price
        product_item.append(unit_value)  # append details to list
        print()
        all_products.append(product_item)  # add items list into the main list
        print(all_products)  # print the main list
