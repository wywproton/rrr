import PySimpleGUI as sg

layout = [
    [sg.Text('Hello world!')],
    [sg.Button('Click me!')]
]

window = sg.Window('My Window', layout)

buttons = [sg.Button('Button 1'), sg.Button('Button 2'), sg.Button('Button 3')]
window.add_components(buttons)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    print(event, values)

window.close()
