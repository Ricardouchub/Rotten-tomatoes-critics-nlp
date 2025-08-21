# 🎬 ¿Qué tan positiva es tu reseña de cine? (EN/ES)

Demo en Hugging Face Spaces que carga un modelo de sentimiento multilingüe (XLM-R base) **desde el Hugging Face Hub**, sin subir los pesos al repo del Space.

## 🧠 Modelo
- Repo del modelo en HF Hub: `ricardo/xlmr-sentiment-es-en` (cámbialo en `app.py` o como variable `HF_REPO_ID`)
- Umbral por defecto: `THRESHOLD=0.48`
- Máx tokens: `MAX_LEN=224`

## 🚀 Cómo levantar este Space
1. Sube estos archivos (`app.py`, `requirements.txt`, `README.md`) a un nuevo **Hugging Face Space** (tipo `Gradio`).
2. (Opcional) En **Settings → Variables**:
   - `HF_REPO_ID = ricardo/xlmr-sentiment-es-en`
   - Si el repo es privado: añade **Secret** `HF_TOKEN` y el Space leerá tu token automáticamente.
3. Guarda y espera el build; el Space descargará el modelo al cache y quedará listo.

## 📝 Notas
- El Space usa `gradio` (más simple que orquestar FastAPI+Dash y CORS).
- Si quieres migrar tu UI en Dash, puedes crear un Space **Docker** y correr tu `uvicorn` + Dash (más complejo, no necesario para la demo).
- Para reducir tiempos de arranque, mantén el modelo en **safetensors** y evita deps pesadas.
