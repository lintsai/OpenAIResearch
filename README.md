
# 智能客服系統

本項目是一個基於 React 和 Flask 的全棧智能客服系統。前端使用 React 構建用戶界面，後端使用 Python 和 Flask 提供 API 服務，並且集成了 OpenAI 的 GPT 模型來生成智能回應。

## 項目概述

智能客服系統旨在模擬人類與用戶的對話，能夠回答問題、提供建議，並進行多回合對話。該系統可以應用於各類需要自動客服功能的應用中。

## 技術棧

- **前端：** React
- **後端：** Flask
- **NLP 引擎：** OpenAI GPT 模型
- **其他：** Flask-CORS, Python

## 功能特點

- 用戶可以通過界面輸入問題，系統將生成並返回智能回應。
- 支持多回合對話。
- 系統基於 GPT 模型進行自然語言處理，提供高質量的回應。

## 項目結構

```
AIResearch/
├── backend/
│   ├── app.py                # Flask 後端應用程式
│   └── requirements.txt      # 後端依賴項目
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js            # React 主組件
│   │   ├── App.css           # 自定義樣式
│   │   └── index.js          # React 入口文件
│   └── package.json          # 前端依賴項目
└── README.md                 # 項目說明文件
```

## 安裝與運行

### 前置條件

- Node.js 和 npm
- Python 3.x
- OpenAI API 密鑰

### 安裝步驟

1. 克隆本儲存庫：

   ```bash
   git clone https://github.com/lintsai/OpenAIResearch.git
   cd OpenAIResearch
   ```

2. 設置並運行前端：

   ```bash
   cd frontend
   npm install
   npm start
   ```

   此步驟會啟動 React 開發伺服器，通常會在 `http://localhost:3000` 上運行。

3. 設置並運行後端：

   ```bash
   cd ../backend
   python -m venv venv
   source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
   pip install -r requirements.txt
   python app.py
   ```

   此步驟會啟動 Flask 開發伺服器，通常會在 `http://localhost:5000` 上運行。

### 使用方法

- 在瀏覽器中打開 `http://localhost:3000`，你會看到一個簡單的聊天界面。
- 輸入你的問題，按下 `Send` 按鈕，系統將調用後端 API 並顯示回應。

## 未來改進

- 添加情感分析功能
- 優化多回合對話邏輯
- 添加數據庫以持久化用戶對話記錄

## 貢獻

如果你對此項目有任何建議或改進，歡迎提交 Pull Request 或開啟 Issue 進行討論。

## 版權

此項目使用 MIT 許可證 - 詳見 [LICENSE](LICENSE) 文件。
