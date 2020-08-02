class Cell(object):

    width = 0

    def __init__(self, value=''):
        self.__value = str(value)
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
