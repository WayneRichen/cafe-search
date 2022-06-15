# 【外包作品】咖啡店查詢系統
# 【外包作品】加油補給站
連結：[waynerichen.github.io/cafe-serach/](https://waynerichen.github.io/cafe-serach/)

※ 本專案僅供學術用途，網站使用之素材為咖啡店所有。

## 技術
* 前端使用 HTML、Tailwind CSS、jQuery
* 後端使用 Python（開發環境使用 Python 3.10）Flask 框架

## 本地安裝
1. 下載以後先進入資料夾安裝 Python 套件，輸入 ``pip install -r requirements.txt`` 安裝本專案必備套件。
![image](https://user-images.githubusercontent.com/84951972/170245503-2850f9fc-644b-499b-9434-754fd8229b54.png)

3. 安裝好套件以後輸入 ``python app.py`` 啟動後端 Python 伺服器。
![image](https://user-images.githubusercontent.com/84951972/170245652-3739c27d-6e44-42cf-8111-c1c17a6dcc3e.png)


5. 編輯 ``index.html`` 把 ``BACKEND_URL`` 常數改成本地 Python 網址及埠號，例如 ``http://127.0.0.1:5000`` ，即可與本地 Python 後端對接。
![image](https://user-images.githubusercontent.com/84951972/170245853-887152ba-c4d0-4326-8991-3f8a49f5b4b9.png)


7. 後端啟動以及改好 ``BACKEND_URL`` 後直接點擊 ``index.html`` 用瀏覽器打開前端網頁即完成。
![image](https://user-images.githubusercontent.com/84951972/170245980-c5e6b691-cd7d-4d74-8468-33fa6e87af39.png)
