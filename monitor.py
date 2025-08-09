# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import psutil
import time

# 創建 Flask 應用實例
app = Flask(__name__)
# 啟用 CORS，讓前端可以從不同網址向此伺服器發送請求
CORS(app)  

# ================================================================
# 路由設定
# ================================================================

# API 終點路由: 提供即時系統資料
@app.route('/data')
def get_system_data():
    """
    此 API 終點會使用 psutil 函式庫獲取系統的 CPU 和記憶體使用率，
    並以 JSON 格式返回。
    """
    try:
        # 獲取 CPU 使用率 (non-blocking)
        # 參數 interval=1 會在 1 秒內測量並返回 CPU 使用率
        cpu_usage = psutil.cpu_percent(interval=1)

        # 獲取虛擬記憶體 (RAM) 使用率
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent

        # 創建要返回的 JSON 資料
        system_data = {
            'cpu': cpu_usage,
            'memory': memory_usage
        }

        # 使用 jsonify 將 Python 字典轉換為 JSON 格式的 HTTP 回應
        return jsonify(system_data)

    except Exception as e:
        # 處理任何可能發生的錯誤，並返回錯誤訊息
        return jsonify({'error': str(e)}), 500

# 根目錄路由，僅用於確認伺服器已啟動
@app.route('/')
def hello_world():
    return '後端伺服器已啟動，請前往 /data 獲取資料。'


# ================================================================
# 啟動伺服器
# ================================================================

if __name__ == '__main__':
    # 在 3000 埠上啟動伺服器
    print("後端伺服器已啟動，請在瀏覽器中開啟 http://127.0.0.1:3000")
    app.run(debug=True, port=3000)