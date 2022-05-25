# 咖啡店查詢系統

## 技術
* 前端使用 HTML、Tailwind CSS、jQuery
* 後端使用 Python（開發環境使用 Python 3.10）Flask 框架

## 本地安裝
1. git clone 下來以後先進入資料夾安裝 Python 套件，輸入 ``pip install -r requirements.txt`` 安裝本專案必備套件。
1. 安裝好套件以後輸入 ``python app.py`` 啟動後端 Python 伺服器。
1. 編輯 ``index.html`` 把 ``BACKEND_URL`` 常數改成本地 Python 網址及埠號，例如 http://127.0.0.1:5000，即可與本地 Python 後端對接。
1. 後端啟動以及改好 ``BACKEND_URL`` 後直接點擊 ``index.html`` 用瀏覽器打開前端網頁即完成。