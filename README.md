# 薪資計算機 & 錢錢管家

個人財務管理工具組，包含**薪資計算**與**日常記帳**兩大功能，專為打工族、家教等兼職工作者設計。

**不需要安裝任何東西**，用手機或電腦的瀏覽器打開就能用。

> **給一般使用者：** 看到下方的「技術細節」之前的內容就夠用了，技術細節可以完全跳過。
> **給技術人員 / 面試官：** 本專案的架構設計、資料模型、同步機制等完整技術文件請見 [技術細節](#技術細節)。

---

## 如何下載

1. 點擊本頁面上方綠色的 **「Code」** 按鈕
2. 選擇 **「Download ZIP」**
3. 下載後解壓縮，會得到一個資料夾

---

## 如何使用

### 電腦版

1. 打開解壓縮後的資料夾
2. 找到 **`薪資計算機v2.html`** 或 **`錢錢管家v3.html`**
3. 對檔案**點兩下**，瀏覽器（Chrome、Safari、Edge 都可以）就會自動打開
4. 開始使用！

### 手機版（iPhone / Android）

**推薦做法：部署到 Netlify 後加到主畫面**

1. 把整個資料夾上傳到 [Netlify Drop](https://app.netlify.com/drop)（一次拖上去，不要分開）
2. 取得網址，例如 `xxx.netlify.app/錢錢管家v3.html`
3. 在手機上用瀏覽器打開該網址
4. **加到主畫面**：
   - **iPhone Safari**：點底部的「分享」按鈕 → 選「加入主畫面」
   - **Android Chrome**：點右上角選單 → 選「加到主畫面」

**離線可用 ✨**：本專案已內建 Service Worker，第一次連網開啟後，所有檔案會被自動快取，**之後沒網路也能正常使用**。

---

## 兩個工具分別是什麼

### 薪資計算機 — 算薪水用的

打開 **`薪資計算機v2.html`** 就可以使用。

**第一次使用：先新增工作**
1. 點下方的「💼 工作」
2. 輸入工作名稱（例如：咖啡店打工）
3. 選擇計費方式：
   - **時薪**：按小時算錢（例如 183 元/小時）
   - **堂薪**：按堂數算錢（例如家教 500 元/堂）
   - **日薪**：按天算固定金額
4. 輸入金額，按「新增工作」

**每次上完班：記錄薪資**
1. 點下方的「✏️ 記帳」
2. 選你的工作
3. 選日期
4. 填入上班時間（時薪）或堂數（堂薪）
5. 系統會自動算出薪水
6. 按「✅ 新增」就記好了

**看薪水統計**
- 點「📊 總覽」可以看這個月賺了多少、每天的收入圖表

### 錢錢管家 — 記帳用的

打開 **`錢錢管家v3.html`** 就可以使用。

**記一筆帳**
1. 點下方的「✏️ 記帳」
2. 選「💸 支出」或「💰 收入」
3. 輸入金額
4. 選類別（飲食、交通、購物...）
5. 選帳戶（現金、銀行、信用卡）
6. 按「✅ 新增」

**設定每月預算**
1. 點「⚙️ 設定」
2. 在「每月預算上限」輸入金額（例如 10000）
3. 回到「📊 總覽」就能看到預算還剩多少

**設定存錢目標**
1. 點「🎯 目標」
2. 輸入目標名稱（例如：買 Switch）和金額
3. 每次存錢就按「+存入」，可以追蹤進度

---

## 兩個工具怎麼連動

薪資計算機可以把薪水紀錄**自動同步**到錢錢管家，這樣你的薪水收入會自動出現在記帳裡。

**開啟同步：**
1. 打開**薪資計算機**
2. 點「⚙️ 設定」
3. 找到「同步至錢錢管家」，選擇**自動**
4. 之後每次記錄薪資，錢錢管家裡就會自動多一筆收入

> 兩個程式要用**同一個瀏覽器**打開才能同步。

---

## 怎麼備份資料（很重要！）

你的資料存在瀏覽器裡，**清除瀏覽器資料就會不見**，所以要定期備份。

**備份方法：**
1. 點「⚙️ 設定」
2. 找到「資料管理」
3. 點「JSON」匯出，會下載一個備份檔

**還原方法：**
1. 點「⚙️ 設定」→「資料管理」
2. 點「📥 匯入備份」
3. 選擇之前下載的備份檔

---

## 怎麼匯出報表

兩個工具都支援匯出報表，可以存到電腦或分享給別人：

| 格式 | 說明 | 適合用途 |
|------|------|----------|
| **Excel** | 試算表 | 用 Excel 或 Google 試算表開啟 |
| **PDF** | 文件 | 列印或傳給別人看 |
| **Word** | 文件 | 需要編輯內容時使用 |
| **CSV** | 純資料 | 匯入其他軟體 |
| **JSON** | 備份檔 | 備份還原用 |

---

## 切換深色/淺色模式

點「⚙️ 設定」裡的「主題模式」按鈕就能切換。兩個工具的主題設定會自動同步。

---

## 常見問題

**Q：資料不見了怎麼辦？**
A：如果有備份的 JSON 檔，可以用「匯入備份」還原。如果沒備份，很遺憾資料無法找回。所以記得定期備份！

**Q：換手機/換電腦，資料怎麼搬？**
A：在舊裝置匯出 JSON 備份 → 傳到新裝置 → 在新裝置匯入備份。

**Q：可以兩個人一起用嗎？**
A：目前不支援多人共用，每個瀏覽器的資料是獨立的。

**Q：用不同瀏覽器（例如 Chrome 和 Safari）資料會同步嗎？**
A：不會，每個瀏覽器的資料是各自獨立的。請固定使用同一個瀏覽器。

---

## 檔案說明

| 檔案 | 說明 |
|------|------|
| `薪資計算機v2.html` | 薪資計算機（主要版本，請用這個） |
| `錢錢管家v3.html` | 記帳程式（主要版本，請用這個） |
| `薪資計算機v1.html` | 薪資計算機舊版（保留參考） |
| `錢錢管家v2.html` | 記帳程式舊版（保留參考） |
| `使用說明書.pdf` | 完整使用說明書（PDF） |
| `使用說明書.docx` | 完整使用說明書（Word） |
| `build_docs.py` | 說明書產生腳本（docx） |
| `build_pdf.py` | 說明書產生腳本（pdf） |
| `index.html` | 首頁入口（含兩個 App 的選單） |
| `service-worker.js` | 離線快取機制（PWA 核心） |
| `manifest.json` | PWA 應用程式設定 |

---

# 技術細節

> 以下內容為本專案的完整技術文件，涵蓋架構設計、資料模型、同步機制、渲染策略及效能考量。

## 總體架構

本專案由兩個獨立的單頁應用程式（SPA）組成，每個應用程式為**單一 HTML 檔案**，內嵌所有 CSS 與 JavaScript，無需建置工具（No Build Step）、無需後端伺服器。

**核心設計原則：**
- **零安裝**：使用者用瀏覽器直接開啟 HTML 檔案即可運行
- **離線優先**：所有資料儲存於 `localStorage`，不依賴網路連線（僅匯出功能的外部程式庫需要 CDN）
- **行動裝置優先**：以 480px 為基準寬度設計，支援 iOS Safe Area

### 架構模式

兩個應用程式皆採用 **Centralized State + Full Re-render** 架構：

```
使用者操作 → 事件處理函數修改全域狀態 S → save() 持久化至 localStorage → render() 重新產生完整 HTML → innerHTML 替換 DOM
```

此模式類似早期 React 的理念（單向資料流），但不使用 Virtual DOM，而是直接以 Template Literal 組裝 HTML 字串後一次性注入 `innerHTML`。優點是實作簡單、無框架依賴；取捨是每次狀態變更都會重繪整個頁面（對本專案的資料量而言效能影響可忽略）。

---

## 狀態管理

### 薪資計算機 v2 — 全域狀態物件 `S`

```javascript
const S = {
  jobs: [],           // 工作類型列表（持久化至 wc2-jobs）
  records: [],        // 薪資紀錄列表（持久化至 wc2-records）
  settings: {         // 使用者設定（持久化至 wc2-settings）
    targetMonthlySalary: 0,
    syncMode: "manual"    // "manual" | "auto"
  },
  dark: true,         // 主題模式（持久化至 mm2-dark，與錢錢管家共用）
  view: "dashboard",  // 當前頁面：dashboard | add | history | jobs | settings
  month: "2026-04",   // 當前檢視月份（YYYY-MM 格式）
  search: "",         // 搜尋關鍵字
  sTab: "main",       // 設定頁面子分頁
  af: { ... },        // 新增紀錄表單狀態
  newJob: { ... },    // 新增工作表單狀態
  editJobId: null     // 編輯中的工作 ID
};
```

### 錢錢管家 v3 — 全域狀態物件 `S`

```javascript
const S = {
  tx: [],             // 交易紀錄列表（持久化至 mm2-tx）
  budget: 0,          // 每月預算上限（持久化至 mm2-budget）
  cats: [],           // 支出類別列表（持久化至 mm2-cats）
  accounts: [],       // 帳戶列表（持久化至 mm2-accounts）
  goals: [],          // 儲蓄目標列表（持久化至 mm2-goals）
  fixed: [],          // 固定支出列表（持久化至 mm2-fixed）
  dark: true,         // 主題模式（持久化至 mm2-dark，與薪資計算機共用）
  view: "dashboard",  // 當前頁面：dashboard | add | history | goals | settings
  month: "2026-04",   // 當前檢視月份
  search: "",         // 搜尋關鍵字
  sTab: "main",       // 設定頁面子分頁
  af: { ... },        // 新增交易表單狀態
  newCat: { ... },    // 新增類別表單狀態
  newGoal: { ... },   // 新增目標表單狀態
  newFixed: { ... }   // 新增固定支出表單狀態
};
```

### 持久化函數 `save()`

每個應用程式的 `save()` 函數將狀態物件中的持久化欄位序列化為 JSON 並寫入 `localStorage`：

```javascript
// 錢錢管家 v3 的 save()
function save() {
  localStorage.setItem("mm2-tx",       JSON.stringify(S.tx));
  localStorage.setItem("mm2-budget",   JSON.stringify(S.budget));
  localStorage.setItem("mm2-cats",     JSON.stringify(S.cats));
  localStorage.setItem("mm2-accounts", JSON.stringify(S.accounts));
  localStorage.setItem("mm2-goals",    JSON.stringify(S.goals));
  localStorage.setItem("mm2-fixed",    JSON.stringify(S.fixed));
  localStorage.setItem("mm2-dark",     JSON.stringify(S.dark));
}
```

---

## 資料模型

### localStorage Keys 總覽

| Key | 所屬應用程式 | 資料類型 | 說明 |
|-----|-------------|---------|------|
| `wc2-jobs` | 薪資計算機 | `Array<Job>` | 工作類型定義 |
| `wc2-records` | 薪資計算機 | `Array<Record>` | 薪資紀錄 |
| `wc2-settings` | 薪資計算機 | `Object` | 使用者設定 |
| `mm2-tx` | 錢錢管家 | `Array<Transaction>` | 交易紀錄（薪資計算機同步時也會寫入此 key） |
| `mm2-budget` | 錢錢管家 | `Number` | 每月預算上限 |
| `mm2-cats` | 錢錢管家 | `Array<Category>` | 自訂支出類別 |
| `mm2-accounts` | 錢錢管家 | `Array<Account>` | 帳戶列表 |
| `mm2-goals` | 錢錢管家 | `Array<Goal>` | 儲蓄目標 |
| `mm2-fixed` | 錢錢管家 | `Array<FixedExpense>` | 固定支出 |
| `mm2-dark` | **共用** | `Boolean` | 深色模式開關（兩個應用程式共用） |

### 資料結構定義

**Job（工作類型）**
```json
{
  "id": "m1abc2def3",
  "name": "咖啡店打工",
  "billingType": "hourly",
  "rate": 183,
  "color": "#E8590C",
  "active": true,
  "sessionDurationMinutes": null
}
```

| 欄位 | 型別 | 說明 |
|------|------|------|
| `id` | `string` | 唯一識別碼，由 `Date.now().toString(36) + Math.random().toString(36).slice(2,7)` 生成 |
| `name` | `string` | 工作名稱 |
| `billingType` | `"hourly" \| "perSession" \| "daily"` | 計費方式：時薪 / 堂薪 / 日薪 |
| `rate` | `number` | 費率（整數，單位：新台幣） |
| `color` | `string` | 圖表顯示色（Hex） |
| `active` | `boolean` | 是否啟用（停用後不出現在記帳選單） |
| `sessionDurationMinutes` | `number \| null` | 每堂時長（分鐘），僅 `perSession` 使用 |

**Record（薪資紀錄）**
```json
{
  "id": "m1xyz4uvw5",
  "jobId": "m1abc2def3",
  "date": "2026-04-10",
  "startTime": "18:00",
  "endTime": "20:00",
  "durationMinutes": 120,
  "breakMinutes": 0,
  "sessions": 0,
  "calculatedPay": 366,
  "notes": "加班",
  "createdAt": "2026-04-10T15:30:45.123Z",
  "syncedToMM": true
}
```

| 欄位 | 型別 | 說明 |
|------|------|------|
| `id` | `string` | 唯一識別碼 |
| `jobId` | `string` | 關聯的工作 ID（外鍵） |
| `date` | `string` | 工作日期（ISO 格式 `YYYY-MM-DD`） |
| `startTime` | `string` | 開始時間（`HH:MM`，非時薪制為空） |
| `endTime` | `string` | 結束時間（`HH:MM`，非時薪制為空） |
| `durationMinutes` | `number` | 工作時長（分鐘） |
| `breakMinutes` | `number` | 休息時間（分鐘，預設選項 0/30/60/90 或自訂） |
| `sessions` | `number` | 堂數（僅堂薪制使用） |
| `calculatedPay` | `number` | 計算後薪資（整數） |
| `notes` | `string` | 備註 |
| `createdAt` | `string` | 建立時間（ISO 8601） |
| `syncedToMM` | `boolean` | 是否已同步至錢錢管家 |

**薪資計算邏輯：**
```javascript
function calcPay(job, rec) {
  if (job.billingType === "hourly") {
    return Math.round(((rec.durationMinutes - rec.breakMinutes) / 60) * job.rate);
  }
  if (job.billingType === "perSession") {
    return Math.round(rec.sessions * job.rate);
  }
  return Math.round(job.rate);  // daily
}
```

**Transaction（交易紀錄）**
```json
{
  "id": "m1pqr6stu7",
  "type": "expense",
  "amount": 150,
  "category": "food",
  "account": "cash",
  "note": "午餐便當",
  "date": "2026-04-10"
}
```

| 欄位 | 型別 | 說明 |
|------|------|------|
| `id` | `string` | 唯一識別碼 |
| `type` | `"expense" \| "income"` | 交易類型 |
| `amount` | `number` | 金額（整數） |
| `category` | `string` | 類別 ID（支出用，收入固定為 `"income"`） |
| `account` | `string` | 帳戶 ID（`"cash"` / `"bank"` / `"credit"` 或自訂） |
| `note` | `string` | 備註（同步來的紀錄以 `[薪資]` 開頭） |
| `date` | `string` | 日期（`YYYY-MM-DD`） |

**Category（支出類別）**
```json
{ "id": "food", "label": "飲食", "icon": "🍜", "color": "#E8590C" }
```

預設 8 個類別：飲食、交通、購物、娛樂、帳單、醫療、教育、其他。使用者可自訂新增（從 20 個 Emoji 和 12 色調色盤中選擇），但不能刪除預設類別。

**Account（帳戶）**
```json
{ "id": "cash", "label": "現金", "icon": "💵" }
```

預設 3 個帳戶：現金、銀行、信用卡。使用者可新增自訂帳戶。

**Goal（儲蓄目標）**
```json
{ "id": "m1ghi8jkl9", "name": "買 Switch", "target": 9780, "saved": 3000 }
```

進度計算：`Math.min((saved / target) * 100, 100)`，達標時顯示完成標記。支援存入（+）和取出（-）操作，`saved` 下限為 0。

**FixedExpense（固定支出）**
```json
{ "id": "m1mno0pqr1", "name": "房租", "amount": 8000, "category": "bills", "day": "1" }
```

`day` 為每月幾號（1-28）。系統會在到期前 3 天於總覽頁面顯示提醒，並提供「快速記帳」按鈕一鍵轉為交易紀錄。

---

## 跨應用程式同步機制

### 同步方向

```
薪資計算機 v2 ──寫入──→ mm2-tx (localStorage) ──監聽──→ 錢錢管家 v3
```

同步為**單向**：薪資計算機將薪資紀錄轉換為收入交易，寫入錢錢管家的 `mm2-tx` key。

### 寫入端（薪資計算機 v2）

```javascript
function syncRecord(rec) {
  const j = S.jobs.find(x => x.id === rec.jobId);
  if (!j) return;
  const mmTx = JSON.parse(localStorage.getItem("mm2-tx") || "[]");
  mmTx.unshift({
    id: gId(),
    type: "income",
    amount: rec.calculatedPay,
    category: "income",
    account: "bank",
    note: "[薪資] " + j.name + (rec.notes ? " · " + rec.notes : ""),
    date: rec.date
  });
  localStorage.setItem("mm2-tx", JSON.stringify(mmTx));
  rec.syncedToMM = true;
  save();
}
```

**資料轉換規則：**
- `Record.calculatedPay` → `Transaction.amount`
- `type` 固定為 `"income"`
- `account` 固定為 `"bank"`
- `note` 格式：`"[薪資] {工作名稱}"` 或 `"[薪資] {工作名稱} · {備註}"`
- 寫入後將原始紀錄標記 `syncedToMM: true`

**同步模式：**
- `auto`：在 `addRec()` 新增紀錄時自動呼叫 `syncRecord()`
- `manual`：使用者手動點擊按鈕觸發 `syncAllUnsynced()`，批次同步所有 `syncedToMM !== true` 的紀錄

### 接收端（錢錢管家 v3）

```javascript
window.addEventListener("storage", function(e) {
  if (e.key === "mm2-tx" && e.newValue) {
    const incoming = JSON.parse(e.newValue);
    const existIds = new Set(S.tx.map(t => t.id));
    const newItems = incoming.filter(t => !existIds.has(t.id));
    if (newItems.length) {
      S.tx = newItems.concat(S.tx);
      save();
      render();
      toast("已同步 " + newItems.length + " 筆薪資紀錄");
    }
  }
  if (e.key === "mm2-dark" && e.newValue != null) {
    S.dark = JSON.parse(e.newValue);
    render();
  }
});
```

**同步機制說明：**

利用瀏覽器原生的 [`StorageEvent`](https://developer.mozilla.org/en-US/docs/Web/API/StorageEvent)。當**同源（same-origin）的不同分頁**修改 `localStorage` 時，其他分頁會收到 `storage` 事件。

**去重邏輯：**
1. 將現有交易的 ID 建立 `Set`（O(1) 查詢）
2. 從 incoming 資料中過濾出本地不存在的新交易
3. 將新交易 prepend 到現有交易列表
4. 呼叫 `save()` 持久化、`render()` 更新畫面

**注意事項：**
- `storage` 事件**僅在不同分頁間觸發**，同一分頁內的 `localStorage.setItem()` 不會觸發自身的 `storage` 事件
- 兩個 HTML 檔案必須從**相同 origin** 開啟（例如同一資料夾的 `file://` 協議）
- 同時監聽 `mm2-dark` key，實現跨分頁主題同步

---

## 渲染系統

### 全頁面重繪策略

```javascript
function render() {
  applyTheme();                    // 更新 body class 和 meta theme-color
  const t = T();                   // 取得當前主題色彩 token
  // ... 根據 S.view 組裝 HTML 字串（200+ 行 template literal）
  document.getElementById("content").innerHTML = html;
}
```

每次狀態變更後呼叫 `render()`，透過單次 `innerHTML` 賦值替換整個內容區域。事件處理器以 inline `onclick` 屬性綁定，在 `innerHTML` 替換時自動清除（無記憶體洩漏風險）。

### 主題系統

`T()` 函數根據 `S.dark` 布林值回傳完整色彩配置物件：

```javascript
function T() {
  const d = S.dark;
  return {
    bg:     d ? "#111"    : "#f5f5f5",   // 頁面背景
    card:   d ? "#1a1a1a" : "#fff",      // 卡片背景
    border: d ? "#2a2a2a" : "#e0e0e0",   // 邊框色
    input:  d ? "#222"    : "#f0f0f0",   // 輸入框背景
    ib:     d ? "#333"    : "#d0d0d0",   // 輸入框邊框
    text:   d ? "#e0e0e0" : "#1a1a1a",   // 主要文字
    dim:    d ? "#888"    : "#666",      // 次要文字
    dimmer: d ? "#555"    : "#aaa",      // 最淡文字
    w:      d ? "#fff"    : "#1a1a1a",   // 強調文字
    toast:  d ? "#2d2d2d" : "#333",      // Toast 背景
    niA:    d ? "#1e1e1e" : "#e8e8e8"    // 導航列未選中背景
  };
}
```

色彩 token 透過 template literal 內聯注入至 `style` 屬性，未使用 CSS Custom Properties。`applyTheme()` 負責切換 `body.dark` / `body.light` class 並更新 `<meta name="theme-color">`。

### 圖表渲染

**環形圖（Donut Chart）— SVG Path**

以三角函數計算各分類的圓弧路徑：

```javascript
// 計算弧線起止點
const startAngle = accumulated * 2 * Math.PI - Math.PI / 2;
const endAngle = (accumulated + fraction) * 2 * Math.PI - Math.PI / 2;

// SVG arc 指令
`<path d="M ${x1} ${y1} A 70 70 0 ${largeArc} 1 ${x2} ${y2}"
       stroke="${color}" stroke-width="20" fill="none"/>`
```

- 半徑 70px，圓心 (90, 90)，線寬 20px
- 當某分類佔比 >= 99.99% 時，繪製完整圓形（避免弧線退化）
- 圓心顯示總金額

**長條圖（Bar Chart）— CSS Flexbox**

```javascript
// 每天一條，高度按比例計算
const height = Math.max(4, (dayAmount / maxAmount) * 48);  // 最低 4px
`<div class="daily-bar" style="height:${height}px;
     background:linear-gradient(180deg, #51cf66, #339af0)"></div>`
```

使用 `align-items: flex-end` 的 Flex 容器實現底部對齊。

---

## 匯出系統

### 插件式架構（Plugin Registry Pattern）

```javascript
const ExportManager = {
  exporters: {},
  register(format, fn) { this.exporters[format] = fn; },
  async doExport(format, data) {
    const exporter = this.exporters[format];
    if (!exporter) throw new Error("Unknown format");
    const result = await exporter(data);
    if (result) this.download(result.blob, result.filename);
  },
  download(blob, filename) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(() => URL.revokeObjectURL(url), 1000);  // 延遲釋放記憶體
  }
};
```

6 種匯出格式各自注冊為獨立函數，回傳 `{ blob: Blob, filename: string }`：

| 格式 | 實作重點 |
|------|---------|
| **JSON** | BOM 前綴 `\uFEFF` 確保 UTF-8 編碼，附加 `exportDate` 時戳，Pretty Print 2 格縮排 |
| **CSV** | BOM 前綴，逗號分隔，雙引號跳脫（`"` → `""`），中文欄位標頭 |
| **Markdown** | Pipe 表格語法，底部顯示總計，附時戳 |
| **XLSX** | SheetJS 產生，雙工作表（紀錄 + 摘要），自訂欄寬 |
| **DOCX** | docx 程式庫，Microsoft JhengHei 字體，置中標題，粗體表頭，右對齊總計 |
| **PDF** | jsPDF + AutoTable，橫向排版，交替列底色 `[240, 245, 255]`，每頁顯示總計頁腳 |

薪資計算機額外支援**按工作篩選匯出**及**匯出為錢錢管家 JSON 格式**（用於跨裝置還原）。

---

## CSS 與響應式設計

### 行動裝置適配

```css
body {
  max-width: 480px;
  margin: 0 auto;
  min-height: 100vh;
  min-height: 100dvh;                              /* Dynamic Viewport Height */
  padding-top: env(safe-area-inset-top);            /* iPhone 瀏海適配 */
  font-family: 'Noto Sans TC', -apple-system, 'Helvetica Neue', sans-serif;
}

.content {
  padding-bottom: calc(20px + env(safe-area-inset-bottom));  /* Home Indicator 適配 */
  -webkit-overflow-scrolling: touch;                          /* iOS 慣性滾動 */
}
```

- **`100dvh`**：使用 Dynamic Viewport Height，自動扣除手機瀏覽器網址列高度（含 `100vh` 作為 fallback）
- **`env(safe-area-inset-*)`**：支援 iPhone X 以後的瀏海和底部 Home Indicator 安全區域
- **`viewport-fit=cover`**：透過 viewport meta tag 啟用全螢幕佈局

### Viewport Meta Tag

```html
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
```

### Apple Web App 支援

```html
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="薪資計算機">
<meta name="theme-color" content="#111111">
```

加入主畫面後以全螢幕模式運行，狀態列半透明黑色，`theme-color` 隨主題動態更新。

### 佈局系統

- **Flexbox**：主要佈局方式，頁面結構、卡片排列、導航列
- **CSS Grid**：類別選擇按鈕（`grid-template-columns: repeat(4, 1fr)`）、匯出格式按鈕

### 動畫與過渡

```css
body         { transition: background .3s, color .3s; }   /* 主題切換漸變 */
.nav-item    { transition: all .2s; }                      /* 導航切換 */
.p-fill      { transition: width .5s ease; }               /* 進度條填充 */
.daily-bar   { transition: height .3s; }                   /* 長條圖動畫 */
.toast       { transition: opacity .3s; }                  /* Toast 淡入淡出 */
```

### 跨瀏覽器相容性

```css
-webkit-tap-highlight-color: transparent;   /* 移除 iOS 點擊高亮 */
-webkit-overflow-scrolling: touch;          /* iOS 慣性滾動 */
-webkit-appearance: none;                   /* 移除原生 select 樣式 */
appearance: none;                           /* 標準寫法 */
```

---

## 外部依賴

| 程式庫 | 版本 | CDN | 用途 | 載入方式 |
|--------|------|-----|------|---------|
| **SheetJS (xlsx)** | 0.20.3 | `cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js` | Excel 匯出 | `<script>` 同步載入 |
| **jsPDF** | 2.5.1 | `cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js` | PDF 產生 | `<script>` 同步載入 |
| **jsPDF-AutoTable** | 3.8.2 | `cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js` | PDF 表格排版 | `<script>` 同步載入 |
| **docx** | 8.5.0 | `cdn.jsdelivr.net/npm/docx@8.5.0/build/index.umd.min.js` | Word 文件產生 | `<script>` 同步載入 |
| **Google Fonts** | — | `fonts.googleapis.com` | Noto Sans TC 字型 | `<link>` stylesheet |

所有程式庫皆以 UMD 格式載入，掛載於 `window` 全域物件（`window.XLSX`、`window.jspdf`、`window.docx`）。

**原生 Web API 使用：**
- `localStorage`：資料持久化
- `StorageEvent`：跨分頁同步
- `Blob` / `URL.createObjectURL()`：檔案下載
- `FileReader`：JSON 匯入
- `SVG`：圖表渲染
- `CSS env()`：Safe Area 適配

---

## 效能考量

| 面向 | 現況 | 說明 |
|------|------|------|
| **DOM 更新** | 全頁面 `innerHTML` 替換 | 每次狀態變更重繪整個 content 區域。對於一般使用量（每月數十至數百筆紀錄）無明顯效能問題 |
| **事件處理** | Inline `onclick` 屬性 | 隨 `innerHTML` 替換自動回收，無需手動解除綁定，避免記憶體洩漏 |
| **資料過濾** | 每次 render 進行 O(n) 陣列過濾 | 按月份篩選紀錄，n 為總紀錄數。千筆以下無感 |
| **同步去重** | `Set` 查詢 O(1) | 接收同步資料時建立 ID Set，過濾重複紀錄效率良好 |
| **記憶體管理** | `URL.revokeObjectURL()` 延遲 1 秒釋放 | 匯出下載後釋放 Blob URL，防止記憶體洩漏 |
| **CSS 動畫** | 純 CSS `transition` | 不使用 JavaScript 動畫，由 GPU 加速處理 |
| **Virtual Scrolling** | 未實作 | 歷史紀錄一次渲染當月所有筆數。若單月超過數百筆可能需要優化 |

---

## 設計決策與取捨

| 決策 | 理由 |
|------|------|
| **單一 HTML 檔案** | 降低使用門檻，不需要任何安裝或建置步驟 |
| **不使用框架** | 減少依賴、檔案體積小、載入快速、長期維護不受框架版本更迭影響 |
| **localStorage 而非 IndexedDB** | API 更簡單，同步操作，對本專案的資料量（< 5MB）綽綽有餘 |
| **`innerHTML` 而非 DOM API** | 程式碼更簡潔直觀，對本專案的 DOM 複雜度而言效能差異可忽略 |
| **Inline style 而非 CSS Variables** | 主題色彩在 render 時動態注入，省去 CSS Variable 更新與級聯計算 |
| **CDN 載入而非打包** | 不需要 Webpack / Vite 等建置工具，但離線時匯出功能不可用 |
| **SVG 而非 Canvas** | 宣告式語法，易於動態生成，支援高 DPI 螢幕，無需處理像素比 |
