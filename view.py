from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QPushButton, QToolButton, QSizePolicy
from PyQt5 import QtCore
import time

class GridLayout(QGridLayout):
    def __init__(self):
        super().__init__()

        self.labels = [[QLabel("0") for i in range(6)] for i in range(6)]
        for row in self.labels:
            for lb in row:
                lb.setStyleSheet(
                    "font-size : 25px;"
                    "background-color : hsl({0:0.0f}, 0%, 100%);"
                    "min-width: 120px;"
                    "min-height: 120px;"
                        .format(10, 20)
                )
                lb.setAlignment(QtCore.Qt.AlignCenter)

        for i in range(6):
            for j in range(6):
                self.addWidget(self.labels[i][j], i, j)

    def setN(self, n):
        for i in range(6):
            for j in range(6):
                self.labels[i][j].setVisible(False)
        for i in range(n):
            for j in range(n):
                self.labels[i][j].setVisible(True)


class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 30)
        size.setWidth(max(size.width(), size.height()))
        return size


class mainView(QWidget) :
    def __init__(self, parent=None):
        super().__init__(parent)

        scoreLabel = QLabel("score")
        scoreLabel.setStyleSheet('font-size: 12pt;')
        scoreEdit = QLineEdit()
        tryLabel = QLabel("try")
        tryLabel.setStyleSheet('font-size: 12pt;')
        tryEdit = QLineEdit()
        self.newGameButton = QPushButton("new Game")
        widgetList = [scoreLabel, scoreEdit, tryLabel, tryEdit, self.newGameButton]
        layout = QHBoxLayout()
        v1 = QVBoxLayout()
        for i in widgetList :
            v1.addWidget(i)
            if i == scoreEdit or i == tryEdit :
                v1.addStretch(1)
        v1.addStretch(22)

        self.g1 = GridLayout()

        layout.addLayout(self.g1)
        layout.addLayout(v1)
        self.setLayout(layout)


class startView(QWidget) :
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(300, 300)
        self.threeButton = Button("3 x 3")
        self.fourButton = Button("4 x 4")
        self.fiveButton = Button("5 x 5")
        self.sixButton = Button("6 x 6")
        buttonList = [self.threeButton, self.fourButton, self.fiveButton, self.sixButton]

        for i in buttonList :
            i.setStyleSheet('font-size: 20pt; font-family: Courier;')

        mainLayout = QVBoxLayout()
        for i in buttonList :
            mainLayout.addWidget(i)
        self.setLayout(mainLayout)



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    View = mainView()
    StartView = startView()
    StartView.hide()
    StartView.show()
    sys.exit(app.exec_())

