import typer


def karatsuba(n1: int, n2: int) -> int:
  raise NotImplementedError("Implementar o algoritmo de Karatsuba")


def main(number1: int, number2: int):
  result = karatsuba(number1, number2)
  print(f"O resultado da multiplicação de {number1} e {number2} é {result}")


if __name__ == "__main__":
  typer.run(main)
