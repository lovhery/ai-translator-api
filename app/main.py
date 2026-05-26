import logging
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routes import analyze, history
from app.db import init_db

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="AI Translator API")

# Подключаем шаблоны и статику
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.on_event("startup")
async def startup():
    logger.info("🚀 Запуск сервиса AI Translator API")
    init_db()

app.include_router(analyze.router)
app.include_router(history.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# 👈 НОВЫЙ РОУТ - главная страница
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})