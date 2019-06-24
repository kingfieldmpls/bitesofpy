class MultiplicationTable:
    def __init__(self, length):
        """Create a 2D self._table of (x, y) coordinates and
           their calculations (form of caching)"""

        self._table = []

        for i in range(1, length + 1):
            sub_matrix = []
            for j in range(1, length + 1):
                sub_matrix.append(j * i)
            self._table.append(sub_matrix)

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return len(self._table) * len(self._table[0])

    def __str__(self):
        """Returns a string representation of the table"""
        table = ""

        for row in self._table:
            row_str = " | ".join([str(num) for num in row])
            table += row_str + "\n"

        return table

    def calc_cell(self, x, y):
        """Takes x and y coords and returns the (pre-calculated) result"""
        return self._table[y - 1][x - 1]
