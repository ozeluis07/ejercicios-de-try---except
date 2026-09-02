def consultar_inventario():
    productos = ["Laptop", "Teclado", "Mouse", "Monitor"]
    print(f"Lista de productos disponibles (índices del 0 al {len(productos)-1}):")
    
    try:
        posicion = int(input("Ingresa la posición del producto: "))
        producto = productos[posicion]
        print(f"El producto en la posición {posicion} es: {producto}")
        
    except ValueError:
        print("Error de formato: Debes ingresar un número entero válido.")
    except IndexError:
        print("Error de rango: La posición ingresada no existe en el inventario.")

# Para probar la función:
consultar_inventario()