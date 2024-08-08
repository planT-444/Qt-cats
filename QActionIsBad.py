from functools import partial
from PySide2.QtCore import (
    QRect, QSize
)
from PySide2.QtWidgets import (
    QMainWindow, QWidget, QLabel, QToolBar, QPushButton, QAction, QHBoxLayout, QGridLayout
)
from PySide2.QtGui import (
    QPixmap
)

class MyQAction(QAction):
    def __init__(self, text, parent=None):
        super(MyQAction, self).__init__(text, parent)

    def event(self, evt):
        print(evt)
        return True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # configure window
        self.setWindowTitle("die katzen")
        self.setMinimumSize(QSize(1500, 1000))

        # initialize toolbar and image container
        toolbar = QToolBar()
        toolbar.setFixedSize(QSize(1980, 30))
        toolbar.setMovable(False)
        toolbar.setFloatable(False)
        self.toolbar_cmds = ("toggle", "wot", "poop", "stinky")
        self.toolbar_buttons = {}

        image_layout = QGridLayout()
        self.image_dict = {}
        self.shown_images = {}

        # load toolbar and data
        for cmd in self.toolbar_cmds:
            new_button = MyQAction(cmd, self)
            new_button.setCheckable(False)
            new_button.setChecked(False)
            self.toolbar_buttons[cmd] = new_button
            toolbar.addAction(new_button)
            toolbar.addSeparator()
            if cmd != "toggle":
                new_button.installEventFilter(self)
                image = QPixmap(QSize(200, 150))
                image.load(f"./images/{cmd}.png")
                image_label = QLabel()
                image_label.setPixmap(image)
                image_layout.addWidget(image_label)
                self.image_dict[cmd] = image_label
                print(cmd)
                new_button.toggled.connect(partial(self.action_toggled, cmd))
                new_button.hovered.connect(partial(self.action_clicked, cmd))
                # new_button.hovered.connect(partial(self.show_image, cmd))
                image_label.hide()

        self.addToolBar(toolbar)
        image_widget = QWidget()
        image_widget.setLayout(image_layout)
        self.setCentralWidget(image_widget)

    @property
    def toggle(self):
        return self.toolbar_buttons["toggle"].isChecked()

    def action_toggled(self, cmd: str, checked):
        # print(cmd, checked)
        # button = self.toolbar_buttons[cmd]
        # image = self.image_dict[cmd]
        # if self.toggle:
        #     if self.toolbar_buttons[cmd].isChecked():
        #         image.show()
        #     else:
        #         image.hide()
        #
        # else:
        #     image.hide()
        #     button.setChecked(False)
        pass

    def action_clicked(self, cmd):
        pass
        # print(cmd, "hovered")
        # image = self.image_dict[cmd]
        # if not self.toggle:
        #     image.show()

    # def eventFilter(self, obj, event):
    #     print(obj.text())
    #     print(event.type())
    #     if event.type() == event.MouseButtonRelease:
    #         if isinstance(obj, QAction):
    #             print("Action released")
    #     return super().eventFilter(obj, event)
