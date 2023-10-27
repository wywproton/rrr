'''PySimpleGUI是一个基于PyQt5的Python GUI库，可以使用PyQt5 Designer生成的界面代码。
以下是一个简单的示例，演示如何使用PySimpleGUI导入PyQt5 Designer生成的界面代码：

首先，使用PyQt5 Designer创建一个名为`my_ui.ui`的界面文件，并保存到磁盘上。

然后，使用PySimpleGUI导入该界面文件，并创建一个新的PySimpleGUI窗口：'''
```python
import sys
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PySimpleGUI import Window, Button

# 从my_ui.ui文件中加载界面
with open("my_ui.ui", "r") as f:
    ui = loadUi(f)

# 创建一个新的PySimpleGUI窗口
window = Window("My Window", size=(640, 480))

# 将PyQt5 Designer生成的界面添加到PySimpleGUI窗口中
window.add(ui)

# 创建一个按钮，用于关闭窗口
button = Button("Close")
button.clicked.connect(lambda: window.close())
window.add(button)

# 显示窗口
window.show()

sys.exit(app.exec_())
'''
在上面的示例中，我们首先使用`loadUi()`函数从`my_ui.ui`文件中加载界面。
然后，我们创建一个新的PySimpleGUI窗口，并将PyQt5 Designer生成的界面添加到窗口中。
最后，我们创建一个按钮，用于关闭窗口，并将其添加到窗口中。

请注意，在使用PySimpleGUI导入PyQt5 Designer生成的界面代码时，
需要确保PySimpleGUI版本与PyQt5版本相匹配。否则，可能会出现兼容性问题。
'''
