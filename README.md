# test_proj

##pip install flask

##python app.py

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

## Получение всех отзывов (GET /reviews)

### Получить все отзывы

```bash
curl http://localhost:5000/reviews
```
### Получить только негативные отзывы

```bash
curl http://localhost:5000/reviews?sentiment=negative
```
### Получить только позитивные отзывы

```bash
curl http://localhost:5000/reviews?sentiment=positive
```

### Пример ответа
```[
  {
    "id": 2,
    "text": "Плохо работает, ужасно",
    "sentiment": "negative",
    "created_at": "2025-08-07T15:45:33.456789"
  },
  {
    "id": 4,
    "text": "Очень плохой сервис, разочарован",
    "sentiment": "negative",
    "created_at": "2025-08-07T15:47:10.654321"
  }
]

```
