from flask import Flask, jsonify
from app import add, subtract, multiply, divide
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Калькулятор API',
        'endpoints': {
            '/': 'Главная страница',
            '/add/<a>/<b>': 'Сложение',
            '/subtract/<a>/<b>': 'Вычитание',
            '/multiply/<a>/<b>': 'Умножение',
            '/divide/<a>/<b>': 'Деление',
            '/health': 'Проверка статуса'
        }
    })

@app.route('/add/<float:a>/<float:b>')
def api_add(a, b):
    return jsonify({'result': add(a, b)})

@app.route('/subtract/<float:a>/<float:b>')
def api_subtract(a, b):
    return jsonify({'result': subtract(a, b)})

@app.route('/multiply/<float:a>/<float:b>')
def api_multiply(a, b):
    return jsonify({'result': multiply(a, b)})

@app.route('/divide/<float:a>/<float:b>')
def api_divide(a, b):
    try:
        return jsonify({'result': divide(a, b)})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health')
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
