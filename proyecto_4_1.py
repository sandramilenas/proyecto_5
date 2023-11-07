def convertir_mapa_a_matriz(mapa):
  filas = mapa.split("\n")
  columnas = len(filas[0])
  matriz = []
  for fila in filas:
    matriz.append(list(fila))

  for i in range(len(matriz)):
    for j in range(len(matriz[0])):
      if i == 0 or j == 0 or i == len(matriz) - 1 or j == len(matriz[0]) - 1:
        matriz[i][j] = "#"

  return matriz

def mostrar_matriz(matriz):
  os.system("cls")
  for fila in matriz:
    print("".join(fila))

def main_loop(mapa, posicion_inicial, posicion_final):
  px, py = posicion_inicial
  while (px, py) != posicion_final:
    mapa[px][py] = "P"
    tecla = input("Ingrese una tecla: ")

    if tecla == "w":
      px -= 1
    elif tecla == "a":
      py -= 1
    elif tecla == "s":
      px += 1
    elif tecla == "d":
      py += 1

    if 0 <= px < len(mapa) and 0 <= py < len(mapa[0]) and mapa[px][py] != "#":
      mapa[px][py] = "P"
      mapa[py][px] = "."
    else:
      continue

  mostrar_matriz(mapa)
  print("¡Has ganado!")

mapa = generar_laberinto(5, 5)
posicion_inicial = (0, 0)
posicion_final = (4, 4)

main_loop(mapa, posicion_inicial, posicion_final)