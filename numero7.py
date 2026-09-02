def calcular_descuento_proporcional():
    try:
        monto = float(input("Ingresa el monto del descuento: "))
        base = float(input("Ingresa el monto base (total): "))
        
        porcentaje = (monto / base) * 100
        print(f"El descuento representa el {porcentaje:.2f}% del total.")
        
    except ValueError:
        print("Error: Por favor ingresa únicamente valores numéricos.")
    except ZeroDivisionError:
        print("Error: La base no puede ser 0, no es posible dividir entre cero.")

# Para probar la función:
calcular_descuento_proporcional()