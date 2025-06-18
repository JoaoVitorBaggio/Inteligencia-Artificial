from typing import Tuple
from .minimax import minimax_move

EVAL_TEMPLATE = [
    [100, -30, 6, 2, 2, 6, -30, 100],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [6, 1, 1, 1, 1, 1, 1, 6],
    [2, 1, 1, 3, 3, 1, 1, 2],
    [2, 1, 1, 3, 3, 1, 1, 2],
    [6, 1, 1, 1, 1, 1, 1, 6],
    [-30, -50, 1, 1, 1, 1, -50, -30],
    [100, -30, 6, 2, 2, 6, -30, 100]
]

def make_move(state) -> Tuple[int, int]:
    return minimax_move(state, 4, evaluate_mask)

def evaluate_mask(state, player: str) -> float:
    board = state.get_board().tiles
    opponent = 'B' if player == 'W' else 'W'
    score = 0
    for y in range(8):
        for x in range(8):
            if board[y][x] == player:
                score += EVAL_TEMPLATE[y][x]
            elif board[y][x] == opponent:
                score -= EVAL_TEMPLATE[y][x]
    return score
