from cell import Cell


class Row:

    def __init__(self, is_headers=False):
        self.__cells = list()
        self.__first_cell = None
        self.__last_cell = self.__last_cell
        self.__is_headers = is_headers

    def add_cell(self, cell: Cell):
        self.__cells.append(cell)
        if self.first_cell is None:
            self.__last_cell = cell
        self.__last_cell = cell

    @property
    def first_cell(self):
        return self.__first_cell

    @property
    def last_cell(self):
        return self.__last_cell

    @property
    def length(self):
        return len(self.__cells)

    @property
    def is_headers(self):
        return self.__is_headers

