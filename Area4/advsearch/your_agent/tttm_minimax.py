from typing import Tuple
from ..tttm.gamestate import GameState
from .minimax import minimax_move

def make_move(state: GameState) -> Tuple[int, int]:
    return minimax_move(state, -1, utility)

def utility(state, player: str) -> float:
    if state.is_terminal():
        winner = state.winner()
        opponent = 'B' if player == 'W' else 'W'
        if winner == player:
            return 1
        elif winner == opponent:
            return -1
        else:
            return 0
    return 0
