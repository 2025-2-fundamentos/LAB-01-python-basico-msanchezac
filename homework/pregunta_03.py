"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    with open("files/input/data.csv", "r") as f:
        data = [line.strip().split("\t") for line in f]
    suma_por_letra = {}
    for row in data:
        letra = row[0]
        valor = int(row[1])
        suma_por_letra[letra] = suma_por_letra.get(letra, 0) + valor
    return sorted(suma_por_letra.items())
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """