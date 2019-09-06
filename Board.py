from typing import Union
from CustomError import SelectionError

class Board(object):
    def __init__(self):
        # self.__matrix = [[x + 1 + 3 * y for x in range(3)] for y in range(3)]
        self.__matrix = [[1,2,'X'], [4,'X', 6], [7, 'O', 9]]

    @property
    def board(self):
        return self.__matrix

    @staticmethod
    def has_move_left(board):
        for i in range(3):
            for j in range(3):
                if type(board[i][j]) == int:
                    return True
        return False

    def get_winner(self) -> Union[int, None]:
        # Verifica linhas
        for i in self.__matrix:
            if i[0] == i[1] == i[2]:
                return i[0]
        # Verifica colunas
        for j in range(3):
            if self.__matrix[0][j] == self.__matrix[1][j] == self.__matrix[2][j]:
                return self.__matrix[0][j]
        # Verifica diagonais
        if self.__matrix[0][0] == self.__matrix[1][1] == self.__matrix[2][2] or \
            self.__matrix[0][2] == self.__matrix[1][1] == self.__matrix[2][0]:
            return self.__matrix[1][1]
        return None

    def move(self, symbol: str, field: int) -> None:
        for y in range(3):
            for x in range(3):
                if x + 1 + 3 * y == field:
                    try:
                        int(self.__matrix[y][x])
                        self.__matrix[y][x] = symbol
                    except Exception:
                        print('Campo %d já selecionado' % field)
                        raise SelectionError

    def print_out(self) -> None:
        for i in self.__matrix:
            print(*i, sep='\t|\t')
        print('\n')