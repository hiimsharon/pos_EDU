from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os

app = Flask(__name__)
app.secret_key = 'womens_fashion_pos_secret_key'

PRODUCTS_DB = [
    {"id": 1, "barcode": "W2026001", "name": "法式優雅V領針織衫", "category": "上衣/襯衫", "price": 1280, "cost": 450, "stock_physical": 15, "stock_online": 8, "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?auto=format&fit=crop&w=600&q=80"},
    {"id": 2, "barcode": "W2026002", "name": "率性西裝寬褲", "category": "下身/裙褲", "price": 1580, "cost": 550, "stock_physical": 10, "stock_online": 5, "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=600&q=80"}
]
ACCOUNTING_LOGS = []

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS_DB, current_category='所有商品')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form.get('username')
        session['role'] = request.form.get('role')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
