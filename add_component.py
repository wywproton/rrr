import PySimpleGUI as sg

layout = [
    [sg.Text('Hello world!')],
    [sg.Button('Click me!')]
]

window = sg.Window('My Window', layout)

button = sg.Button('Another button')
window.add_component(button)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    print(event, values)

window.close()
