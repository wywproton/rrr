import PySimpleGUI as sg

# 定义窗口布局
layout = [
    [sg.Text('Page 1')],
    [sg.Button('Next Page', key='next_page')],
    [sg.Button('Previous Page', key='prev_page')],
    [sg.Button('Exit', key='exit')]
]

# 创建窗口
window = sg.Window('Multi-Page Window', layout)

# 定义页面列表
pages = ['Page 1', 'Page 2', 'Page 3']
current_page = 0

while True:
    event, values = window.read()
    if event in (None, 'exit'):
        break
    elif event == 'next_page':
        current_page += 1
        if current_page >= len(pages):
            current_page = 0
        window['text'].update(pages[current_page])
    elif event == 'prev_page':
        current_page -= 1
        if current_page < 0:
            current_page = len(pages) - 1
        window['text'].update(pages[current_page])

window.close()
