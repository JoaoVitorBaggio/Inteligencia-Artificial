from typing import Tuple
from .minimax import minimax_move

MASK = [
    [100, -20, 10, 5, 5, 10, -20, 100],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [5, -2, -1, -1, -1, -1, -2, 5],
    [5, -2, -1, -1, -1, -1, -2, 5],
    [10, -2, -1, -1, -1, -1, -2, 10],
    [-20, -50, -2, -2, -2, -2, -50, -20],
    [100, -20, 10, 5, 5, 10, -20, 100]
]

def make_move(state) -> Tuple[int, int]:
    return minimax_move(state, 4, evaluate_custom)

def evaluate_custom(state, player: str) -> float:
    board = state.get_board().tiles
    opponent = 'B' if player == 'W' else 'W'
    score = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == player:
                score += MASK[y][x]
            elif board[y][x] == opponent:
                score -= MASK[y][x]
    return score
