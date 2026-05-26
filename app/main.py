import logging
from fastapi import FastAPI
from app.routes import analyze, history
from app.db import init_db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Translator API")

@app.on_event("startup")
async def startup():
    logger.info("🚀 Запуск сервиса AI Translator API")
    init_db()

app.include_router(analyze.router)
app.include_router(history.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}