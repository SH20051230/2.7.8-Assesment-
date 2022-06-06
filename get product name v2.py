# I have modfied the function
# So the error messages stay togather with the question in the main routine
# The function then can be reused in other time
def not_blank(question, error_messages):
    valid = ""
    while not valid:
        response = input(question)
        if not response():
            print(error_messages)
        else:
            return response


# Main routine
product_name = not_blank("what's the name of your product that you want to compared?: ",
                         "You can't leave this blank")
