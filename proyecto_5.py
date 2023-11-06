class Juego:

  def __init__(self, mapa, pos_inicial, pos_final):
    self.mapa = mapa
    self.pos_inicial = pos_inicial
    self.pos_final = pos_final

  def imprimir_mapa(self):
    for fila in self.mapa:
      print(fila)

  def mover_personaje(self, tecla):
    if tecla == "w":
      self.pos_inicial[0] -= 1
    elif tecla == "a":
      self.pos_inicial[1] -= 1
    elif tecla == "s":
      self.pos_inicial[0] += 1
    elif tecla == "d":
      self.pos_inicial[1] += 1

  def ha_ganado(self):
    return self.pos_inicial == self.pos_final

class JuegoArchivo(Juego):

  def __init__(self, path_a_mapas):
    super().__init__(None, None, None)

    self.path_a_mapas = path_a_mapas

  def __repr__(self):
    return f"JuegoArchivo(path_a_mapas={self.path_a_mapas})"

  def _leer_mapa(self, nombre_archivo):
    with open(nombre_archivo) as f:
      datos = f.readline().split()
      return datos[0], datos[1], datos[2:]

  def __init__(self):
    super().__init__(None, None, None)

    self.path_a_mapas = input("Ingrese la ruta a la carpeta con los mapas: ")

    nombres_archivos = os.listdir(self.path_a_mapas)
    self.nombre_archivo = random.choice(nombres_archivos)

    self.mapa, self.pos_inicial, self.pos_final = self._leer_mapa(
        f"{self.path_a_mapas}/{self.nombre_archivo}"
    )
mapa = ["1111", "1001", "1001", "1111"]
pos_inicial = (0, 0)
pos_final = (3, 3)

juego = Juego(mapa, pos_inicial, pos_final)

juego.imprimir_mapa()

while not juego.ha_ganado():
  tecla = input("Ingrese una tecla: ")
  juego.mover_personaje(tecla)
  juego.imprimir_mapa()

print("Has ganado!")