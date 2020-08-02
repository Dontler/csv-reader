from grid.cell import Cell


class Row(object):

    def __init__(self, is_headers=False, cells=None):
        if cells is None:
            cells = []
        self.__cells = cells
        if len(cells) > 0:
            self.__first_cell = cells[0]
            self.__last_cell = cells[len(cells) - 1]
        else:
            self.__first_cell = None
            self.__last_cell = None
        self.__is_headers = is_headers

    def append_cell(self, cell: Cell):
        self.__cells.append(cell)
        if self.first_cell is None:
            self.__first_cell = cell
        self.__last_cell = cell

    def insert_cell(self, cell, index):
        if cell is not Cell:
            cell = Cell(cell)
        self.__cells.insert(index, cell)

    def insert_several_cells(self, cells, index):
        if index > len(self.__cells):
            raise IndexError('Индекс за границей строки. '
                             + f'Длина строки: {len(self.__cells)}, переданный индекс: {index}')
        for index, cell in enumerate(cells):
            if cell is not Cell:
                cells[index] = Cell(cell)
        self.__cells[index:1] = cells

    def remove_cell(self, index):
        self.__cells.pop(index)

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

    def __str__(self):
        row = ' '.join(self.__cells) + '\n'
        return row

    def __getitem__(self, key):
        return self.__cells[key]

    def __setitem__(self, key: int, value):
        self.__cells[key] = str(value)

