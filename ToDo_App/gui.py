import functions
import PySimpleGUI as sg


label = sg.Text("Type in a to-do")
inputBox = sg.InputText(tooltip="Enter a to-do")
add_button = sg.Button("Add")

window = sg.Window('To-Do App', layout=[[label], [inputBox, add_button]])
window.read()
print("hello")
window.close()
