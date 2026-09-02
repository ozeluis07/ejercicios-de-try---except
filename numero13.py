def consultar_empleado():
    empleados = {
        "E01": "Carlos Pérez - Desarrollador",
        "E02": "Ana Gómez - Diseñadora"
    }
    
    codigo = input("Ingresa el código del empleado (ej. E01): ").strip().upper()
    
    # Opción 1: Acceso directo capturando KeyError
    print("\n--- Método 1: Con try/except (KeyError) ---")
    try:
        info = empleados[codigo]
        print(f"Empleado encontrado: {info}")
    except KeyError:
        print(f"Error: El código '{codigo}' no existe en el registro.")
        
    # Opción 2: Alternativa con el método get()
    print("\n--- Método 2: Alternativa con get() ---")
    info_get = empleados.get(codigo, "Código de empleado no encontrado.")
    print(f"Resultado: {info_get}")

# Para probar la función:
consultar_empleado()