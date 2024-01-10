import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("Add")

window = sg.Window('To-Do App',
                   layout=[[label], [inputBox, add_button]],
                   font=('Helvetica', 15))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = value['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()
