import PyQt5.QtCore
import PyQt5.QtWidgets
import PySimpleGUI as sg

# 导入 PyQt5 Designer 设计的 UI 文件
ui_file = 'your_ui_file.ui'

# 使用 PyQt5 解析 UI 文件
ui = PyQt5.QtCore.QMetaObject.from_file(ui_file)

# 将 UI 文件转换为 PySimpleGUI 可以使用的格式
ui_dict = {}
for widget in ui.children():
    if isinstance(widget, PyQt5.QtWidgets.QWidget):
        ui_dict[widget.objectName()] = widget

# 创建 PySimpleGUI 应用程序
window = sg.Window('My Application', ui_dict)

# 显示 PySimpleGUI 应用程序
window.read(close=True)
