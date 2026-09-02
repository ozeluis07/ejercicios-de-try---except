def calcular_comision():
    try:
        ventas = float(input("Ingresa el total de ventas: "))
        porcentaje = float(input("Ingresa el porcentaje de comisión (ej. 10 para 10%): "))
        
        comision = ventas * (porcentaje / 100)
        print(f"La comisión correspondiente es: ${comision:.2f}")
        
    # Se captura la excepción específica en lugar de 'except Exception:'
    except ValueError:
        print("Error: Los valores de ventas y porcentaje deben ser numéricos.")

# Para probar la función:
calcular_comision()