# IA Trabalho 4
<ul>
  <li>André Mainardi Klarmann 343582 turma A</li>
  <li>João Gabriel Rau Wendt 343242 turma A</li>
  <li>João Vitor Baggio 326585 turma A</li>
  <li>Gabriel Weingartner Welter 550135 turma A</li>
</ul>

# Meta-Heurístca Customizada

A meta-heurística customizada utiliza o algoritmo minimax com profundidade fixa, em combinação
com uma matriz MASK com valores posicionais fixos. A matriz MASK define um valor estratégico para
cada posição do tabuleiro, os cantos possuem valor 100 por serem posições valiosas uma vez que uma
peça em um canto não pode ser revertida, os valores adjacentes aos cantos possuem valores negativos
pois o posicionamento de uma peça nessas posições abre a possibilidade de o oponente capturar o
canto, casas centrais possuem valores com módulo pequeno, podendo ser positivas ou negativas.
A matriz é utilizada na função evaluate_custom, somando os valores das peças do Player e subtraindo
os valores das peças do oponente.

# Critério de Parada do Agente

O critério de parada utilizado é a profundidade máxima que é fixa com valor 4