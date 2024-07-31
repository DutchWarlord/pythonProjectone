# functions

# def control_loop():
#     while True:
#         user_prompt = "Enter a todo: "
#         todos = []
#         sanitized = user_prompt.lower()
#         if sanitized != "exit":
#             todos.append(sanitized)
#         else:
#             print(todos)
#             return False


def control_loop():
    todos = []  # Move this outside of the loop
    while True:
        user_prompt = input("Enter a todo (or type 'exit' to quit): ")  # Get user input
        sanitized = user_prompt.lower()
        if sanitized == "exit":
            break  # Exit the loop
        todos.append(sanitized)  # Add the todo to the list

    print(todos)  # Print the list of todos after exiting the loop



control_loop()
