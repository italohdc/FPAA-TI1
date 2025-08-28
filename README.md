# FPAA-TI1

> **Fundamentos de Programação e Algoritmos Avançados**
> 
> Trabalho Individual 1 - Implementação do Algoritmo de Karatsuba


## Descrição do projeto

Este projeto tem como objetivo implementar, e explicar, o
funcionamento do Algoritmo de Karatsuba. De forma resumida, esse
algoritmo é uma técnica eficiente para multiplicação de números
grandes.

### Como o algoritmo funciona

Dentre os conteúdos utilizados para compreender o algoritmo, foi
utilizada a explicação deste [artigo do Medium](https://medium.com/@sachinkg12/karatsuba-multiplication-algorithm-f60c4abe5779).
Este artigo foi escolhido por sua clareza e pela sua didática.

O algoritmo de Karatsuba é baseado na ideia de dividir os números
em partes menores, realizar multiplicações parciais e depois
combinar os resultados para obter o produto final. Trata-se de um
algoritmo recursivo, que reduz a complexidade da multiplicação.

Quando falamos de números grandes, o algoritmo pode reduzir o tempo
de execução em comparação com o método tradicional. Para números
pequenos, a diferença de desempenho pode não ser tão significativa.

### Explicação do código

No código, o algoritmo está implementado na função `def karatsuba(num1: int, num2: int)`,
Essa função recebe os dois números a serem multiplicados e retorna
o resultado da multiplicação utilizando o algoritmo de Karatsuba.

Como trata-se de um código pequeno, foi escolhido deixar todo o
conteúdo somente no arquivo `main.py`. Dessa forma, fica mais fácil
de entender e manter o código.

Abaixo, explico cada passo do código:

`Linha 10`: Caso base

Trata-se do caso base do algoritmo. Como trata-se de um algoritmo
recursivo, é necessário existir um caso base para finalizar a
recursão.

No caso, se um dos números tem 1 dígito, faz a multiplicação
utilizando o método comum.

`Linha 5`: Passo 1

Os números são convertidos para strings para facilitar a sua manipulação.
Como strings, fica mais fácil de pegar pedaços dos números e
contar a quantidade de dígitos.

`Linha 15`: Passo 2

As strings, que representam os números, são preenchidas com zeros
à esquerda, para que ambas tenham o mesmo tamanho. Isso facilita
a divisão dos números no Python.

`Linha 21`: Passo 3

Os números são divididos em duas partes, cada uma com metade dos dígitos.

`Linha 30`: Passo 4

Os produtos necessários são calculados recursivamente, utilizando as
partes dos números que foram obtidas no passo anterior.

Os produtos necessários vêm da fórmula combinada do algoritmo de Karatsuba.

`Linha 36`: Combinar os resultados utilizando a fórmula do Karatsuba

Os resultados dos produtos, da etapa anterior, são combinados
utilizando a fórmula do Karatsuba para obter o resultado final.



## Como executar o projeto

Este projeto utiliza Python. Para rodar o projeto, você precisa ter
o Python instalado na sua máquina. Foi utilizado, durante o
desenvolvimento, o Python 3.13. Recomendo a utilização do
[PyEnv](https://github.com/pyenv/pyenv) para instalar e gerenciar as
versões do Python.

### Configurar ambiente virtual

Para configurar um ambiente virtual, você pode usar o `venv`.
Execute os seguintes criar e rodar um novo `venv`:

```
# Criar novo venv
python -m venv venv

# Executar o venv
source venv/bin/activate  # No Linux ou macOS
venv\Scripts\activate  # No Windows
```

### Instalar Dependências

Para instalar as dependências do projeto, execute o seguinte
comando na raiz do projeto:

```
pip install -r requirements.txt
```

### Sobre as dependências

Para este projeto, foram utilizadas algumas dependências para
auxiliar no desenvolvimento. Dentre elas:

[`typer`](https://typer.tiangolo.com/): Biblioteca para a criação
de CLI (Interfaces de Linha de Comando). Utilizada para facilitar
a inserção dos números a serem multiplicados.


### Rodar o projeto

Para rodar o projeto, você pode utilizar o seguinte comando:

```
python main.py <NÚMERO_1> <NÚMERO_2>
```



## Relatório Técnico

### Análise de Complexidade Ciclomática

#### Fluxo de Controle da Função

O fluxo da função pode ser descrito da seguinte forma:

1. Conversão dos números em strings.
2. Verificação do **caso base** (`if len(x) == 1 or len(y) == 1`).  
   - Se verdadeiro → retorna a multiplicação direta.  
      - 2.1. Multiplicação direta (`return int(x) * int(y)`).
   - Se falso → continua.  
3. Preenchimento dos números com zeros.
4. Divisão dos números em duas partes (`a` e `b`, `c` e `d`).  
5. Cálculo dos produtos (chamadas recursivas): `z0`, `z2`, `z1`.  
6. Combinação dos resultados utilizando a fórmula do Karatsuba (`return`).

Abaixo, segue o diagrama do grafo de fluxo do algoritmo
implementado:

![Grafo de Fluxo](/assets/grafo_fluxo.png)

A partir da imagem acima, podemos identificar que existem:
- N = 7 nós (representando as etapas do algoritmo).
- E = 6 arestas (representando as transições entre as etapas).
- P = 1 componente conexo (trata-se de um único grafo).

Com isso, podemos calcular a complexidade ciclomática:

```
M = E - N + 2P
M = 6 - 7 + 2(1)
M = 1
```

### Análise de Complexidade Assintótica

Sobre os casos principais, podemos identificar:

- **Melhor caso:**  
  - Quando um dos números tem apenas 1 dígito
  - Complexidade O(1).  

- **Caso médio:**  
  - A recursão ocorre até os números serem reduzidos a 1 dígito → O(n^1.585).  

- **Pior caso:**  
  Igual ao caso médio, pois a recursão sempre se aplica para números com mais de 1 dígito → O(n^1.585).  
