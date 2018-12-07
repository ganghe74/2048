import push

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
        self.mainView.upButton.clicked.connect(self.push)
        self.mainView.downButton.clicked.connect(self.push)
        self.mainView.rightButton.clicked.connect(self.push)
        self.mainView.leftButton.clicked.connect(self.push)
        #self.mainView.keyPressed.connect(self.push) 키바인딩 추후작업

    def gameStart(self):
        sender = self.startView.sender()
        n = int(sender.text()[0])
        self.model.N = n
        self.startView.hide()
        self.mainView.g1.setN(n)
        self.mainView.show()

    def newGame(self):
        self.mainView.hide()
        self.startView.show()

    def push(self, e=0):
        direction = e
        if e == 0:
            sender = self.mainView.sender()
            direction = sender.text()
        print(direction)
        if direction == 'up':
            model.field = push.up(model.field)
        elif direction == 'down':
            model.field = push.down(model.field, model.N)
        elif direction == 'left':
            model.field = push.left(model.field)
        elif direction == 'right':
            model.field = push.right(model.field, model.N)

        if model.isMovable():
            model.generate(2)
            model.tries += 1
        else:
            print("Game Over!!!!!!!!")

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
    model.register(main)
    start.show()
    sys.exit(app.exec_())