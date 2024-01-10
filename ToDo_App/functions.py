FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Return to-does"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ Writes to-does into the file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_local)

if __name__ == "__main__":
    print(get_todos())

