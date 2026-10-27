from paquete import *

def mostrar_menu() -> None:
    print("""
    Ingrese 1 opcion:
    1. Cargar ventas.
    2. Mostrar ventas.
    3. Países con menos del 10 % de ventas.
    4. Países con menos del 15 % de ventas.
    5. Países con menos del 20 % de ventas.
    6. Países con más de 500 compras.
    7. Países con más de 1000 compras.
    8. Países por encima del promedio.
    9. Países menos compradores.
    10. “Hardcodear” vector.
    11. Ordenar países por nombre.
    
    """)

paises_base = ["Argentina", "Brasil", "Colombia", "Italia", "Ecuador", "Noruega"]
paises_harcodeados = ["Uruguay", "Chile", "Paraguay", "Costa de Marfil", "Bolivia"]
compras_paises =  [450, 720, 310, 1650, 890, 620, 1250, 230]
paises = paises_base
ventas = []
opcion = ""

while opcion != "12":
    mostrar_menu()
    opcion = input("Ingrese una opcion: ")

    match opcion:

        case "1":
            paises = paises_base
            ventas = cargar_ventas()
        
        case "2":
            mostrar_ventas(paises, ventas)
        
        case "3":
            mostrar_paises_porcentajes(paises, ventas, 10)
            
        case "4":
            mostrar_paises_porcentajes(paises, ventas, 15)

        case "5":
            mostrar_paises_porcentajes(paises, ventas, 20)

        case "6":
            mostrar_paises_ventas(paises, ventas, 500)

        case "7":
            mostrar_paises_ventas(paises, ventas, 1000)            
        
        case "8":
            mostrar_paises_sobre_promedio(paises, ventas)
        
        case "9":
            pass

        case "10":
            paises = paises_harcodeados
            ventas = compras_paises
            print("Los datos fueron reemplazados por los paises hardcodeados.")
        

        case "11":
            bubble_sort(paises)
            print(paises)        
        
        case "12":
            break

        case _:
            print("Error. Ingrese una opcion valida.")