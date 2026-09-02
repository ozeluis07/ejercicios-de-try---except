def obtener_precio():
    entrada = input("Ingresa el precio del producto: ")
    
    try:
        precio = float(entrada)
        print(f"El precio ingresado es: ${precio:.2f}")
    except ValueError:
        print("Error: La entrada no es un número válido (ejemplo válido: 150.50).")

# Para probar la función:
obtener_precio()