# IA Trabalho 1
<ul>
  <li>André Mainardi Klarmann 343582 turma A</li>
  <li>João Gabriel Rau Wendt 343242 turma A</li>
  <li>João Vitor Baggio  turma A</li>
  <li>Gabriel Weingartner Welter 550135 turma A</li>
</ul>

## 1. Regressão Linear

<p>
Escolhemos como alpha=0.01, b=0.0, w=1.0 e num_iterations=500. EQM final: 9.289090691422183 
</p>

## 2. Aprendizado Supervisionado

<p>
A etapa dois foi realizada no google colab utilizando a GPU como ambiente de execução.

Avaliamos a dificuldade dos datasets a partir da acurácia dos resultados obtidos.

MNIST mais simples de executar de obter resultados com grande taxa de acurárcia devido a simplcidade do dataset, com imagens em preto e branco e relativamente parecidas. 
FASHION_MNIST mais complexo que o MNIST, a dificuldade principal foi encontrar alterações em relação à configuração base que melhorasse significantemente o desempenho.



MNIST:
Foram usadas cinco configurações para o treinamento e avaliação deste modelo, as alterações entre configurações foram feitas de maneira incremental, significando que as mudanças foram carregadas adiante a cada alteração de configuração. 
A primeira sendo a partir da função base; a segunda com uma camada convolucional a mais; a terceira com a adição de uma camada de pooling abaixo da cmada de convolução e uma função de batch entre as camadas; a quarta com um aumento para 128 neurônios relu; a quinta com a primeira camada convolucional com um filtro 5x5 e a adição de outra camada de 128 neurônios relu.
A configuração que melhor se saiu foi a última que trouxe todos as alterações das configurações anteriores junto a si. No entanto, o desempenho se mostrou poucos pontos percentuais acima das concorrentes, o aumento no tamanho do kernell e as camadas extras de neurônio contribuíram para o aumento da acuracia.

FASHION_MNIST:
Foram usadas cinco configurações para o treinamento e avaliação deste modelo, as alterações entre configurações foram feitas de maneira incremental, significando que as mudanças foram carregadas adiante a cada alteração de configuração. 
A primeira configuração sendo a partir da função base; a segunda com a adição de duas camadas de neurônios relu e aumento do número de neurônios para 100 em todas; a terceira foi usada uma função de batch entre as camadas de neurônios; a quarta com mais duas camadas de pooling e convolução com funções de batch entre elas e tamanho de kernell regressivos, sendo 7x7 na primeira e 5x5 nas duas últimas; A última removendo as camadas de convolução adicionadas e as funções de batch entre elas, mantendo o tamanho de 7x7 no kernell, além da diminuição da quantidade de neurônios para 32 nas duas camadas existentes. 
A configuração que melhor se saiu foi a primeira, baseada na função base que criamos. A maior diferença de desempenho entre a primeira, a terceira e a quinta configuração foi de 0.2 pontos percentuais. Nem camadas extras de convolução, pooling e neurônios nem a mudança no tamanho do kernell e quantidades de neurônios favoreceram o treinamento do modelo. 


<p>