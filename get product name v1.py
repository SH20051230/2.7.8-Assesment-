# This is a program that get the input of the product name from the user
# Program only continues if the user had entered a name
def not_blank(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You can't leave this blank")
        else:
            return response


# Main routine
product_name = not_blank("what's the name of your product that you want to compared?: ")
