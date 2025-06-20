from typing import Tuple
from .minimax import minimax_move

def make_move(state) -> Tuple[int, int]:
    return minimax_move(state, 4, evaluate_count)

def evaluate_count(state, player: str) -> float:
    board = state.get_board().tiles
    opponent = 'B' if player == 'W' else 'W'
    player_count = sum(row.count(player) for row in board)
    opponent_count = sum(row.count(opponent) for row in board)
    return player_count - opponent_count

