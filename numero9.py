def manejar_tipo_incompatible():
    texto = "100"
    numero = 50
    
    # 1. Ejemplo del error (Descomentar para ver cómo falla):
    # resultado = texto + numero  # Provoca TypeError porque no se puede sumar str e int
    
    # 2. Solución corrigiendo el tipo de dato:
    try:
        resultado = int(texto) + numero
        print(f"Resultado corregido convirtiendo el texto a entero: {resultado}")
    except TypeError:
        print("Error: Intentaste realizar una operación entre tipos de datos incompatibles.")

# Explicación:
# TypeError ocurre cuando aplicas un operador (+, -, *, /) a dos variables
# cuyos tipos de datos no son compatibles directamente (ej. 'str' con 'int').

# Para probar la función:
manejar_tipo_incompatible()