#!/usr/bin/env python3
"""Generate 使用說明書.docx and 使用說明書.pdf from markdown content."""
import zipfile, os, io

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# ─── DOCX Generation ───────────────────────────────────────────────
def esc(t):
    return t.replace("&","&amp;").replace("<","&lt;").replace(">","&gt;").replace('"',"&quot;")

def run(text, bold=False, size=24, font="Microsoft JhengHei", color=None):
    rpr = f'<w:rPr><w:rFonts w:ascii="{font}" w:eastAsia="{font}" w:hAnsi="{font}"/><w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
    if bold: rpr += '<w:b/><w:bCs/>'
    if color: rpr += f'<w:color w:val="{color}"/>'
    rpr += '</w:rPr>'
    return f'<w:r>{rpr}<w:t xml:space="preserve">{esc(text)}</w:t></w:r>'

def para(text, style=None, bold=False, size=24, alignment=None, spacing_before=0, spacing_after=120, color=None):
    ppr = '<w:pPr>'
    if style: ppr += f'<w:pStyle w:val="{style}"/>'
    ppr += f'<w:spacing w:before="{spacing_before}" w:after="{spacing_after}"/>'
    if alignment: ppr += f'<w:jc w:val="{alignment}"/>'
    ppr += '</w:pPr>'
    return f'<w:p>{ppr}{run(text, bold=bold, size=size, color=color)}</w:p>'

def heading(text, level):
    sizes = {1: 36, 2: 30, 3: 26}
    sid = f"Heading{level}"
    sz = sizes.get(level, 24)
    sb = {1: 360, 2: 240, 3: 180}.get(level, 120)
    return para(text, style=sid, bold=True, size=sz, spacing_before=sb, spacing_after=120)

def table_cell(text, bold=False, shading=None, size=20):
    shade = ""
    if shading:
        shade = f'<w:shd w:val="clear" w:color="auto" w:fill="{shading}"/>'
    tc_pr = f'<w:tcPr><w:tcW w:w="0" w:type="auto"/>{shade}<w:tcMar><w:top w:w="60" w:type="dxa"/><w:bottom w:w="60" w:type="dxa"/><w:left w:w="100" w:type="dxa"/><w:right w:w="100" w:type="dxa"/></w:tcMar></w:tcPr>'
    return f'<w:tc>{tc_pr}{para(text, bold=bold, size=size, spacing_after=0)}</w:tc>'

def table_row(cells, header=False, shading=None):
    sh = shading if shading else ("D5E8F0" if header else None)
    tcs = "".join(table_cell(c, bold=header, shading=sh, size=20) for c in cells)
    trpr = '<w:trPr><w:tblHeader/></w:trPr>' if header else ''
    return f'<w:tr>{trpr}{tcs}</w:tr>'

def table(headers, rows):
    border = '<w:top w:val="single" w:sz="4" w:space="0" w:color="AAAAAA"/><w:left w:val="single" w:sz="4" w:space="0" w:color="AAAAAA"/><w:bottom w:val="single" w:sz="4" w:space="0" w:color="AAAAAA"/><w:right w:val="single" w:sz="4" w:space="0" w:color="AAAAAA"/><w:insideH w:val="single" w:sz="4" w:space="0" w:color="AAAAAA"/><w:insideV w:val="single" w:sz="4" w:space="0" w:color="AAAAAA"/>'
    tbl_pr = f'<w:tblPr><w:tblW w:w="5000" w:type="pct"/><w:tblBorders>{border}</w:tblBorders><w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" w:firstColumn="1" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr>'
    hr = table_row(headers, header=True)
    rs = "".join(table_row(r) for r in rows)
    return f'<w:tbl>{tbl_pr}{hr}{rs}</w:tbl>'

def hr_line():
    return '<w:p><w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="1" w:color="CCCCCC"/></w:pBdr><w:spacing w:before="120" w:after="120"/></w:pPr></w:p>'

