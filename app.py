from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os

# 初始化 Flask 應用程式
app = Flask(__name__)

# TODO: 上線前記得換掉這組 secret_key，別用預設的
app.secret_key = 'womens_fashion_pos_secret_key'

# 模擬的商品資料庫（之後這塊要接真的資料庫或 ORM）
PRODUCTS_DB = [
    {
        "id": 1, 
        "barcode": "W2026001", 
        "name": "法式優雅V領針織衫", 
        "category": "上衣/襯衫", 
        "price": 1280, 
        "cost": 450, 
        "stock_physical": 15, 
        "stock_online": 8, 
        "img": "https://images.unsplash.com/photo-1434389677669-e08b4cac3105?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2, 
        "barcode": "W2026002", 
        "name": "率性西裝寬褲", 
        "category": "下身/裙褲", 
        "price": 1580, 
        "cost": 550, 
        "stock_physical": 10, 
        "stock_online": 5, 
        "img": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?auto=format&fit=crop&w=600&q=80"
    }
]

# 暫存會計與銷售紀錄用
ACCOUNTING_LOGS = []

# 首頁路由：載入商品清單與預設分類
@app.route('/')
def index():
    # 這裡先給所有商品，之後前端會用 JS 做篩選
    return render_template('index.html', products=PRODUCTS_DB, current_category='所有商品')

# 登入頁面：處理簡單的身份驗證 (Admin 測試用)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 簡單把使用者名稱跟權限塞進 session，先求有再求好
        session['user'] = request.form.get('username')
        session['role'] = request.form.get('role')
        return redirect(url_for('index'))
    return render_template('login.html')

# 登出：清空 session 狀態
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    # 開發環境下開啟 debug 比較方便看錯誤訊息
    app.run(host='0.0.0.0', port=5000, debug=True)
