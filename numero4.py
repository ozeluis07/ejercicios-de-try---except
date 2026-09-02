def registrar_edad():
    entrada = input("Ingresa tu edad: ")
    
    try:
        edad = int(entrada)
        
        # Verificamos si la edad es lógica
        if 0 <= edad <= 120:
            print(f"Registro exitoso. Edad: {edad} años.")
        else:
            print("Error: La edad ingresada está fuera del rango válido (0 a 120).")
            
    except ValueError:
        print("Error: La edad debe ser un número entero sin letras ni decimales.")

# Para probar la función:
registrar_edad()