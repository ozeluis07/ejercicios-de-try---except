def convertir_moneda():
    try:
        monto = float(input("Ingresa el monto a convertir: "))
        tasa = float(input("Ingresa la tasa de cambio: "))
        
        resultado = monto * tasa
        print(f"Monto convertido: {resultado:.2f}")
        
    except ValueError:
        print("Error: Tanto el monto como la tasa de cambio deben ser datos numéricos.")

# Para probar la función:
convertir_moneda()