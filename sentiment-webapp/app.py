from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import analyze_text

app = FastAPI(title="Sentiment Analysis Web App")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class PredictRequest(BaseModel):
    text: str

@app.get("/", response_class=HTMLResponse)
async def get_ui(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/predict")
async def predict(payload: PredictRequest):
    text = payload.text.strip()
    if not text:
        return JSONResponse(status_code=400, content={"error": "Empty text provided"})
    try:
        out = analyze_text(text)
        return {"text": text, "label": out["label"], "score": out["score"]}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": "Model inference error", "detail": str(e)})

@app.post("/predict-form", response_class=HTMLResponse)
async def predict_form(request: Request, text: str = Form(...)):
    try:
        out = analyze_text(text)
        return templates.TemplateResponse("index.html", {"request": request, "result": out, "input_text": text})
    except Exception as e:
        return templates.TemplateResponse("index.html", {"request": request, "error": str(e), "input_text": text})
