def es_bisiesto(anio):
  """
  Determina si un año es bisiesto.

  Args:
    anio: El año a evaluar.

  Returns:
    True si el año es bisiesto, False en caso contrario.
  """

  if anio % 4 != 0:
    return False

  if anio % 100 == 0:
    return False

  return True


def es_fecha_valida(fecha):
  """
  Determina si una fecha es válida.

  Args:
    fecha: La fecha a evaluar.

  Returns:
    True si la fecha es válida, False en caso contrario.
  """

  try:
    d, m, a = map(int, fecha.split())
  except ValueError:
    return False

  if m < 1 or m > 12:
    return False

  if d < 1 or d > 31:
    return False

  dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if m in [1, 3, 5, 7, 8, 10, 12]:
    if d > dias_mes[m - 1]:
      return False

  if m == 2:
    if es_bisiesto(a):
      if d > 29:
        return False
    else:
      if d > 28:
        return False

  return True


def main():
  """
  Programa principal.

  Lee una fecha del usuario y determina si es válida.
  """

  fecha = input("Ingrese una fecha: ")

  if es_fecha_valida(fecha):
    print("Fecha correcta")
  else:
    print("Fecha incorrecta")


if __name__ == "__main__":
  main()