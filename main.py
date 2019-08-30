#!/usr/bin/python3
from Board import Board
from Player import Player
from CustomError import SelectionError

def main():
    board = Board()
    value = 1
    while True:
        board.print_out()
        try:
            board.move('x', value)
        except SelectionError:
            continue
        value = value + 1
        winner = board.get_winner()
        if winner:
            print('Jogador %s venceu' % winner)
            break


if __name__ == '__main__':
    main()