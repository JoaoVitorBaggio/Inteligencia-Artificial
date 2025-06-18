import random
from typing import Tuple

def make_move(state) -> Tuple[int, int]:
    return monte_carlo_movimento(state, 100)

def contar_vencedor(state):
    try:
        board = state.get_board().tiles
        b = sum(row.count('B') for row in board)
        w = sum(row.count('W') for row in board)
        return 'B' if b > w else 'W' if w > b else 'empate'
    except:
        return state.winner() or 'empate'

def monte_carlo_movimento(state, iteracoes=100):
    jogador = state.player
    melhor = None
    melhor_taxa = -1
    for mov in state.legal_moves():
        vitorias = 0
        for _ in range(iteracoes):
            sim = state.copy().next_state(mov)
            while not sim.is_terminal():
                moves = list(sim.legal_moves())
                if moves:
                    sim = sim.next_state(random.choice(moves))
            if contar_vencedor(sim) == jogador:
                vitorias += 1
        taxa = vitorias / iteracoes
        if taxa > melhor_taxa:
            melhor_taxa = taxa
            melhor = mov
    return melhor or random.choice(list(state.legal_moves()))
