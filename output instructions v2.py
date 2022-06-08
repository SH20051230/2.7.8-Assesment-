# This is based on v1
# I have made the show_instructions component into its own function

def show_instructions():
        instructions = ""
        # While loop that loops out invalid choice
        while not instructions:
            instructions = not_blank("Do you wish to read the instructions? ").lower()
            instructions = choice_checker(instructions, valid_yes_no)
        # If they want to read it, output the instructions
        if instructions == "Y":
            print("\n******************************************************************************************\n"
                  "\n\t**** Price evaluator Instructions ****\n\t"
                  "\nYou will be asked to enter the amount of budget you can use to purchase your items\n"
                  "but there is a limit of max 100 as values over that isn't logical as the purpose of this\n"
                  "program is to service the local community of the daily purchasing\n"
                  "\nAnd you will then need to enter the name of the product you are comparing,\n"
                  "the price of the product you are comparing,\n"
                  "the unit you want to compared in and how much of that units\n"
                  "\nThen it will repeat this process until you have entered all products you want to compare\n"
                  "When you want to stop the program, simply press x as the break key\n"
                  "then the program will print out a list of all your products sort from the cheapest\n"
                  "to the most expensive, and we also give out which of them is the best choice\n"
                  "\n******************************************************************************************\n")
        # otherwise just launch the program without the instructions
        print("Program launches...")

# The answer can't be blank
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("you can't leave this blank and please enter a name with alpha characters")
        else:
            return response


# This is the checker that used to check the choices are valid or not
def choice_checker(choice, valid_yes_no):
    choice_error = "Sorry that's not a valid choice, or check your spelling\n"\
                   "valid choices are yes, y, n and no\n"
    for list_item in valid_yes_no:
        if choice in list_item:
            instruction_choice = choice[0].title()
            return instruction_choice

    print(choice_error)



valid_yes_no = [["y", "yes"],["no", "n"]]
show_instructions()
