# Modify match_case to include a pre-determined # of items
# Goal is to add an option to edit, presumably it means to select, remove, delete?

# August 1st Goals - Git Branch Checkout, Match Case +
from unittest import case


# Get Input Function
def get_input():
    start = True
    todos = []
    while start:
        user_prompt = input("Please select an option: ")
        sanitized_input = user_prompt.lower()
        todos, start = return_answer(todos, start, sanitized_input)
    print("Here is your final list, goodbye: ")
    print_list(todos)

# Determine Case Function
# Options 1 - Add 2 - Print 3 - Quiet

def return_answer(list, value , answer):
    selection = answer
    match selection:
        case 'add':
            todo = input("Enter a new To Do Item: ")
            list.append(todo)
            return list, True
        case 'print':
            print_list(list)
            return list, True
        case 'exit':
            print("Here is your to do list:")
            return list, False

#For Loop Function
def print_list(list):
    for x in list:
        print(x)


get_input()