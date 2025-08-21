# app_dash.py
import os
import requests
from urllib.parse import urljoin

from dash import Dash, html, dcc, Input, Output, State, no_update
import dash_bootstrap_components as dbc

# ================= Config =================
API_BASE = os.getenv("API_URL", "http://localhost:8000/")  # Cambia si despliegas
PREDICT_URL = urljoin(API_BASE, "predict")
HEALTH_URL = urljoin(API_BASE, "health")

# Umbral FIJO (no editable por usuario)
THRESHOLD_FIXED = float(os.getenv("THRESHOLD", "0.48"))

# ================= Helpers =================
def call_health():
    try:
        r = requests.get(HEALTH_URL, timeout=5)
        if r.ok:
            return r.json()
    except Exception:
        pass
    return {"status": "down", "device": "?", "model": "?"}

def call_predict(text, threshold: float = THRESHOLD_FIXED):
    payload = {"text": text}
    params = {"threshold": float(threshold)}
    r = requests.post(PREDICT_URL, json=payload, params=params, timeout=15)
    r.raise_for_status()
    return r.json()

def label_to_view(label: int):
    return ("Positiva", "success", "👍") if int(label) == 1 else ("Negativa", "danger", "👎")

def pct(score: float):
    return f"{score*100:.1f}%"

# ================= App =================
app = Dash(
    __name__,
    external_stylesheets=[dbc.themes.FLATLY],
    title="¿Qué tan positiva es tu reseña de cine?"
)
server = app.server  # por si despliegas con gunicorn

status = call_health()
badge_color = "success" if status.get("status") == "ok" else "danger"

# ---- Header ----
header = dbc.Navbar(
    dbc.Container([
        dbc.NavbarBrand("🎬 ¿Qué tan positiva es tu reseña de cine?", className="fw-bold"),
        dbc.Nav(className="ms-auto", children=[
            dbc.Badge(f"API: {status.get('status','down').upper()}", color=badge_color, className="me-2"),
            dbc.Badge(status.get("device","?"), color="secondary", className="me-2"),
            dbc.Badge(f"model: {status.get('model','?')}", color="secondary"),
        ]),
    ]),
    color="white",
    class_name="shadow-sm"
)

# ---- Single inference card (único bloque) ----
single_card = dbc.Card([
    dbc.CardHeader("Analiza una reseña (EN o ES)"),
    dbc.CardBody([
        html.P("Pega o escribe tu reseña. El modelo detectará si es positiva o negativa.", className="text-muted"),
        dcc.Textarea(
            id="input-text",
            placeholder="Ejemplos:\n- \"I absolutely loved this film!\"\n- \"La película fue excelente, actuaciones brillantes.\"\n- \"Demasiado lenta y predecible.\"",
            style={"width": "100%", "height": "150px", "resize": "vertical"},
        ),
        dbc.Row([
            dbc.Col(dbc.Button("Analizar Sentimiento", id="btn-run", color="primary", className="mt-3 w-100"), md=3),
            dbc.Col(html.Div([
                html.Small(f"Umbral utilizado (fijo): {THRESHOLD_FIXED:.2f}", className="text-muted")
            ], className="mt-3 ps-2")),  # Solo informativo
        ], className="g-2"),
        html.Hr(),
        dcc.Loading(
            id="loading",
            type="dot",
            children=html.Div(id="result-card")
        ),
    ])
], className="shadow-sm")

# ---- Footer ----
footer = dbc.Container([
    html.Hr(),
    html.Div([
        html.Small("Hecho por Ricardo Urdaneta · "),
        html.A("GitHub", href="https://github.com/Ricardouchub", target="_blank", className="me-2"),
        html.A("LinkedIn", href="https://www.linkedin.com/in/ricardourdanetacastro", target="_blank"),
    ], className="text-muted")
], className="mt-4 mb-4")

# ---- Layout ----
app.layout = dbc.Container([
    header,
    dbc.Row([
        dbc.Col(single_card, md=10, lg=8, class_name="mx-auto mt-4"),
    ]),
    footer
], fluid=True)

# ================= Callbacks =================
@app.callback(
    Output("result-card", "children"),
    Input("btn-run", "n_clicks"),
    State("input-text", "value"),
    prevent_initial_call=True,
)
def on_run(n, text):
    if not text or not str(text).strip():
        return dbc.Alert("Por favor ingresa una reseña.", color="warning", dismissable=True)

    try:
        res = call_predict(text.strip(), THRESHOLD_FIXED)
        label_str, color, emoji = label_to_view(res.get("label", 0))
        score = float(res.get("score", 0.0))
        score_pct = pct(score)

        # Tarjeta bonita con emoji + barra de confianza
        return dbc.Card([
            dbc.CardBody([
                html.H4([html.Span(emoji, className="me-2"), html.Span(label_str)], className=f"text-{color} fw-bold"),
                dbc.Progress(
                    value=score * 100, striped=True, animated=True,
                    color=color, className="mt-2",
                    label=f"Confianza: {score_pct}"
                ),
                html.Small("Interpretación: probabilidad de clase positiva producida por el modelo.", className="text-muted d-block mt-2")
            ])
        ], className="border-0")
    except Exception as e:
        return dbc.Alert(f"Error llamando a la API: {e}", color="danger", dismissable=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)