def build_docx():
    body_parts = []
    P = body_parts.append

    # Title
    P(para("薪資計算機 & 錢錢管家", bold=True, size=44, alignment="center", spacing_after=60, color="2E75B6"))
    P(para("使用說明書", bold=True, size=32, alignment="center", spacing_after=60, color="555555"))
    P(para("版本：v2.0 / v3.0　更新日期：2026-04-13", size=20, alignment="center", spacing_after=200, color="888888"))
    P(hr_line())

    # 一、概述
    P(heading("一、概述", 1))
    P(para("本專案包含兩個互相串接的行動網頁應用程式："))
    P(table(["應用程式","檔案","用途"],[
        ["薪資計算機 v2","薪資計算機v2.html","打工、家教薪資紀錄與計算"],
        ["錢錢管家 v3","錢錢管家v3.html","日常收支記帳與預算管理"],
    ]))
    P(para("兩者皆為單一 HTML 檔案，無需安裝，使用瀏覽器直接開啟即可。資料儲存在瀏覽器的 localStorage 中。", spacing_before=120))
    P(heading("舊版檔案（保留用）", 3))
    P(table(["檔案","說明"],[
        ["薪資計算機.html","v1 原版（SVG 風格、底部導航）"],
        ["錢錢管家v2.html","v2 原版（僅 CSV + JSON 匯出）"],
    ]))

    # 二、快速開始
    P(heading("二、快速開始", 1))
    P(heading("1. 開啟方式", 2))
    P(para("直接在瀏覽器中開啟 HTML 檔案即可使用。"))
    P(para("重要：若要使用兩個程式之間的「同步」功能，必須從相同來源開啟兩個檔案（例如同一個資料夾用 file:/// 協議開啟，或透過同一個本地伺服器）。", bold=True, size=22, color="C00000"))
    P(heading("2. 手機使用", 2))
    P(para("兩個程式皆為行動裝置最佳化設計（480px 寬度），支援 iOS Safari「加入主畫面」、深色/淺色模式自動同步、安全區域適配（瀏海手機）。"))

    # 三、薪資計算機
    P(heading("三、薪資計算機 v2 功能說明", 1))
    P(heading("導航列", 2))
    P(table(["頁籤","圖示","功能"],[
        ["總覽","📊","月度收入摘要、圖表、目標進度"],
        ["記帳","✏️","新增薪資紀錄"],
        ["明細","📋","瀏覽、搜尋、刪除紀錄"],
        ["工作","💼","管理工作類型"],
        ["設定","⚙️","主題、目標薪資、同步、匯出"],
    ]))

    P(heading("3.1 工作管理（💼 工作）", 2))
    P(para("使用前需先建立工作類型。"))
    P(para("新增工作步驟：", bold=True))
    P(para("1. 前往「工作」頁籤"))
    P(para("2. 填入工作名稱（例如「王同學家教」「咖啡店打工」）"))
    P(para("3. 選擇計費方式："))
    P(table(["計費方式","說明"],[
        ["時薪","按工作時數計算（扣除休息時間）"],
        ["堂薪","按上課堂數計算"],
        ["日薪","按天計算固定金額"],
    ]))
    P(para("4. 設定費率、顏色，點擊「新增工作」"))
    P(para("編輯/停用/刪除：點擊工作旁的「編輯」按鈕，可修改所有欄位。「停用」後不會出現在記帳選擇中。", spacing_before=120))

    P(heading("3.2 記帳（✏️ 記帳）", 2))
    P(para("1. 選擇工作 → 2. 選擇日期 → 3. 填入對應資訊 → 4. 點擊「✅ 新增」"))
    P(para("薪資計算邏輯：", bold=True, spacing_before=120))
    P(table(["計費方式","計算公式"],[
        ["時薪","(工作時長 - 休息時間) ÷ 60 × 時薪費率"],
        ["堂薪","堂數 × 堂薪費率"],
        ["日薪","日薪費率（固定）"],
    ]))
    P(para("時薪模式下可設定休息時間：0 / 30 / 60 / 90 分鐘或自訂。", spacing_before=80))

    P(heading("3.3 總覽（📊 總覽）", 2))
    P(para("月度摘要卡片：總收入、工作天數、平均日薪"))
    P(para("目標進度：若已設定目標薪資，顯示進度條"))
    P(para("收入分佈：環形圖，按工作分類顯示收入比例"))
    P(para("每日收入：長條圖，顯示每天的收入分佈"))
    P(para("工作摘要：各工作的累計時數/堂數與總薪資"))

    P(heading("3.4 明細（📋 明細）", 2))
    P(para("顯示當月所有紀錄，支援搜尋。已同步紀錄會顯示「已同步」標籤。刪除已同步紀錄時會提醒使用者至錢錢管家手動移除。"))

    P(heading("3.5 設定（⚙️ 設定）", 2))
    P(para("主題模式：深色/淺色切換（與錢錢管家同步）"))
    P(para("每月目標薪資：設定後會在總覽顯示進度"))
    P(para("同步至錢錢管家：詳見第五章"))

    # 四、錢錢管家
    P(heading("四、錢錢管家 v3 功能說明", 1))
    P(heading("導航列", 2))
    P(table(["頁籤","圖示","功能"],[
        ["總覽","📊","月度收支摘要、圖表"],
        ["記帳","✏️","新增收入/支出"],
        ["明細","📋","瀏覽、搜尋、刪除紀錄"],
        ["目標","🎯","儲蓄目標、固定支出"],
        ["設定","⚙️","主題、預算、類別、匯出"],
    ]))

    P(heading("4.1 記帳", 2))
    P(para("選擇類型（支出/收入）→ 輸入金額 → 選擇帳戶 → 選擇類別（僅支出）→ 選擇日期 → 備註 → 新增"))
    P(para("預設類別：飲食、交通、購物、娛樂、帳單、醫療、教育、其他（可在設定中自訂新增）"))

    P(heading("4.2 總覽", 2))
    P(para("收支摘要（支出/收入/結餘）、上月比較、預算進度、支出分佈環形圖（含上月比較）、每日支出長條圖、帳戶分佈、近期固定支出提醒。"))

    P(heading("4.3 明細", 2))
    P(para("月度紀錄列表，支援搜尋。來自薪資計算機同步的紀錄會顯示「薪資計算機」標籤。"))

    P(heading("4.4 目標", 2))
    P(para("儲蓄目標：建立目標（名稱 + 目標金額），可隨時存入/取出，顯示進度條。"))
    P(para("固定支出：建立固定支出（名稱、金額、每月幾號），支援快速記帳，到期前 3 天自動提醒。"))

    P(heading("4.5 設定", 2))
    P(para("主題模式、每月預算上限、自訂類別（圖示+顏色）、帳戶管理、資料管理（匯出/匯入/清除）。"))

    # 五、同步機制
    P(heading("五、同步機制", 1))
    P(para("同步方向：薪資計算機 → 錢錢管家（單向）", bold=True, size=24, color="2E75B6"))
    P(para("薪資計算機的紀錄可同步到錢錢管家作為「收入」紀錄。反向不支援。", spacing_before=80))
    P(heading("同步模式", 2))
    P(table(["模式","說明"],[
        ["自動","每次新增紀錄時自動同步"],
        ["手動","手動點擊「同步」按鈕才同步"],
    ]))
    P(heading("同步後的紀錄", 2))
    P(para("在錢錢管家的明細中，同步來的紀錄備註以 [薪資] 開頭，顯示「薪資計算機」標籤。帳戶預設為「銀行」，類別為「收入」。"))
    P(heading("注意事項", 2))
    P(para("同步為單向，修改或刪除已同步的紀錄時，需至對應的程式手動處理。", color="C00000"))
    P(para("刪除已同步紀錄時，薪資計算機會彈出提醒。"))

    # 六、匯出功能
    P(heading("六、匯出功能", 1))
    P(para("兩個程式皆支援 6 種匯出格式："))
    P(table(["格式","副檔名","說明"],[
        ["JSON",".json","完整結構化資料，可用於備份還原"],
        ["CSV",".csv","Excel / Google Sheets 可開啟"],
        ["Markdown",".md","純文字表格，適合筆記軟體"],
        ["Excel",".xlsx","含紀錄 + 摘要雙工作表"],
        ["Word",".docx","排版好的表格文件"],
        ["PDF",".pdf","橫向排版，適合列印或分享"],
    ]))
    P(heading("薪資計算機額外功能", 2))
    P(para("工作篩選：可選擇只匯出特定工作的紀錄（方便和家長報帳）"))
    P(para("匯出錢錢管家 JSON 格式：將薪資資料轉換為錢錢管家可匯入的格式"))

    # 七、備份
    P(heading("七、資料備份與還原", 1))
    P(para("匯出備份：前往「設定 → 資料管理」，選擇 JSON 格式匯出。", bold=True))
    P(para("匯入還原：點擊「📥 匯入備份」，選擇 .json 檔案。資料會完全覆蓋現有資料。", bold=True))
    P(para("清除資料：點擊「🗑️ 清除資料」。此操作不可還原，請先備份。", bold=True, color="C00000"))

    # 八、深色模式
    P(heading("八、深色/淺色模式", 1))
    P(para("兩個程式共用深色模式設定（儲存在 mm2-dark）。在任一程式中切換主題，另一個重新整理後即同步。預設為深色模式。"))

    # 九、技術資訊
    P(heading("九、技術資訊", 1))
    P(heading("資料儲存位置（localStorage keys）", 2))
    P(table(["Key","應用程式","內容"],[
        ["wc2-jobs","薪資計算機","工作類型"],
        ["wc2-records","薪資計算機","薪資紀錄"],
        ["wc2-settings","薪資計算機","設定"],
        ["mm2-tx","錢錢管家","交易紀錄"],
        ["mm2-budget","錢錢管家","預算"],
        ["mm2-cats","錢錢管家","類別"],
        ["mm2-accounts","錢錢管家","帳戶"],
        ["mm2-goals","錢錢管家","儲蓄目標"],
        ["mm2-fixed","錢錢管家","固定支出"],
        ["mm2-dark","共用","深色模式"],
    ]))
    P(heading("使用的外部程式庫", 2))
    P(table(["程式庫","版本","用途"],[
        ["SheetJS (xlsx)","0.20.3","Excel 匯出"],
        ["jsPDF","2.5.1","PDF 匯出"],
        ["jspdf-autotable","3.8.2","PDF 表格"],
        ["docx","8.5.0","Word 匯出"],
    ]))

    # 十、FAQ
    P(heading("十、常見問題", 1))
    faqs = [
        ("Q: 兩個程式的資料不互通怎麼辦？","A: 請確認兩個 HTML 檔案是從相同來源（同一資料夾）開啟的。不同來源的 localStorage 是隔離的。"),
        ("Q: 手機上資料會消失嗎？","A: localStorage 在清除瀏覽器資料時會被刪除。建議定期使用 JSON 匯出功能備份。"),
        ("Q: 可以多裝置同步嗎？","A: 目前不支援雲端同步。可透過匯出 JSON → 傳送到另一裝置 → 匯入的方式手動同步。"),
    ]
    for q, a in faqs:
        P(para(q, bold=True, spacing_before=120))
        P(para(a))

    P(hr_line())
    P(para("本說明書涵蓋薪資計算機 v2.0 與錢錢管家 v3.0 的所有功能。", size=20, alignment="center", color="888888"))

    body_xml = "".join(body_parts)

    # Build DOCX ZIP
    content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
