# August 1st Goals - Git Branch Checkout, Match Case +
from unittest import case


# Get Input Function
def get_input():
    start = True
    todos = []
    while start:
        user_prompt = input("Please choose to add, print, edit or exit ")
        sanitized_input = user_prompt.lower()
        todos, start = return_answer(todos, sanitized_input)
    print("Here is your final list, goodbye: ")
    print_list(todos)

# Determine Case Function
# Options 1 - Add 2 - Print 3 - Quiet

def return_answer(list , answer):
    selection = answer
    match selection:
        case 'add':
            todo = input("Enter a new To Do Item: ")
            list.append(todo)
            return list, True
        case 'print':
            print_list(list)
            return list, True
        case 'edit':
            return edit_list(list)
        case 'exit':
            print("Here is your to do list:")
            return list, False
        case _:
            print("Your entry did not match one of the options. Please try again.")
            return list, True



#Edit Function
# Pass ToDo List / Select Item / Edit or delete item?
def edit_list(list):
    print("Here is your list: ")
    print_list(list)
    number = input("Please select which item to edit")
    # note - I have no way to catch an error yet
    # compare while statement forcing a number
    while int(number) > len(list)+1:
        print("You did not enter a valid number. Please try again")
        number = input("Please enter the numbered item to edit")
    edit_variable = input("Please enter your new variable")
    #list.insert(int(number)-1, edit_variable)
    list[int(number)-1] = edit_variable
    return list, True






# For Loop Function
def print_list(list):
    # added a counter
    counter = 1
    for x in list:
        print(counter, x)
        counter += 1


get_input()