from PyQt5.QtCore import Qt, pyqtSignal
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

    keyPressed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("2048")
        self.g1 = GridLayout()
        self.scoreLabel = QLabel("score")
        self.scoreLabel.setStyleSheet('font-size: 12pt;')
        self.scoreEdit = QLineEdit()
        self.scoreEdit.setReadOnly(True)
        self.tryLabel = QLabel("try")
        self.tryLabel.setStyleSheet('font-size: 12pt;')
        self.tryEdit = QLineEdit()
        self.tryEdit.setReadOnly(True)
        self.newGameButton = QPushButton("new Game")
        self.upButton = Button("up")
        self.downButton = Button("down")
        self.leftButton = Button("left")
        self.rightButton = Button("right")
        self.buttonVisible = QPushButton("Open Keys")
        self.buttonVisible.clicked.connect(self.keySetting)
        self.buttonList = [self.upButton, self.downButton, self.leftButton, self.rightButton]
        widgetList = [self.scoreLabel, self.scoreEdit, self.tryLabel, self.tryEdit, self.newGameButton]
        layout = QHBoxLayout()
        self.v1 = QVBoxLayout()
        for i in widgetList :
            self.v1.addWidget(i)
            if i == self.scoreEdit or i == self.tryEdit :
                self.v1.addStretch(1)
        self.v1.addStretch(1)

        self.g2 = QGridLayout()
        self.g2.addWidget(self.upButton, 0, 1)
        self.g2.addWidget(self.leftButton, 1, 0)
        self.g2.addWidget(self.rightButton, 1, 2)
        self.g2.addWidget(self.downButton, 2, 1)
        for i in self.buttonList :
            i.setVisible(False)


        self.v1.addStretch(10)
        self.v1.addLayout(self.g2)
        self.v1.addStretch(10)
        self.v1.addWidget(self.buttonVisible)


        layout.addLayout(self.g1)
        layout.addLayout(self.v1)
        self.setLayout(layout)

    def keySetting(self):
        sender = self.sender()
        if sender.text() == "Open Keys" :
            for i in self.buttonList :
                i.setVisible(True)
            self.buttonVisible.setText("Close Keys")
        elif sender.text() == "Close Keys" :
            for i in self.buttonList :
                i.setVisible(False)
            self.buttonVisible.setText("Open Keys")

    def keyPressEvent(self ,e):
        self.keyPressed.emit(e.key())

    def update(self, model):
        self.scoreEdit.setText(str(model.score))
        self.tryEdit.setText(str(model.tries))
        for row in range(6):
            for column in range(6):
                num = str(model.field[row][column])
                if num == '0':
                    num = ''
                self.g1.labels[row][column].setText(num)
        

class startView(QWidget) :
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("2048")
        self.resize(300, 300)
        self.title = QLabel("2048")
        self.title.setStyleSheet('font-size: 35pt;')
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.threeButton = Button("3 x 3")
        self.fourButton = Button("4 x 4")
        self.fiveButton = Button("5 x 5")
        self.sixButton = Button("6 x 6")
        buttonList = [self.threeButton, self.fourButton, self.fiveButton, self.sixButton]
        for i in buttonList :
            i.setStyleSheet('font-size: 20pt; font-family: Courier;')

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.title)
        mainLayout.addStretch(10)
        for i in buttonList :
            mainLayout.addWidget(i)
        self.setLayout(mainLayout)



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    View = mainView()
    StartView = startView()
    View.show()
    sys.exit(app.exec_())