import numpy as np


def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    # data[:, 0] = área (x), data[:, 1] = preço (y)
    x = data[:, 0]
    y = data[:, 1]
    predictions = w * x + b
    errors = predictions - y
    mse = np.mean(errors ** 2)
    return mse


def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    x = data[:, 0]
    y = data[:, 1]
    n = len(x)
    
    # Derivadas parciais
    prediction = w * x + b
    error = prediction - y
    b_gradient = (2/n) * np.sum(error)
    w_gradient = (2/n) * np.sum(error * x)
    
    # Atualização
    b = b - alpha * b_gradient
    w = w - alpha * w_gradient
    
    return b, w


def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    b_history = []
    w_history = []
    
    for _ in range(num_iterations):
        b, w = step_gradient(b, w, data, alpha)
        b_history.append(b)
        w_history.append(w)
    
    return b_history, w_history
