from pydantic import BaseModel, Field
from typing import Optional

class AnalyzeRequest(BaseModel):
    text: str = Field(..., min_length=1, max_length=500, description="Текст для перевода")
    direction: Optional[str] = "en-ru"

class AnalyzeResponse(BaseModel):
    result: str
    score: float = 1.0
    model_name: str