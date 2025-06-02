from typing import Iterable, Set, Tuple
from heapq import heappop,heappush
from time import time 
from itertools import count

class Nodo:
    """
    Implemente a classe Nodo com os atributos descritos na funcao init
    """
    def __init__(self, estado:str, pai, acao:str, custo:int):
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
        


def sucessor(estado:str)->Set[Tuple[str,str]]:
    """
    Recebe um estado (string) e retorna um conjunto de tuplas (ação,estado atingido)
    para cada ação possível no estado recebido.
    Tanto a ação quanto o estado atingido são strings também.
    :param estado:
    :return:
    """
    
    acoes_possiveis = []
    idx = estado.index("_")
    linha, coluna = divmod(idx, 3)

    movimentos = {
        "acima": (-1, 0),
        "abaixo": (1, 0),
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
    
    filhos = []
    for acao, novo_estado in sorted(sucessor(nodo.estado)):
        filho = Nodo(estado=novo_estado, pai=nodo, acao=acao, custo=nodo.custo + 1)
        filhos.append(filho)
    return filhos
    
def astar_hamming(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Hamming e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    objetivo = "12345678_"
    inicio = time()
    contador = count()

    
    F = []
    nodo_inicial = Nodo(estado, None, None, 0)
    f_inicial = hamming_distance(estado, objetivo)
    heappush(F, (f_inicial, next(contador), nodo_inicial))

    
    X = set()             
    g = {estado: 0}       
    caminho_para = {estado: nodo_inicial}  

    nos_expandidos = 0

    while F:
        _, _, v = heappop(F)

        if v.estado == objetivo:
            fim = time()
            caminho = []
            while v.pai:
                caminho.insert(0, v.acao)
                v = v.pai
            print(f"Tempo decorrido: {fim - inicio:.4f} segundos")
            print(f"Nós expandidos: {nos_expandidos}")
            return caminho

        if v.estado not in X:
            X.add(v.estado)
            nos_expandidos += 1

            for filho in expande(v):
                g_novo = v.custo + 1
                if filho.estado not in g or g_novo < g[filho.estado]:
                    g[filho.estado] = g_novo
                    f = g_novo + hamming_distance(filho.estado, objetivo)
                    heappush(F, (f, next(contador), filho))
                    caminho_para[filho.estado] = filho

    return None

def hamming_distance(string1, string2): 
    distance = 0
    L = len(string1)
    for i in range(L):
        if string1[i] != string2[i] and string1[i] != "_":
            distance += 1
    return distance

def astar_manhattan(estado:str)->list[str]:
    """
    Recebe um estado (string), executa a busca A* com h(n) = soma das distâncias de Manhattan e
    retorna uma lista de ações que leva do
    estado recebido até o objetivo ("12345678_").
    Caso não haja solução a partir do estado recebido, retorna None
    :param estado: str
    :return:
    """
    objetivo = "12345678_"
    inicio = time()
    contador = count()

    F = []
    heappush(F, (manhattan_distance(estado, objetivo), next(contador), Nodo(estado, None, None, 0)))

    X = set() 
    g = {estado: 0} 

    nos_expandidos = 0

    while F:
        _, _, v = heappop(F)

        if v.estado == objetivo:
            fim = time()
            caminho = []
            while v.pai:
                caminho.insert(0, v.acao)
                v = v.pai
            print(f"Tempo decorrido: {fim - inicio:.4f} segundos")
            print(f"Nós expandidos: {nos_expandidos}")
            return caminho

        if v.estado not in X:
            X.add(v.estado)
            nos_expandidos += 1

            for filho in expande(v):
                g_novo = v.custo + 1
                if filho.estado not in g or g_novo < g[filho.estado]:
                    g[filho.estado] = g_novo
                    f = g_novo + manhattan_distance(filho.estado, objetivo)
                    heappush(F, (f, next(contador), filho))

    return None

def manhattan_distance(string1, string2, grid_size = 3): 
    distance = 0
    L = len(string1)
    for i in range(L):
        char = string1[i]
        if char != '_':
            matching_pos = string2.index(char)
            x1,y1 = divmod(i, grid_size)
            x2,y2 = divmod(matching_pos, grid_size)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

    


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
