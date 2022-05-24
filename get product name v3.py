# So in this third iteration i have put the error messages back in to the function
# By adding isalpha in the function to make sure at least one alpha character is entered
# which also prevented the user entering numbers space to escape this
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You can't leave this blank, and please enter a name with alpha characters")
        else:
            return response


# Main routine

product_name = not_blank("what's the name of your product that you want to compared?: ")
