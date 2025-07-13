<h1 align=center> CHATBOT CON API DE GEMINI</h1>

### 🔹CREACION DEL ENTORNO VIRTUAL DE PYTHON

> [!IMPORTANT]
> Checkear:
```powershell
python --version
pip --version
```
---

1. Crea el directorio .venv

```powershell
python -m venv venv
```
---

2. Activa el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

### 🔹INSTALACION DE LIBRERIAS

```powershell
pip install google-generativeai
```

### 🔹CREACIÓN DEL ARCHIVO DE CONFIGURACIÓN, (PLANTILLA)

1. Incluimos en la raiz del proyecto

```
 -gemini-chatbot
    -gemi_api_plan.py
```

2. Conseguimos nuestra clave API

    https://aistudio.google.com/app/apikey

    Pasos para obtener tu clave:
    - Ve a la página de Google AI Studio usando el enlace de arriba.
    - Haz clic en el botón "Crear clave de API" (Create API key).
    - Es posible que te pida que inicies sesión con tu cuenta de Google y que crees un nuevo proyecto de Google Cloud si aún no tienes uno. Sigue los pasos que te indica.
    - Una vez creada, verás tu clave. ¡Cópiala y guárdala en un lugar seguro!



