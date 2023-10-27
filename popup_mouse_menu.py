import PySimpleGUI as sg

layout = [
    [sg.Table(values=[['Alice', 'Bob'], ['Charlie', 'David']], headings=['Name', 'Age'])],
    [sg.PopupMenu(values=['Option 1', 'Option 2', 'Option 3'], key='popup')]
]

window = sg.Window('Table with Popup Menu', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == 'popup':
        print(f'Selected option: {values["popup"]}')

window.close()
