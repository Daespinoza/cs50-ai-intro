"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x = sum(row.count(X) for row in board)
    count_o = sum(row.count(O) for row in board)
    return X if count_x == count_o else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    
    # Validate movement
    if board[i][j] != EMPTY:
        raise Exception("Movimiento inválido")
    
    # Create copy
    new_board = [row[:] for row in board]
    
    # New movement
    new_board[i][j] = player(board)
    
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Verificar filas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
    
    # Verificar columnas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != EMPTY:
            return board[0][j]
    
    # Verificar diagonales
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell != EMPTY for row in board for cell in row)


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:  # MAX player
        best_value = -float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            # Llamada recursiva a MIN
            value = min_value(new_board)
            if value > best_value:
                best_value = value
                best_move = action
        return best_move
    else:  # MIN player (O)
        best_value = float('inf')
        best_move = None
        for action in actions(board):
            new_board = result(board, action)
            # Llamada recursiva a MAX
            value = max_value(new_board)
            if value < best_value:
                best_value = value
                best_move = action
        return best_move

'''
    Auxiliary Functions
'''
def max_value(board):
    if terminal(board):
        return utility(board)
    
    value = -float('inf')
    for action in actions(board):
        value = max(value, min_value(result(board, action)))
    return value

def min_value(board):
    if terminal(board):
        return utility(board)
    
    value = float('inf')
    for action in actions(board):
        value = min(value, max_value(result(board, action)))
    return value
