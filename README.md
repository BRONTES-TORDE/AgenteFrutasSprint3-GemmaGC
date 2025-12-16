# AgenteFrutasSprint3-GemmaGC
SPRINT 3
# Agente Clasificador de Frutas Impulsado por IA

Este proyecto documenta un segundo ejercicio para el Sprint 3, creando un agente inteligente sencillo que simula la clasificación de frutas.

## 1. Propósito del Agente Propuesto

El objetivo de este agente es actuar como un asistente que adivina qué fruta es basándose en las descripciones del usuario (color y forma). El propósito es entender cómo se pueden usar variables y decisiones lógicas simples para simular un proceso de clasificación inteligente.

## 2. Herramienta o Framework Utilizado

Para generar el código inicial se ha utilizado **[GitHub Copilot](copilot.github.com)**.

## 3. Resumen del Flujo Lógico de Interacción del Agente

El agente sigue estos pasos lógicos:

1.  **Saludo:** Saluda al usuario.
2.  **Pregunta por Color:** Pide al usuario que escriba un color (rojo, amarillo, verde...).
3.  **Pregunta por Forma:** Pide al usuario que escriba una forma (redonda, alargada...).
4.  **Procesamiento y Decisión:** El agente compara las respuestas con su base de datos interna.
5.  **Respuesta:** Si encuentra una coincidencia, adivina la fruta. Si no, dice que no la conoce.

## 4. Código Generado y Explicación Conceptual

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

## 5. Captura o Descripción del Resultado de la Interacción

¡Hola! Soy tu agente clasificador de frutas.
Piensa en una fruta común (manzana, banana, sandía) y yo intentaré adivinarla.
Introduce el color de tu fruta (rojo, amarillo, verde): ROJO
Introduce la forma de tu fruta (redonda, alargada): REDONDA
Intentando adivinar una fruta rojo y redonda...        
¡Creo que tu fruta es una manzana!
