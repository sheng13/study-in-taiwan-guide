'''
靜態截取（Static scraping）
工具/方式：通常用 requests 直接向網站伺服器發送 HTTP 請求，取得原始 HTML 原始碼，再用 BeautifulSoup 或其他解析器處理。

適用對象：網站內容是靜態的，HTML 一開始就包含完整資料（不需要執行 JavaScript）。

優點：

較快、資源消耗低。

不需啟動瀏覽器，執行效率較高。

實作較簡單。

缺點：

不能抓取透過 JavaScript 動態生成的內容。

無法處理需要登入、互動或頁面變化的情況。
'''
# 匯入所需模組
import requests  # 用來發送網頁請求
from bs4 import BeautifulSoup  # 用來解析 HTML 結構
from datetime import datetime  # 用來取得與格式化現在時間
import os  # 用來操作檔案與資料夾（如建立資料夾）

# 定義主要函式
def get_text_static():
    # 目標網頁（工作證公告的網頁）網址
    url = 'https://www.stu.edu.tw/latestnews_single.php?id=186106'

    # 設定 HTTP 請求標頭，模擬使用者是用瀏覽器存取（避免被網站阻擋）
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # 向該網址發送 GET 請求
    res = requests.get(url, headers=headers)

    # 檢查是否成功取得內容（狀態碼 200 表示成功）
    #狀態碼	含義
    #200	✅ 成功：伺服器成功處理了請求，並回傳資料。這是我們最想要的狀態。
    #301/302	🔁 網頁搬家了（重新導向）
    #403	⛔ 禁止訪問（可能需要登入或權限）
    #404	❌ 找不到網頁（URL 打錯或已被刪除）
    #500	💥 伺服器內部錯誤（程式錯了）
    if res.status_code != 200:
        print("❌ 無法取得頁面")
        return  # 若失敗，結束函式

    # 使用 BeautifulSoup 解析 HTML 文件
    soup = BeautifulSoup(res.text, 'html.parser')

    # 尋找指定的內容區塊（以 class 名稱為依據）
    content_div = soup.find("div", class_="latestnews_popup__content")

    # 如果沒找到該內容區塊，顯示錯誤並結束
    if not content_div:
        print("❌ 找不到內容區塊")
        return

    # 把 HTML 區塊轉成文字（含標籤）
    html_content = str(content_div)

    # 取得現在時間並轉為字串，用來顯示更新時間
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 建立完整 HTML 模板，嵌入擷取的內容與其他說明文字
    html_template = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>工作證內容擷取</title>
    <style>
        body {{
            font-family: 'Segoe UI', sans-serif;
            margin: 0;
            background-color: #e6f0ff;
        }}
        header {{
            background-color: #002855;
            padding: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .header-logo h1 {{
            margin: 0;
            font-size: 24px;
            color: #ffffff;
        }}
        .header-logo h2 {{
            margin: 5px 0 0 0;
            font-size: 16px;
            color: #a3cfff;
        }}
        main {{
            padding: 30px;
            max-width: 800px;
            margin: 0 auto;
        }}
        .section-box {{
            padding: 20px;
            border: 3px solid #004080;
            border-radius: 12px;
            background-color: #d9e6ff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }}
        .section-box h2 {{
            font-size: 20px;
            color: #0059b3;
            font-weight: bold;
            margin-bottom: 15px;
        }}
        .section-box .timestamp {{
            font-size: 14px;
            color: #777;
            margin-bottom: 10px;
        }}
        .section-box .content {{
            font-size: 16px;
            line-height: 1.6;
        }}
        footer {{
            text-align: center;
            padding: 20px;
            font-size: 14px;
            color: #ffffff;
            background-color: #002855;
        }}
        a {{
            color: #003399;
            text-decoration: underline;
        }}
        h3 {{
            background-color: #002855;
            color: white;
            padding: 6px 10px;
            border-radius: 6px;
        }}
        ul {{
            padding-left: 20px;
        }}
        .back-button {{
              padding: 15px 30px;
              font-size: 18px;
              background-color: white;
              color: #002855;
              border-radius: 10px;
              cursor: pointer;
              border: none;
              transition: background-color 0.2s;
              display: block;
              margin: 0 auto;
              max-width: 200px;
              text-align: center;
          }}
          .back-button:hover {{
              background-color: #e6f0ff;
          }}
    </style>

   <!-- Google 翻譯初始化 -->
  <script src="translate.js"></script>
  <!-- 載入 Google 翻譯插件 -->
  <script src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</head>
<body>
    <header>
        <div class="header-logo">
            <h1>留學台灣指南</h1>
            <h2>工作證申請</h2>
        </div>
        <div id="google_translate_element"></div>
    </header>

    <main>
        <div class="section-box">
            <div class="timestamp">本網頁更新時間：{timestamp}</div>
            <div class="content">{html_content}</div>
        </div>

        <div class="section-box">
            <h2>更多相關咨詢：</h2>

            <h3>聯絡資訊</h3>
            <p>勞動部勞動力發展署</p>
            <ul>
                <li>地址：北市中正區中華路一段39號10樓</li>
                <li>電話：(02) 8995-6000</li>
                <li>網址：<a href="http://www.wda.gov.tw" target="_blank">www.wda.gov.tw</a></li>
                <li>Email：<a href="mailto:wda@wda.gov.tw">wda@wda.gov.tw</a></li>
            </ul>

            <h3>💰 審查費繳交方式（100元）</h3>
            <ul>
                <li>郵局劃撥：賬號19058848，戶名：勞動部勞動力發展署聘僱許可收費專戶</li>
                <li>ATM繳費：送出申請後，系統會產生專屬16位賬號，並以ATM「繳費」功能繳交</li>
            </ul>
        </div>

        <div class="section-box">
            <h2>資料來源</h2>
            <div class="content"><a href="{url}" target="_blank">點我查看工作證原文連結</a></div>
        </div>
        <button class="back-button" id="back-home-button" onclick="window.location.href='main_page1.html'">
          返回首頁
        </button>
    </main>

    <footer>
        <span>畢業論文所有</span>
    </footer>
</body>
</html>"""

    # 建立資料夾 D:/專題1，如果資料夾已存在就略過
    os.makedirs("D:/專題_1", exist_ok=True)

    # 指定輸出 HTML 檔案的路徑
    output_path = "D:/專題_1/work_permit.html"

    # 寫入 HTML 檔案
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_template)

    # 顯示成功訊息
    print(f"✅ 已儲存為 {output_path}")

# 程式執行進入點（若此程式是被執行，而不是被引用）
if __name__ == '__main__':
    get_text_static()  # 呼叫主函式
