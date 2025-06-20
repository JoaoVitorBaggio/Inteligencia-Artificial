from typing import Tuple, Callable

def minimax_move(state, max_depth: int, eval_func: Callable) -> Tuple[int, int]:
    player = state.player

    def minimax(state, depth, alpha, beta, maximizing):
        if state.is_terminal() or (depth == 0 and max_depth != -1):
            return eval_func(state, player), None

        best_move = None
        moves = list(state.legal_moves())

        if maximizing:
            value = float('-inf')
            for move in moves:
                child = state.next_state(move)
                eval_value, _ = minimax(child, depth - 1, alpha, beta, False)
                if eval_value > value:
                    value = eval_value
                    best_move = move
                alpha = max(alpha, value)
                if beta <= alpha:
                    break
            return value, best_move
        else:
            value = float('inf')
            for move in moves:
                child = state.next_state(move)
                eval_value, _ = minimax(child, depth - 1, alpha, beta, True)
                if eval_value < value:
                    value = eval_value
                    best_move = move
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value, best_move

    depth = max_depth if max_depth != -1 else 64
    _, move = minimax(state, depth, float('-inf'), float('inf'), True)
    return move