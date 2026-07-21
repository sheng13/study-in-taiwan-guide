// 定義一個初始化 Google 翻譯元件的函式
function googleTranslateElementInit() {
  // 建立 Google 翻譯小工具的實體
  new google.translate.TranslateElement({
    // 指定原始網頁的語言為繁體中文
    pageLanguage: 'zh-TW',

    // 限定使用者可選擇的翻譯語言：繁體中文、簡體中文、英文、印尼語
    includedLanguages: 'zh-TW,zh-CN,en,id',

    // 設定翻譯小工具的版面為簡易模式（下拉式選單）
    layout: google.translate.TranslateElement.InlineLayout.SIMPLE
  }, 
  // 將翻譯工具插入到網頁中 ID 為 'google_translate_element' 的 HTML 元素內
  'google_translate_element');
}