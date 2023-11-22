import functionsForMain
import time

now = time.strftime("%H:%M:%S     %B %d, %Y")
print ("It is ", now)

while True:
    user_choice = input("enter add, show, edit, complete or exit: ")
    user_choice = user_choice.strip()

    if user_choice.startswith('add'):
        todo = user_choice[4:] + '\n'

        todos = functionsForMain.get_todos()

        todos.append(todo)

        functionsForMain.write_todos(todos)

    elif user_choice.startswith('show'):
        todos = functionsForMain.get_todos()


        for index, item in enumerate(todos):
            item = item.strip('\n')
            raw = f"{index + 1}-{item}"
            print(raw)
    elif user_choice.startswith('edit'):
        try:
            number = int(user_choice[5:])
            number = number - 1
            todos = functionsForMain.get_todos()

            new_todo = input("enter a new todo: ")
            todos[number] = new_todo + '\n';

            functionsForMain.write_todos(todos)

        except Exception:
            print('This command is not valid')
            continue

    elif user_choice.startswith('complete'):
        try:
            index = int (user_choice[9:])

            todos = functionsForMain.get_todos()

            todo_to_remove = todos[index-1].strip('\n')
            todos.pop(index-1)

            functionsForMain.write_todos(todos)

            print(f"todo '{todo_to_remove}' was removed from the list")

        except IndexError:
            print('there is no a todo with this number')
            continue

    elif user_choice.startswith('exit'):
         break
    else:
        print("stupid boy")

print("bye")

