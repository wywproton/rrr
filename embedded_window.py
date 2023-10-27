import PySimpleGUI as sg

# 定义主窗口
layout = [[sg.Text('This is the main window')],
          [sg.Button('Open another window', key='open_window')]]

window = sg.Window('Main Window', layout)

# 定义嵌入窗口
embedded_layout = [[sg.Text('This is an embedded window')],
                   [sg.Button('Close', key='close')]]

embedded_window = sg.Window('Embedded Window', embedded_layout, modal=True)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == 'open_window':
        # 显示嵌入窗口
        embedded_window.show()

window.close()
