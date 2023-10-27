import PySimpleGUI as sg

layout = [
    [sg.Text('Hello, world!')],
    [sg.Button('Update', key='update')],
    [sg.Output(size=(30, 10))]
]

window = sg.Window('Dynamic Content', layout)

while True:
    event, values = window.read()
    if event == 'update':
        window['output'].update(values['text'])
    elif event is None:
        break

window.close()
