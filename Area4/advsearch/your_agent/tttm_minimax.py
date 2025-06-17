import random
from typing import Tuple
from ..tttm.gamestate import GameState
from ..tttm.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Retorna uma jogada calculada pelo algoritmo minimax para o estado de jogo fornecido.
    :param state: estado para fazer a jogada
    :return: tupla (int, int) com as coordenadas x, y da jogada (lembre-se: 0 é a primeira linha/coluna)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada do Jogo da Tic-Tac-Toe Misere
    # Remova-o e coloque uma chamada para o minimax_move com 
    # a sua implementacao da poda alpha-beta. Use profundidade ilimitada na sua entrega,
    # uma vez que o jogo tem profundidade maxima 9. 
    # Preencha a funcao utility com o valor de um estado terminal e passe-a como funcao de avaliação para seu minimax_move

    _, move = minimax_move(state, utility, depth=5)
    return move

def utility(state, player:str) -> float:
    """
    Retorna a utilidade de um estado (terminal) 
    """
    if state.is_terminal():
        if state.winner() == state.player:
            return -1  # perde = bom
        elif state.winner() == state.opponent():
            return 1   # adversario vence = ruim
        else:
            return 0
    return 0
