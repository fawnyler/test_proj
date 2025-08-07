import sqlite3
import json
from flask import Flask, request, jsonify, Response
from datetime import datetime

app = Flask(__name__)
DB_PATH = 'reviews.db'

# --- Словарь для определения сентимента ---
POSITIVE_WORDS = ['хорош', 'люблю', 'отличн', 'нрав', 'супер', 'класс', 'прекрасн', 'замечательн']
NEGATIVE_WORDS = ['плохо', 'ненавиж', 'ужас', 'отстой', 'дурацк', 'ненрав', 'разочарован', 'кошмар']

def detect_sentiment(text):
    text_lower = text.lower()
    if any(word in text_lower for word in POSITIVE_WORDS):
        return 'positive'
    if any(word in text_lower for word in NEGATIVE_WORDS):
        return 'negative'
    return 'neutral'

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# --- Создание таблицы ---
def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                sentiment TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        ''')
    print('DB initialized!')

init_db()

# --- POST /reviews ---
@app.route('/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'Text is required'}), 400

    sentiment = detect_sentiment(text)
    created_at = datetime.utcnow().isoformat()

    with get_db() as conn:
        cur = conn.execute(
            'INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)',
            (text, sentiment, created_at)
        )
        review_id = cur.lastrowid

    return jsonify({
        'id': review_id,
        'text': text,
        'sentiment': sentiment,
        'created_at': created_at,
    }), 201

# --- GET /reviews?sentiment=negative ---
@app.route('/reviews', methods=['GET'])
def get_reviews():
    sentiment = request.args.get('sentiment')
    query = 'SELECT * FROM reviews'
    params = []
    if sentiment:
        query += ' WHERE sentiment = ?'
        params.append(sentiment)
    with get_db() as conn:
        cur = conn.execute(query, params)
        rows = [dict(row) for row in cur.fetchall()]
    return Response(
        json.dumps(rows, ensure_ascii=False, indent=2),
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(debug=True)
