def abrir_reporte():
    try:
        # Intentamos abrir el archivo en modo lectura
        archivo = open("reportes.txt", "r")
        contenido = archivo.read()
        print("Contenido del reporte:")
        print(contenido)
        archivo.close()
    except FileNotFoundError:
        print("Error: El archivo 'reportes.txt' no existe en la ruta actual.")
    finally:
        # Siempre se ejecuta al terminar el proceso
        print("Proceso de lectura de archivo finalizado.")

# Para probar la función:
abrir_reporte()