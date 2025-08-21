# app.py
import os, torch
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from fastapi.middleware.cors import CORSMiddleware

MODEL_DIR = "./hf_xlmr_best"      # <- tu modelo guardado
THRESHOLD = 0.48                  # <- umbral óptimo encontrado
DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"

tok = AutoTokenizer.from_pretrained(MODEL_DIR)
mdl = AutoModelForSequenceClassification.from_pretrained(MODEL_DIR).to(DEVICE).eval()

# 1) Inicializamos FastAPI
app = FastAPI(title="Sentiment (EN/ES) - XLM-R", version="1.0")

# 2) Agregamos CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8050", "http://127.0.0.1:8050"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------- Modelos de entrada ----------
class Item(BaseModel):
    text: str

class Batch(BaseModel):
    texts: List[str]

# ----------- Inferencia ----------
@torch.inference_mode()
def infer(texts: List[str], threshold: float = THRESHOLD):
    enc = tok(texts, truncation=True, max_length=224, padding=True, return_tensors="pt").to(DEVICE)
    logits = mdl(**enc).logits
    probs = torch.softmax(logits, dim=-1)[:, 1]  # prob clase positiva
    preds = (probs >= threshold).long()
    return [{"label": int(p.item()), "score": float(s.item())} for p, s in zip(preds, probs)]

# ----------- Endpoints ----------
@app.get("/health")
def health():
    return {
        "status": "ok",
        "device": DEVICE,
        "model": os.path.basename(MODEL_DIR),
        "threshold": THRESHOLD
    }

@app.post("/predict")
def predict(item: Item, threshold: float = THRESHOLD):
    return infer([item.text], threshold=threshold)[0]

@app.post("/predict_batch")
def predict_batch(batch: Batch, threshold: float = THRESHOLD):
    return infer(batch.texts, threshold=threshold)