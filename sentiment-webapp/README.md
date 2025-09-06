# Sentiment Analysis Web App

Simple web app that performs sentiment analysis using Hugging Face transformers and FastAPI.

## Requirements
- Python 3.9+
- GPU optional (PyTorch)
- Internet access for first-time model download

## Install
```bash
python -m venv venv
source venv/bin/activate    # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
```

## Run
```bash
uvicorn app:app --reload --host 127.0.0.1 --port 8000
```
Open http://127.0.0.1:8000 in your browser.

## API
`POST /api/predict` — JSON `{"text":"..."}` -> returns `{"text":"...","label":"POSITIVE","score":0.987}`

## Notes
- First run will download the model (`distilbert-base-uncased-finetuned-sst-2-english`).
- For production: pin package versions, serve behind a proper ASGI server, restrict CORS, and consider using GPU or optimized runtime (ONNX/TF-TRT).
