"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    with open("files/input/data.csv", "r") as f:
        data = [line.strip().split("\t") for line in f]
    suma = sum(int(row[1]) for row in data)
    
    return suma

    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
