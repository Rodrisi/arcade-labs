import json
import random
import os

# -------------------------------
# Leer archivo JSON
# -------------------------------
ruta = os.path.join(os.path.dirname(__file__), "preguntas.json")

with open(ruta, "r", encoding="utf-8") as archivo:
    lista_preguntas = json.load(archivo)

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