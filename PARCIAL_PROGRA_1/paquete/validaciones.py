
def validar_numero(cadena:str) -> bool:
    i = 0
    es_numero = int(cadena) > 0

    while i < len(cadena) and es_numero:
        if ord(cadena[i]) < 48 or ord(cadena[i]) > 57:
            print("Debe ingresar un nùmero.")
            es_numero = False
        
        i += 1
    
    return es_numero

def pedir_cantidad(mensaje: str) -> int:
    numero = 0
    valido = False

    while valido == False:
        cadena = input(mensaje)

        if validar_numero(cadena) == False:
            print("Error. Debe ingresar un numero entero no negativo")

        else:
            numero = int(cadena)

            if numero >= 0:
                valido = True

    return numero


