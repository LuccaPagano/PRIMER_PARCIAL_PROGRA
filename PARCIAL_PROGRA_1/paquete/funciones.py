from .validaciones import *

def bubble_sort(lista) -> list:
    """
    Ordena una lista de menor a mayor utilizando el ordenamiento de burbuja.
    Recibe una lista.
    Return respuesta.
    """

    if type(lista) != list:
        print("El elemento debe ser una lista.")
        respuesta = None
    else:
        n = len(lista)

        for i in range(n):
            limite_superior = n - i - 1

            for j in range(0, limite_superior):
                if lista[j] > lista[j + 1]:
                    menor = lista[j + 1]
                    lista[j + 1] = lista[j]
                    lista[j] = menor
        respuesta = lista
    
    return respuesta

def cargar_ventas() -> list:

    """
    Carga las ventas de todos los paises.
    No recibe ningun parametro.
    Retorna ventas.
    """

    paises = ["Argentina", "Brasil", "Colombia", "Italia", "Ecuador", "Noruega"]

    ventas = [0] * 6

    for i in range(len(ventas)):
        ventas[i] = pedir_cantidad(f"Ingrese las ventas de {paises[i]}: ")
        print()
    
    return ventas

def mostrar_resumen(paises: list, ventas:list) -> None:
    paises_compradores = 0
    total_productos = 0

    for i in range(len(paises)):
        total_productos += ventas[i]
        if ventas[i] > 0:
            paises_compradores += 1

    print(f"Cantidad de paises compradores: {paises_compradores}.")
    print(f"Cantidad total de productos vendidos: {total_productos}")

def mostrar_ventas(paises: list, ventas: list) -> None:
    """
    Muestra las ventas de todos los paises.
    Recibe por parametro paises y ventas (listas).
    Retorna mostrar_resumen.
    """

    for i in range(len(paises)):
        print(f"Ventas en {paises[i]}: {ventas[i]}")
        print()
    
    return mostrar_resumen(paises, ventas)


def mostrar_paises_porcentajes(paises: list, ventas:list, porcentaje: int) -> list:

    """
    Muestra los paises con menos porcentaje que se le indica con la variable porcentaje.
    Recibe paises, ventas (listas) y porcentaje.
    No retorna nada.
    """

    total_ventas = 0

    for i in range(len(ventas)):
        total_ventas += ventas[i]

    encontrado = 0
    porcentaje_acumulado = 0

    if total_ventas > 0:
        for i in range(len(paises)):
            porcentaje_pais = (ventas[i] / total_ventas) * 100
            if porcentaje_pais < porcentaje:
                if encontrado == 0:
                    print(f"Paìses con menos del {porcentaje}% de las ventas.")
                print(f"""{paises[i]}: {ventas[i]} productos comprados ({porcentaje_pais:.2f}% 
                    de las ventas totales.)""")
                porcentaje_acumulado += porcentaje_pais
                encontrado += 1
    
    if encontrado == 0:
        print(f"Error. No hay ningun pais con menos del {porcentaje}% de las ventas.")
    else:
        print(f"Porcentaje acumulado de los paises listados: {porcentaje_acumulado:.2f}%")

def mostrar_paises_ventas(paises: list, ventas:list, cantidad_ventas: int) -> None:

    total_ventas = 0
    for i in range(len(ventas)):
        total_ventas += ventas[i]

    cantidad_paises = 0
    suma_ventas = 0

    for i in range(len(paises)):
        if ventas[i] > cantidad_ventas:
            if cantidad_paises == 0:
                print(f"Paises con mas de {cantidad_ventas} ventas: ")
            porcentaje_pais = (ventas[i] / total_ventas) * 100
            print(f"{paises[i]}: {ventas[i]} productos comprados ({porcentaje_pais:.2f} de las ventas totales).")
            cantidad_ventas += ventas[i]
            cantidad_paises += 1

    if cantidad_paises == 0:
        print(f"Error. No hay ningun pais con mas de {cantidad_ventas} ventas.")
    else:
        promedio_ventas = suma_ventas / cantidad_paises
        print(f"Suma de ventas: {suma_ventas}")        
        print(f"Cantidad de paises: {cantidad_paises}")
        print(f"Promedio de ventas: {promedio_ventas:.2f}.")
    
    

def mostrar_paises_sobre_promedio(paises: list, ventas: list) -> None:
    total_ventas = 0
    for i in range(len(ventas)):
        total_ventas += ventas[i]

    promedio_general = total_ventas / len(ventas)
    cantidad_paises = 0
    porcentaje_acumuldo = 0

    for i in range(len(paises)):
        if ventas[i] > promedio_general:
            if cantidad_paises == 0:
                print(f"Paises por encima del promedio general: ")
            porcentaje_pais = (ventas[i] / total_ventas) * 100
            print(f"{paises[i]}: {ventas[i]} productos comprados ({porcentaje_pais:.2f} de las ventas totales).")
            porcentaje_acumuldo += porcentaje_pais
            cantidad_paises += 1

    if cantidad_paises == 0:
        print(f"Error. No hay ningun pais por encima del promedio general")
    else:
        
        print(f"Promedio general de ventas: {promedio_general:.2f}.")        
        print(f"Porcentaje acumulado de los paises listados: {porcentaje_acumuldo:.2f}.")

