FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of todos."""
    with open(filepath, 'r') as file_local:
            todo_local =  file_local.readlines()
    return todo_local

def save_todos(todos, filepath=FILEPATH):
    """ Write the todos into the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("function")