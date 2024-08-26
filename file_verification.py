# Add a function to verify a file is a string (before/after)
# Add error handling for file path changes
# Consider Doing Error Catching?

# August 1st Goals - Git Branch Checkout, Match Case +
from unittest import case


# verify file exists
def verify_file(file_path):
    if not os.path.isfile(file_path):
        print("File not found")
        return false

# Get Input Function
def get_input():
    start = True
    file1 = 'example.txt'
    if not verify_file(file1):
        print("File not found")
        return
    while start:
        user_prompt = input("Please choose to add, print, edit or exit:  ")
        sanitized_input = user_prompt.lower()
        file1, start = return_answer(file1, sanitized_input)
    print("Here is your final list, goodbye: ")
    print_list(file1)


# Sanitize Input Function
# To take user in put for Add/Print/Edit/Delete and return a single letter. Not sure if worthwhile


# Determine Case Function
# Options 1 - Add 2 - Print 3 - Quiet

def return_answer(file1, answer):
    selection = answer
    match selection:
        case 'add':
            return add_item(file1)
        case 'print':
            print_list(file1)
            return file1, True
        case 'edit':
            return edit_list(file1)
        case 'exit':
            print("Here is your to do list:")
            return file1, False
        case _:
            print("Your entry did not match one of the options. Please try again.")
            return file1, True


# Add function
# Added Loop to continue adding another rather than returning
def add_item(file1):
    status = True
    while status:
        todo = input("Enter a new To Do Item: ")
        with open(file1, 'a') as file:
            file.write(str(todo) + '\n')
        question = input("Would you like to add another? Y/N ")
        if question.upper() == 'N':
            status = False
    return file1, True


# Edit Function
# Pass ToDo List / Select Item / Edit or delete item?
# Edit - Take file, write to list, present items, edit list, re-write list to file
# Ensure items can be selected by name?
def edit_list(file1):
    print("Here is your list: ")
    print_list(file1)
    entry = input("Please select which item to edit")
    number = int(entry)
    # I need to read out a particular line, and then edit, and re-insert it.
    # I could even add an if else statement to determine whether string / number
    with open(file1, 'r') as file:
        lines = file.readlines()
        lines_length = len(lines)
        while number > lines_length - 1 or number < 0:
            entry = input("That number wasn't present on the list. Please enter another: ")
            number = int(entry)
        new_entry = input("Please type your new entry: ")
        lines[number] = new_entry + '\n'
        with open(file1, 'w') as file:
            file.writelines(lines)
    print("The list has been updated")
    # while int(number) >= len(list):
    #     print("You did not enter a valid number. Please try again")
    #     number = input("Please enter the numbered item to edit")
    # edit_variable = input("Please enter your new variable")
    # # list.insert(int(number)-1, edit_variable)
    # list[int(number)] = edit_variable
    return file1, True


# For Loop Function
def print_list(file1):
    # open and read file
    with open(file1, 'r') as file:
        # enumerate over the lines to get index and content
        for index, line in enumerate(file):
            # print the content items line by line
            print(f"{index} : {line.strip()}")
    # added a counter
    # counter = 1
    # for x in list:
    #     print(counter, x)
    #     counter += 1


# Advanced challenge - Re-order items!

get_input()
