# AI Translator API
REST API для перевода текста EN ↔ RU с использованием Hugging Face и сохранением истории в PostgreSQL.

## Запуск
1. `cp .env.example .env` (проверь DATABASE_URL и HF_MODEL_NAME)
2. `docker compose up --build`
3. API and WEB-INTERFACE: `http://localhost:8000`
4. Swagger UI: `http://localhost:8000/docs`

## Endpoints
- `POST /analyze` - перевод текста
- `GET /history` - последние 20 запросов
- `GET /history/{id}` - запрос по ID
- `GET /health` - проверка статуса

## Тестирование
Импорт `postman/collection.json` в Postman.