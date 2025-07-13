import os
import google.generativeai as genai

# The client gets the API key from the environment variable `GOOGLE_API_KEY`.
# If you are using a different name (like GEMINI_API_KEY from your original comment),
# you need to configure it manually.
if 'GEMINI_API_KEY' in os.environ:
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
elif 'GOOGLE_API_KEY' not in os.environ:
    # Para una prueba rápida, descomenta la siguiente línea y pon tu clave.
    genai.configure(api_key="REEMPLAZA_ESTO_CON_TU_API_KEY")
    # exit() # Comentamos o borramos esta línea para que el script no se detenga.

# Create an instance of the model. Note: "gemini-2.5-flash" is not a valid model name yet.
# Using "gemini-1.5-flash" instead.
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

print("Conectado a Gemini. Introduce tu prompt para comenzar.")
print("Escribe 'salir' o presiona Ctrl+C para terminar.")

while True:
    try:
        prompt_text = input("\nTú: ")
        if prompt_text.lower() == 'salir':
            break

        response = model.generate_content(prompt_text)
        print("Gemini: " + response.text)

    except KeyboardInterrupt:
        print("\nSaliendo...")
        break