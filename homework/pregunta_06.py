"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    with open("files/input/data.csv", "r") as f:
        data = [line.strip().split("\t") for line in f]
    dicc = {}
    for row in data:
        pares = row[4].split(",")
        for par in pares:
            clave, valor = par.split(":")
            valor = int(valor)
            if clave not in dicc:
                dicc[clave] = [valor, valor]
            else:
                dicc[clave][0] = min(dicc[clave][0], valor)
                dicc[clave][1] = max(dicc[clave][1], valor)
    return sorted([(k, v[0], v[1]) for k, v in dicc.items()])
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """