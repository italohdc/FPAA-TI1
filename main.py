import typer


def karatsuba(num1: int, num2: int) -> int:
  # Passo 1: Converter os números para strings para facilitar a manipulação
  x = str(num1)
  y = str(num2)


  # Caso base: se um dos números tem 1 dígito, multiplica diretamente
  if len(x) == 1 or len(y) == 1:
    return num1 * num2


  # Passo 2: Deixar ambas as variáveis com o mesmo tamanho, preenchendo com zeros à esquerda
  max_len = max(len(x), len(y))
  x = x.zfill(max_len)
  y = y.zfill(max_len)


  # Passo 3: Dividir os números em duas partes
  m = max_len // 2  # Divisão com resultado inteiro

  a = int(x[:-m]) if x[:-m] else 0
  b = int(x[-m:])
  c = int(y[:-m]) if y[:-m] else 0
  d = int(y[-m:])


  # Passo 4: Calcular recursivamente os os produtos necessários
  z0 = karatsuba(b, d)
  z2 = karatsuba(a, c)
  z1 = karatsuba(a + b, c + d)


  # Passo 5: Combinar os resultados utilizando a fórmula do Karatsuba
  return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0


def main(number1: int, number2: int):
  result = karatsuba(number1, number2)
  print(f"O resultado da multiplicação de {number1} e {number2} é {result}")


if __name__ == "__main__":
  typer.run(main)
