import os


def imprimir_numero(numero):
  """
  Imprime un número en la terminal.

  Args:
    numero: El número a imprimir.
  """

  os.system('cls' if os.name == 'nt' else 'clear')
  print(numero)


def main():
  """
  Programa principal.

  Inicia con un número en 0, lee la tecla `n` del teclado en un bucle, por cada presionada, borra la terminal e imprime el nuevo número hasta el número 50.
  """

  numero = 0
  while True:
    imprimir_numero(numero)
    tecla = input()
    if tecla == "n":
      numero += 1
    if numero == 51:
      break


if __name__ == "__main__":
  main()