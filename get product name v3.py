# I have used other method to prevent user entering blank inputs
# Which is .isalpha function
# It forces the user must enter at least one alpha character
# which match the purpose of this component
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("you can't leave this blank and please enter a name with alpha characters")
        else:
            return response


# Main routine
product_name = not_blank("what's the name of your product that you want to compared?: ")
