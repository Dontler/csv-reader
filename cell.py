class Cell:

    width = 0
    cell_rows = 5

    def __init__(self, value=''):
        self.__value = value
        Cell.width = len(str(value))

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if Cell.width < len(value):
            Cell.width = len(value) + 4
        self.__value = value

    def __str__(self):
        return self.value