</Types>'''

    rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

    word_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
</Relationships>'''

    document = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:wpc="http://schemas.microsoft.com/office/word/2010/wordprocessingCanvas" xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" xmlns:o="urn:schemas-microsoft-com:office:office" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:wp14="http://schemas.microsoft.com/office/word/2010/wordprocessingDrawing" xmlns:wp="http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing" xmlns:w10="urn:schemas-microsoft-com:office:word" xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:w14="http://schemas.microsoft.com/office/word/2010/wordml" xmlns:wpg="http://schemas.microsoft.com/office/word/2010/wordprocessingGroup" xmlns:wpi="http://schemas.microsoft.com/office/word/2010/wordprocessingInk" xmlns:wne="http://schemas.microsoft.com/office/word/2006/wordml" xmlns:wps="http://schemas.microsoft.com/office/word/2010/wordprocessingShape" mc:Ignorable="w14 wp14">
<w:body>{body_xml}
<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>
</w:body></w:document>'''

    styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Microsoft JhengHei" w:eastAsia="Microsoft JhengHei" w:hAnsi="Microsoft JhengHei" w:cs="Microsoft JhengHei"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:rPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:styleId="Normal"><w:name w:val="Normal"/><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:bCs/><w:sz w:val="36"/><w:szCs w:val="36"/><w:color w:val="2E75B6"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="120"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:bCs/><w:sz w:val="30"/><w:szCs w:val="30"/><w:color w:val="2E75B6"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:pPr><w:keepNext/><w:keepLines/><w:spacing w:before="180" w:after="120"/><w:outlineLvl w:val="2"/></w:pPr><w:rPr><w:b/><w:bCs/><w:sz w:val="26"/><w:szCs w:val="26"/><w:color w:val="2E75B6"/></w:rPr></w:style>
</w:styles>'''

    docx_path = os.path.join(OUT_DIR, "使用說明書.docx")
    with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", content_types)
        z.writestr("_rels/.rels", rels)
        z.writestr("word/_rels/document.xml.rels", word_rels)
        z.writestr("word/document.xml", document)
        z.writestr("word/styles.xml", styles)
    print(f"Created: {docx_path}")

if __name__ == "__main__":
    build_docx()
