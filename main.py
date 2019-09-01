#!/usr/bin/python3
from Board import Board
from Player import Player
from CustomError import SelectionError
from random import randint

def main():
    board = Board()
    print('Digite seu nome', end = '\n> ')
    player_name = input()
    players = [Player('X', player_name), Player('O', 'bot', True)]
    turn = randint(0, 1)
    while True:
        current_player = players[turn]
        # Não devemos imprimir o board para a jogada do bot
        if turn == 0:
            board.print_out()
        while True:
            move = current_player.get_move(board, players)
            try:
                board.move(current_player.symbol, move)
                break
            except SelectionError:
                continue
        winner = board.get_winner()
        turn = 1 if turn == 0 else 0
        if not Board.has_move_left(board.board):
            print('Empate!')
            break
        if winner:
            for player in players:
                if player.symbol == winner:
                    print('Jogador \'%s\' venceu' % player.name)
            break


if __name__ == '__main__':
    main()