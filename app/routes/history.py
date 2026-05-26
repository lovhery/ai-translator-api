import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db, RequestHistory

router = APIRouter(prefix="/history", tags=["history"])
logger = logging.getLogger(__name__)

@router.get("")
def get_history(db: Session = Depends(get_db)):
    records = db.query(RequestHistory).order_by(RequestHistory.created_at.desc()).limit(20).all()
    logger.info(f"📊 Получено {len(records)} записей из истории")
    return [
        {
            "id": r.id,
            "input_text": r.input_text,
            "result_text": r.result_text,
            "model_name": r.model_name,
            "created_at": r.created_at.isoformat()
        } for r in records
    ]

@router.get("/{item_id}")
def get_history_item(item_id: int, db: Session = Depends(get_db)):
    record = db.query(RequestHistory).filter(RequestHistory.id == item_id).first()
    if not record:
        logger.warning(f"⚠️ ID {item_id} не найден")
        raise HTTPException(status_code=404, detail="Request not found")
    return {
        "id": record.id,
        "input_text": record.input_text,
        "result_text": record.result_text,
        "model_name": record.model_name,
        "created_at": record.created_at.isoformat()
    }