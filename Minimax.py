from math import inf
from Board import Board

def evaluate(board, symbol, opponent_symbol) -> int:
    for row in board:
        if row[0] == row[1] == row[2]:
            if row[0] == symbol:
                return 1
            elif row[0] == opponent_symbol:
                return -1

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == symbol:
                return 1
            elif board[0][i] == opponent_symbol:
                return -1

    if board[0][0] == board[1][1] == board[2][2] or\
        board[0][2] == board[1][1] == board[2][0]:
        if board[1][1] == symbol:
            return 1
        elif board[1][1] == opponent_symbol:
            return -1
    
    return 0

def minimax(board, players, depth, is_max, alpha, beta):
    opponent_symbol = None
    bot_symbol = None
    for player in players:
        if player.is_bot:
            bot_symbol = player.symbol
        else:
            opponent_symbol = player.symbol
    
    score = evaluate(board, bot_symbol, opponent_symbol)

    if score == 1 or score == -1:
        return score
    
    if not Board.has_move_left(board):
        return 0

    for i in range(3):
        for j in range(3):
            if type(board[i][j]) == int:
                prev_val = board[i][j]
                if is_max:
                    best = -inf
                    alpha = max(alpha, best)
                    board[i][j] = bot_symbol
                    fn = max
                else:
                    best = inf
                    beta = min(beta, best)
                    board[i][j] = opponent_symbol
                    fn = min
                best = fn(best, minimax(board, players, depth + 1, not is_max, alpha, beta))
                board[i][j] = prev_val
                if beta <= alpha:  
                    break
    return best
                
    
