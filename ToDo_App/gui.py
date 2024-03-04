import functions
import PySimpleGUI as sg
import time

sg.theme('DarkPurple')

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('To-Do App',
                   layout=[[clock],
                           [label],
                           [inputBox, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 15))

while True:
    event, value = window.read(timeout=60000)
    window['clock'].update(value=time.strftime("%H:%M    %B %d, %Y"))
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = value['todos'][0]
                new_todo = value['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo + "\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please, select a todo", font=('Helvetica', 15))

        case "Complete":
            try:
                todo_to_complete = value['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please, select a todo", font=('Helvetica', 15))

        case "Exit":
            break

        case "todos":
            window['todo'].update(value=value['todos'][0])

        case sg.WINDOW_CLOSED:
            break

window.close()
