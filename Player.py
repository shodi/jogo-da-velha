from random import randint
from copy import deepcopy
from Minimax import minimax
from math import inf

class Player(object):
    def __init__(self, symbol, name, is_bot = False):
        self.symbol = symbol
        self.is_bot = is_bot
        self.name = name

    def __get_user_move(self) -> int:
        print('Escolha um valor', end = '\n> ')
        try:
            valor = int(input())
            if valor < 1 or valor > 9:
                raise ValueError
            return valor
        except ValueError:
            print('Valor inválido. Tente um valor N tal que 1 <= N <= 9')
            return self.__get_user_move()

    def __get_bot_move(self, table, players) -> int:
        best_move = -inf
        move = -1
        board = deepcopy(table.board)
        for i in range(3):
            for j in range(3):
                if type(board[i][j]) == int:
                    prev_value = board[i][j]
                    board[i][j] = self.symbol
                    move_val = minimax(board, players, 0, False)
                    board[i][j] = prev_value

                    if move_val > best_move:
                        best_move = move_val
                        move = board[i][j]
        return move

    def get_move(self, table, players) -> int:
        if not self.is_bot:
            return self.__get_user_move()
        else:
            return self.__get_bot_move(table, players)