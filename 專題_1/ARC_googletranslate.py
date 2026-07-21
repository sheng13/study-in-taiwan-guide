from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from datetime import datetime
import time
import os

def get_text():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # 可打開無頭模式
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    url = 'https://www.immigration.gov.tw/5385/7244/7250/7317/%E5%B1%85%E7%95%99/362168/'
    driver.get(url)
    time.sleep(3)

    try:
        content = driver.find_element(By.CLASS_NAME, 'cp')
        html_content = content.get_attribute('innerHTML')  # 保留 HTML

        print("✅ 成功擷取內容")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 正確的 HTML 字串（含 Google 翻譯）
        html_template = f"""<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <title>移民署內容擷取</title>
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
    </style>

    <script type="text/javascript">
        function googleTranslateElementInit() {{
            new google.translate.TranslateElement({{
                pageLanguage: 'zh-TW',
                includedLanguages: 'zh-TW,zh-CN,en,id',
                layout: google.translate.TranslateElement.InlineLayout.SIMPLE
            }}, 'google_translate_element');
        }}
    </script>
    <script src="https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit"></script>
</head>
<body>
    <header>
        <div class="header-logo">
            <h1>留學台灣指南</h1>
            <h2>居留證申請</h2>
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
            <p>新竹縣移民署服務站（新竹縣居留證辦理地點）</p>
            <ul>
                <li>📍 國內事務大隊新竹縣服務站</li>
                <li>地址：新竹縣竹北市光明六路10號</li>
                <li>電話：03-555-2399</li>
                <li>辦公時間：週一至週五 08:00–17:00（中午不休息）</li>
                <li>地圖連結：<a href="https://goo.gl/maps/xx" target="_blank">Google 地圖</a></li>
            </ul>
        </div>

        <div class="section-box">
            <h2>資料來源</h2>
            <div class="content"><a href="{url}" target="_blank">點我查看移民署原文連結</a></div>
        </div>
    </main>

    <footer>
        <span>畢業論文所有</span>
    </footer>
</body>
</html>"""

        os.makedirs("D:/專題_1", exist_ok=True)
        output_path = "D:/專題_1/ARC1.html"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html_template)

        print(f"✅ 已儲存為 {output_path}")

    except Exception as e:
        print("❌ 擷取失敗：", e)

    driver.quit()

if __name__ == '__main__':
    get_text()
