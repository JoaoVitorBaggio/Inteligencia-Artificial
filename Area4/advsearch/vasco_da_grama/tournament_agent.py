from typing import Tuple
from .othello_minimax_custom import make_move as tournament_move

def make_move(state) -> Tuple[int, int]:
    return tournament_move(state)
