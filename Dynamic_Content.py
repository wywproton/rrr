import PySimpleGUI as sg

layout = [
    [sg.Output(size=(30, 10), key='-output-')],
    [sg.Input( key='-text-'),sg.Button('Update', key='update')],
]

window = sg.Window('Dynamic Content', layout)
t=''
while True:
    event, values = window.read()
    if event == 'update':
        t=t+'\n'+values['-text-']
        print(event,values)
        window['-output-'].update(t)
        window['-text-'].update(value='')
    elif event is None:
        break

window.close()
