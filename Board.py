from CustomError import SelectionError

class Board(object):
    def __init__(self):
        self.__matrix = [[x + 1 + 3 * y for x in range(3)] for y in range(3)]

    def get_winner(self):
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

    def move(self, symbol: str, field: int):
        for j in range(3):
            for i in range(3):
                if i + 1 + 3 * j == field:
                    try:
                        int(self.__matrix[i][j])
                        self.__matrix[i][j] = symbol
                    except Exception:
                        print('Campo %d já selecionado' % field)
                        raise SelectionError

    def print_out(self):
        for i in self.__matrix:
            print(*i, sep='\t|\t')
        print('\n')