import random
import os

# -------------------------------
# Función para convertir una línea en diccionario
# -------------------------------
def extraer_pregunta(pregunta: str) -> dict:
    partes = pregunta.strip().split("|")

    return {
        "pregunta": partes[0],
        "correcta": partes[1],
        "opciones": partes[1:]
    }

# -------------------------------
# Leer archivo y crear lista
# -------------------------------
ruta = os.path.join(os.path.dirname(__file__), "preguntas.txt")

lista_preguntas = []

with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        lista_preguntas.append(extraer_pregunta(linea))

# -------------------------------
# Lógica del juego
# -------------------------------
puntuacion = 0
letras = ["a", "b", "c", "d"]

for pregunta in lista_preguntas:
    print("\n" + pregunta["pregunta"])

    opciones = pregunta["opciones"].copy()
    random.shuffle(opciones)

    mapa_respuestas = {}

    for i in range(len(opciones)):
        print(f"{letras[i]}) {opciones[i]}")
        mapa_respuestas[letras[i]] = opciones[i]

    respuesta_usuario = input("Elige una opción (a, b, c o d): ").lower()

    if mapa_respuestas.get(respuesta_usuario) == pregunta["correcta"]:
        print("✅ ¡Correcto!")
        puntuacion += 5
    else:
        print("❌ Incorrecto")
        print("La respuesta correcta era:", pregunta["correcta"])

print("\n🎯 Puntuación final:", puntuacion)