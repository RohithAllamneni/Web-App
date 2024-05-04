FILEPATH = "todos.txt"
def read_todos(filename = FILEPATH):
    """
    Reads a text file and returns the items as a list
    """

    with open(filename, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local




def write_todos(todos_arg,filepath = FILEPATH):
    """Writes the todos items into todos.txt"""

    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(read_todos())