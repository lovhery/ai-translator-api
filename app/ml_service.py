import os
import logging
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

MODEL_NAME = os.getenv("HF_MODEL_NAME", "Helsinki-NLP/opus-mt-en-ru")
translator = None

def load_model():
    global translator
    if translator is None:
        logger.info(f"📥 Загрузка модели {MODEL_NAME}...")
        try:
            translator = pipeline("translation", model=MODEL_NAME)
            logger.info("✅ Модель загружена")
        except Exception as e:
            logger.error(f"❌ Ошибка загрузки модели: {e}")
            raise RuntimeError("Failed to load HF model")
    return translator

def translate_text(text: str, direction: str = "en-ru") -> dict:
    model = load_model()
    try:
        # Для opus-mt-en-ru перевод идёт автоматически в нужном направлении
        res = model(text)[0]
        return {"translated_text": res["translation_text"], "model": MODEL_NAME}
    except Exception as e:
        logger.error(f"❌ Ошибка перевода: {e}")
        raise RuntimeError("Translation failed")