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

[TODO: INSERIR EXPLICAÇÃO DETALHADA DO ALGORITMO]

[TODO: INSERIR DIAGRAMA DRAW.IO]

### Explicação do código

No código, o algoritmo está implementado na função `def karatsuba(a: int, b: int)`,
Essa função recebe os dois números a serem multiplicados e retorna
o resultado da multiplicação utilizando o algoritmo de Karatsuba.

Como trata-se de um código pequeno, foi escolhido deixar todo o
conteúdo somente no arquivo `main.py`. Dessa forma, fica mais fácil
de entender e manter o código.



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
