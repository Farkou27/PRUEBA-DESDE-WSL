import ollama

# Pregunta al modelo
respuesta = ollama.generate(
    model="llama3.2:3b",
    prompt="Explícame qué es la inteligencia artificial en 2 líneas"
)

print(respuesta["response"])