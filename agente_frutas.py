# Un agente simple que clasifica frutas basado en color y forma.

def clasificar_fruta(color, forma):
    """Simula un clasificador de frutas."""
    # Base de datos de frutas simulada
    if color == "rojo" and forma == "redonda":
        return "manzana"
    elif color == "amarillo" and forma == "alargada":
        return "banana"
    elif color == "verde" and forma == "redonda":
        return "sandía"
    else:
        return "desconocida"

# --- Flujo principal del agente ---

print("¡Hola! Soy tu agente clasificador de frutas.")
print("Piensa en una fruta común (manzana, banana, sandía) y yo intentaré adivinarla.")

# Pedir color y forma al usuario
color_usuario = input("Introduce el color de tu fruta (rojo, amarillo, verde): ").lower()
forma_usuario = input("Introduce la forma de tu fruta (redonda, alargada): ").lower()

print(f"Intentando adivinar una fruta {color_usuario} y {forma_usuario}...")

# Llamar a la funcion y mostrar el resultado
fruta_adivinada = clasificar_fruta(color_usuario, forma_usuario)

if fruta_adivinada != "desconocida":
    print(f"¡Creo que tu fruta es una {fruta_adivinada}!")
else:
    print("Vaya, no tengo esa fruta en mi base de datos.")