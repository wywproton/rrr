import PySimpleGUI as sg

# 导入 PyQt5 的 UI 文件
ui_file = 'your_ui_file.ui'
ui = sg.convert_ui(ui_file, from_framework='pyqt5')

# 创建 PySimpleGUI 应用程序
window = sg.Window('My Application', ui)

# 显示 PySimpleGUI 应用程序
window.read(close=True)
