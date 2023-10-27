import PySimpleGUI as sg
from PyQt5.QtWidgets import QApplication, QMainWindow

# 导入 PyQt5 Designer 设计的 UI 文件
ui_file = 'your_ui_file.ui'

# 创建一个 PyQt5 应用程序
app = QApplication([])

# 加载 PyQt5 Designer 设计的 UI 文件
window = QMainWindow()
window.setWindowTitle('My Application')
window.setGeometry(300, 300, 300, 200)

# 将 PyQt5 Designer 设计的 UI 文件转换为 PySimpleGUI 可以使用的格式
ui = sg.QtWidgets.QUiLoader().load(ui_file)

# 将 PySimpleGUI 的 UI 对象添加到 PyQt5 应用程序中
window.setCentralWidget(ui)

# 显示 PyQt5 应用程序
window.show()

# 运行 PySimpleGUI 应用程序
sg.Window('My Application').read(close=True)
