def obtener_cantidad():
    entrada = input("¿Cuántas unidades deseas comprar?: ")
    
    try:
        cantidad = int(entrada)
        print(f"Cantidad confirmada: {cantidad} unidades.")
    except ValueError:
        print("Error: Debes ingresar un número entero de productos.")

# Para probar la función:
obtener_cantidad()