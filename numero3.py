def validar_calificacion():
    entrada = input("Ingresa la calificación (0 a 100): ")
    
    try:
        calificacion = float(entrada)
        
        # Validación de rango (separada del error de conversión)
        if 0 <= calificacion <= 100:
            print(f"Calificación válida: {calificacion}")
        else:
            print("Error: La calificación debe estar entre 0 y 100.")
            
    except ValueError:
        print("Error: Debes ingresar un valor numérico.")

# Para probar la función:
validar_calificacion()