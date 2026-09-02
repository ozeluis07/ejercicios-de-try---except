def registrar_datos():
    # El nombre es texto, no requiere conversión
    nombre = input("Ingresa tu nombre: ")
    
    # Manejo de edad
    try:
        edad = int(input("Ingresa tu edad: "))
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return

    # Manejo de salario
    try:
        salario = float(input("Ingresa tu salario: "))
    except ValueError:
        print("Error: El salario debe ser un número válido.")
        return

    print(f"\nDatos registrados correctamente:")
    print(f"Nombre: {nombre} | Edad: {edad} | Salario: ${salario:.2f}")

# Para probar la función:
registrar_datos()