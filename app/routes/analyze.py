import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db, RequestHistory
from app.schemas import AnalyzeRequest, AnalyzeResponse
from app.ml_service import translate_text

router = APIRouter(prefix="/analyze", tags=["analyze"])
logger = logging.getLogger(__name__)

@router.post("", response_model=AnalyzeResponse)
def analyze_text(req: AnalyzeRequest, db: Session = Depends(get_db)):
    logger.info(f"📥 Запрос перевода: {req.text[:50]}...")
    if not req.text.strip():
        raise HTTPException(status_code=400, detail="Текст не может быть пустым")
    try:
        res = translate_text(req.text, req.direction)
        record = RequestHistory(
            input_text=req.text,
            result_text=res["translated_text"],
            model_name=res["model"]
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        logger.info("✅ Запрос сохранён в БД")
        return {"result": res["translated_text"], "score": 1.0, "model_name": res["model"]}
    except Exception as e:
        logger.error(f"❌ Ошибка обработки: {e}")
        raise HTTPException(status_code=500, detail="Internal server error during translation")