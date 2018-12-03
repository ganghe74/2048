from observer.observable import Observable

class Model(Observable):
    def __init__(self):
        super().__init__()
        self.__N = 4
        self.__field = [[j for j in range(6)] for i in range(6)]

    @property
    def field(self):
        return self.__field

    def setField(self, row, column, num):
        self.__field[row][column] = num
        self.notify()
        print("notify")

model = Model()
print(model.field)

model.setField(0,0,3)
print(model.field)