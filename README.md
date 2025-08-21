# FPAA-TI1

## Como rodar o projeto

Este projeto utiliza Python. Para rodar o projeto, você precisa ter o Python instalado na sua máquina.
Recomendo a utilização do [PyEnv](https://github.com/pyenv/pyenv) para instalar e gerenciar as versões
do Python.

### Configurar ambiente virtual

Para configurar um ambiente virtual, você pode usar o `venv`. Execute os seguintes criar e rodar um
novo `venv`:

```
# Criar novo venv
python -m venv venv

# Executar o venv
source venv/bin/activate  # No Linux ou macOS
venv\Scripts\activate  # No Windows
```

### Instalar Dependências

Para instalar as dependências do projeto, execute o seguinte comando na raiz do projeto:

```
pip install -r requirements.txt
```
