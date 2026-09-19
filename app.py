from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os

app = Flask(__name__)
app.secret_key = 'pos_edu_sha_secret_key'

# 初始服飾商品資料庫
PRODUCTS_DB = [
    {"id": 1, "barcode": "W2026001", "name": "法式優雅V領針織衫", "category": "上衣/襯衫", "price": 1280, "cost": 450, "stock_physical": 15, "stock_online": 8, "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?auto=format&fit=crop&w=600&q=80"},
    {"id": 2, "barcode": "W2026002", "name": "率性西裝寬褲", "category": "下身/裙褲", "price": 1580, "cost": 550, "stock_physical": 10, "stock_online": 5, "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=600&q=80"},
    {"id": 3, "barcode": "W2026003", "name": "韓系高質感百褶長裙", "category": "下身/裙褲", "price": 1380, "cost": 480, "stock_physical": 12, "stock_online": 6, "img": "https://images.unsplash.com/photo-1583496661160-fb5886a0aaaa?auto=format&fit=crop&w=600&q=80"}
]

@app.route('/')
def index():
    return render_template('index.html', products=PRODUCTS_DB)

# 新增或編輯商品庫存
@app.route('/update_stock', methods=['POST'])
def update_stock():
    prod_id = int(request.form.get('id'))
    for p in PRODUCTS_DB:
        if p['id'] == prod_id:
            p['stock_physical'] = int(request.form.get('stock_physical', p['stock_physical']))
            p['stock_online'] = int(request.form.get('stock_online', p['stock_online']))
            p['price'] = int(request.form.get('price', p['price']))
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
