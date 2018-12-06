class Controller:
    def __init__(self, model, startView, mainView):
        self.model = model
        self.startView = startView
        self.mainView = mainView
        self.startView.threeButton.clicked.connect(self.gameStart)
        self.startView.fourButton.clicked.connect(self.gameStart)
        self.startView.fiveButton.clicked.connect(self.gameStart)
        self.startView.sixButton.clicked.connect(self.gameStart)
        self.mainView.newGameButton.clicked.connect(self.newGame)

    def left(self):
        pass

    def right(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def gameStart(self):
        sender = self.startView.sender()
        n = int(sender.text()[0])
        self.startView.hide()
        self.mainView.g1.setN(n)
        self.mainView.show()

    def newGame(self):
        self.mainView.hide()
        self.startView.show()

if __name__ == '__main__':
    import sys
    from view import mainView, startView
    from PyQt5.QtWidgets import QApplication
    from model import Model
    app = QApplication(sys.argv)
    model = Model()
    main = mainView()
    start = startView()
    controller = Controller(model, start, main)
    start.show()
    sys.exit(app.exec_())