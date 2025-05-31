from typing import Iterable, Set, Tuple

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai:Nodo, acao:str, custo:int):
        """
        Inicializa o nodo com os atributos recebidos
        :param estado:str, representacao do estado do 8-puzzle
        :param pai:Nodo, referencia ao nodo pai, (None no caso do nó raiz)
        :param acao:str, acao a partir do pai que leva a este nodo (None no caso do nó raiz)
        :param custo:int, custo do caminho da raiz até este nó
        """
        # substitua a linha abaixo pelo seu codigo
        class Nodo:
            def __init__(self, estado: str, pai: 'Nodo', acao: str, custo: int):
                self.estado = estado
                self.pai = pai
                self.acao = acao
                self.custo = custo

            def __lt__(self, other):
                 return self.custo < other.custo
            
            def __eq__(self, other):
                return isinstance(other, Nodo) and self.estado == other.estado

            def __hash__(self):
                return hash(self.estado)
        raise NotImplementedError


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    acoes_possiveis = []
    idx = estado.index("_")
    linha, coluna = divmod(idx, 3)

    movimentos = {
        "cima": (-1, 0),
        "baixo": (1, 0),
        "esquerda": (0, -1),
        "direita": (0, 1)
    }

    for acao, (dl, dc) in movimentos.items():
        nova_linha, nova_coluna = linha + dl, coluna + dc
        if 0 <= nova_linha < 3 and 0 <= nova_coluna < 3:
            novo_idx = nova_linha * 3 + nova_coluna
            estado_lista = list(estado)
            estado_lista[idx], estado_lista[novo_idx] = estado_lista[novo_idx], estado_lista[idx]
            novo_estado = "".join(estado_lista)
            acoes_possiveis.append((acao, novo_estado))

    return set(acoes_possiveis)
    


def expande(nodo:Nodo)->Set[Nodo]:
    """
    Recebe um nodo (objeto da classe Nodo) e retorna um conjunto de nodos.
    Cada nodo do conjunto é contém um estado sucessor do nó recebido.
    :param nodo: objeto da classe Nodo
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    filhos = []
    for acao, novo_estado in sorted(sucessor(nodo.estado)):
        filho = Nodo(estado=novo_estado, pai=nodo, acao=acao, custo=nodo.custo + 1)
    filhos.append(filho)
    return filhos
    raise NotImplementedError


def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    

    raise NotImplementedError


def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    
    raise NotImplementedError


#opcional,extra
def bfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em LARGURA e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def dfs(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca em PROFUNDIDADE e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError

#opcional,extra
def astar_new_heuristic(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = sua nova heurística e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    # substituir a linha abaixo pelo seu codigo
    raise NotImplementedError
