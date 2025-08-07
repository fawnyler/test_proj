# test_proj

pip install flask
python app.py

# Примеры API-запросов для сервиса отзывов

## Добавление отзыва (POST /reviews)

### Linux/macOS, Windows (cmd)

```bash
curl -X POST http://localhost:5000/reviews \
  -H "Content-Type: application/json" \
  -d "{\"text\": \"Очень плохой сервис, разочарован\"}"
```

### Пример успешного ответа
```{
  "id": 1,
  "text": "Очень плохой сервис, разочарован",
  "sentiment": "negative",
  "created_at": "2025-08-07T15:44:20.123456"
}
```
