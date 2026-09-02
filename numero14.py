def mostrar_menu():
    print("--- MENU PRINCIPAL ---")
    print("1. Ver perfil")
    print("2. Configuración")
    print("3. Salir")
    
    try:
        opcion = int(input("Selecciona una opción (1-3): "))
    except ValueError:
        print("Error: Ingresa únicamente un número válido.")
    else:
        # Se ejecuta solo si NO hubo error de conversión
        if opcion == 1:
            print("Accediendo al perfil del usuario...")
        elif opcion == 2:
            print("Accediendo a la configuración del sistema...")
        elif opcion == 3:
            print("Cerrando sesión...")
        else:
            print("Opción fuera de rango. Selecciona entre 1 y 3.")

# Para probar la función:
mostrar_menu()