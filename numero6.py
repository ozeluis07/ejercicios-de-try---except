def calcular_promedio_ventas():
    try:
        v1 = float(input("Ingresa la venta 1: "))
        v2 = float(input("Ingresa la venta 2: "))
        v3 = float(input("Ingresa la venta 3: "))
        
        lista_ventas = [v1, v2, v3]
        
        # Calculamos el promedio
        promedio = sum(lista_ventas) / len(lista_ventas)
        print(f"El promedio de ventas es: ${promedio:.2f}")
        
    except ValueError:
        print("Error: Todas las ventas deben ser números válidos.")
    except ZeroDivisionError:
        print("Error: La lista de ventas está vacía, no se puede dividir entre cero.")

# Para probar la función:
calcular_promedio_ventas()