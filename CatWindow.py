from functools import partial
from PySide2.QtCore import (
    QRect, QSize
)
from PySide2.QtWidgets import (
    QMainWindow, QWidget, QLabel, QToolBar, QPushButton,
    QToolButton, QHBoxLayout, QGridLayout, QDialog
)
from PySide2.QtGui import (
    QPixmap, QMovie
)

class CatWindow(QMainWindow):
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

        self.toolbar_cmds = ("toggle", "wot", "poop", "stinky", "vibingcat")
        self.toolbar_buttons = {}

        widget_layout = QHBoxLayout()
        file_formats = (None, "png", "png", "png", "gif")
        image_formats = ("png")
        animated_formats = ("gif")
        self.image_dict = {}
        self.shown_images = {}

        # load toolbar and data
        for file_format, cmd in zip(file_formats, self.toolbar_cmds):
            print(file_format, cmd)
            new_button = QToolButton()
            new_button.setText(cmd)
            new_button.setCheckable(False)
            new_button.setChecked(False)
            self.toolbar_buttons[cmd] = new_button
            toolbar.addWidget(new_button)
            toolbar.addSeparator()
            if cmd == "toggle":
                new_button.setCheckable(True)
                new_button.toggled.connect(self.toggle_toggle)
            else:
                label = QLabel()
                if file_format in image_formats:
                    # load image into QLabel
                    image = QPixmap()
                    image.load(f"./data/{cmd}.{file_format}")
                    label.setPixmap(image)
                else:
                    print("loading animation!")
                    animation = QMovie(f"./data/{cmd}.{file_format}")
                    animation.start()
                    label.setMovie(animation)

                label.hide()
                widget_layout.addWidget(label)
                self.image_dict[cmd] = label

                # map buttons to signals
                new_button.pressed.connect(partial(self.button_down, cmd))
                new_button.released.connect(partial(self.button_up, cmd))
                new_button.toggled.connect(partial(self.button_toggled, cmd))


        self.addToolBar(toolbar)
        image_widget = QWidget()
        image_widget.setLayout(widget_layout)
        self.setCentralWidget(image_widget)

    @property
    def toggle(self):
        return self.toolbar_buttons["toggle"].isChecked()

    def toggle_toggle(self, checked):
        print("toggling", checked)
        for cmd in self.toolbar_cmds[1:]:
            button = self.toolbar_buttons[cmd]
            button.setChecked(False)
            button.setCheckable(checked)
            if not checked:
                self.image_dict[cmd].hide()



    def button_down(self, cmd):
        if not self.toggle:
            self.image_dict[cmd].show()

    def button_up(self, cmd):
        if not self.toggle:
            self.image_dict[cmd].hide()

    def button_toggled(self, cmd, checked):
        image_label = self.image_dict[cmd]
        if checked:
            image_label.show()
        else:
            image_label.hide()
