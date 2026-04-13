#!/usr/bin/env python3
"""Generate 使用說明書.pdf with Chinese support."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm, cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                 HRFlowable, PageBreak, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont

# Register Chinese font
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
FONT = 'STSong-Light'

OUT_DIR = os.path.dirname(os.path.abspath(__file__))

# Colors
BLUE = HexColor('#2E75B6')
LIGHT_BLUE = HexColor('#D5E8F0')
GRAY = HexColor('#888888')
DARK = HexColor('#333333')
RED = HexColor('#C00000')
TABLE_BORDER = HexColor('#AAAAAA')
TABLE_HEADER_BG = HexColor('#2E75B6')
TABLE_ALT_BG = HexColor('#F2F7FB')

# Styles
styles = getSampleStyleSheet()

style_normal = ParagraphStyle('CN_Normal', fontName=FONT, fontSize=10, leading=15,
                               textColor=DARK, spaceAfter=6)
style_bold = ParagraphStyle('CN_Bold', parent=style_normal, fontName=FONT, fontSize=10,
                             leading=15, spaceAfter=6)
style_h1 = ParagraphStyle('CN_H1', fontName=FONT, fontSize=18, leading=24,
                            textColor=BLUE, spaceBefore=20, spaceAfter=10)
style_h2 = ParagraphStyle('CN_H2', fontName=FONT, fontSize=14, leading=19,
                            textColor=BLUE, spaceBefore=14, spaceAfter=8)
style_h3 = ParagraphStyle('CN_H3', fontName=FONT, fontSize=12, leading=16,
                            textColor=BLUE, spaceBefore=10, spaceAfter=6)
style_title = ParagraphStyle('CN_Title', fontName=FONT, fontSize=24, leading=32,
                              textColor=BLUE, alignment=1, spaceAfter=4)
style_subtitle = ParagraphStyle('CN_Subtitle', fontName=FONT, fontSize=14, leading=20,
                                 textColor=DARK, alignment=1, spaceAfter=4)
style_meta = ParagraphStyle('CN_Meta', fontName=FONT, fontSize=10, leading=14,
                              textColor=GRAY, alignment=1, spaceAfter=16)
style_warn = ParagraphStyle('CN_Warn', parent=style_normal, textColor=RED)
style_small = ParagraphStyle('CN_Small', fontName=FONT, fontSize=9, leading=13,
                               textColor=GRAY, alignment=1)
style_tcell = ParagraphStyle('CN_TCell', fontName=FONT, fontSize=9, leading=13,
                               textColor=DARK)
style_theader = ParagraphStyle('CN_THeader', fontName=FONT, fontSize=9, leading=13,
                                textColor=white)

def B(text):
    """Bold text inline."""
    return f'<b>{text}</b>'

def make_table(headers, rows, col_widths=None):
    """Create a styled table."""
    data = [[Paragraph(h, style_theader) for h in headers]]
    for row in rows:
        data.append([Paragraph(str(c), style_tcell) for c in row])

    if col_widths:
        t = Table(data, colWidths=col_widths, repeatRows=1)
    else:
        t = Table(data, repeatRows=1)

    style_cmds = [
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEADER_BG),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('FONTNAME', (0, 0), (-1, -1), FONT),
        ('FONTSIZE', (0, 0), (-1, -1), 9),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, TABLE_BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]
    # Alternate row shading
    for i in range(1, len(data)):
        if i % 2 == 0:
            style_cmds.append(('BACKGROUND', (0, i), (-1, i), TABLE_ALT_BG))

    t.setStyle(TableStyle(style_cmds))
    return t

def build():
    pdf_path = os.path.join(OUT_DIR, "使用說明書.pdf")
    doc = SimpleDocTemplate(pdf_path, pagesize=A4,
                            leftMargin=2*cm, rightMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    story = []
    W = doc.width  # available width

    # ─── Title Page ───
    story.append(Spacer(1, 3*cm))
    story.append(Paragraph("薪資計算機 &amp; 錢錢管家", style_title))
    story.append(Paragraph("使用說明書", style_subtitle))
    story.append(Spacer(1, 8))
    story.append(Paragraph("版本：v2.0 / v3.0　更新日期：2026-04-13", style_meta))
    story.append(HRFlowable(width="80%", thickness=1, color=TABLE_BORDER, spaceAfter=16, spaceBefore=8))

    # ─── 一、概述 ───
    story.append(Paragraph("一、概述", style_h1))
    story.append(Paragraph("本專案包含兩個互相串接的行動網頁應用程式：", style_normal))
    story.append(make_table(
        ["應用程式", "檔案", "用途"],
        [["薪資計算機 v2", "薪資計算機v2.html", "打工、家教薪資紀錄與計算"],
         ["錢錢管家 v3", "錢錢管家v3.html", "日常收支記帳與預算管理"]],
        col_widths=[W*0.25, W*0.35, W*0.4]
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph("兩者皆為單一 HTML 檔案，無需安裝，使用瀏覽器直接開啟即可。資料儲存在瀏覽器的 localStorage 中。", style_normal))

    story.append(Paragraph("舊版檔案（保留用）", style_h3))
    story.append(make_table(
        ["檔案", "說明"],
        [["薪資計算機.html", "v1 原版（SVG 風格、底部導航）"],
         ["錢錢管家v2.html", "v2 原版（僅 CSV + JSON 匯出）"]],
        col_widths=[W*0.4, W*0.6]
    ))

    # ─── 二、快速開始 ───
    story.append(Paragraph("二、快速開始", style_h1))
    story.append(Paragraph("1. 開啟方式", style_h2))
    story.append(Paragraph("直接在瀏覽器中開啟 HTML 檔案即可使用。", style_normal))
    story.append(Paragraph(f"{B('重要：')}若要使用兩個程式之間的「同步」功能，必須從相同來源開啟兩個檔案（例如同一個資料夾用 file:/// 協議開啟，或透過同一個本地伺服器）。", style_warn))

    story.append(Paragraph("2. 手機使用", style_h2))
    story.append(Paragraph("兩個程式皆為行動裝置最佳化設計（480px 寬度），支援 iOS Safari「加入主畫面」、深色/淺色模式自動同步、安全區域適配（瀏海手機）。", style_normal))

    # ─── 三、薪資計算機 ───
    story.append(Paragraph("三、薪資計算機 v2 功能說明", style_h1))
    story.append(Paragraph("導航列", style_h2))
    story.append(make_table(
        ["頁籤", "功能"],
        [["📊 總覽", "月度收入摘要、圖表、目標進度"],
         ["✏️ 記帳", "新增薪資紀錄"],
         ["📋 明細", "瀏覽、搜尋、刪除紀錄"],
         ["💼 工作", "管理工作類型"],
         ["⚙️ 設定", "主題、目標薪資、同步、匯出"]],
        col_widths=[W*0.25, W*0.75]
    ))

    story.append(Paragraph("3.1 工作管理（💼 工作）", style_h2))
    story.append(Paragraph("使用前需先建立工作類型。前往「工作」頁籤，填入名稱、選擇計費方式、設定費率與顏色。", style_normal))
    story.append(make_table(
        ["計費方式", "說明"],
        [["時薪", "按工作時數計算（扣除休息時間）"],
         ["堂薪", "按上課堂數計算"],
         ["日薪", "按天計算固定金額"]],
        col_widths=[W*0.2, W*0.8]
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("可隨時編輯、停用或刪除工作。停用後不會出現在記帳選擇中。", style_normal))

    story.append(Paragraph("3.2 記帳（✏️ 記帳）", style_h2))
    story.append(Paragraph("選擇工作 → 選擇日期 → 填入對應資訊 → 點擊「✅ 新增」。預計薪資會即時顯示。", style_normal))
    story.append(Paragraph(f"{B('薪資計算邏輯：')}", style_normal))
    story.append(make_table(
        ["計費方式", "計算公式"],
        [["時薪", "(工作時長 - 休息時間) ÷ 60 × 時薪費率"],
         ["堂薪", "堂數 × 堂薪費率"],
         ["日薪", "日薪費率（固定）"]],
        col_widths=[W*0.2, W*0.8]
    ))
    story.append(Spacer(1, 4))
    story.append(Paragraph("時薪模式下可設定休息時間：0 / 30 / 60 / 90 分鐘或自訂。", style_normal))

    story.append(Paragraph("3.3 總覽（📊 總覽）", style_h2))
    story.append(Paragraph("月度摘要卡片（總收入、工作天數、平均日薪）、目標進度條、收入分佈環形圖、每日收入長條圖、工作摘要列表。使用月份切換按鈕（◀ ▶）切換月份。", style_normal))

    story.append(Paragraph("3.4 明細（📋 明細）", style_h2))
    story.append(Paragraph("顯示當月所有紀錄，支援搜尋。已同步紀錄會顯示「已同步」標籤。刪除已同步紀錄時會提醒至錢錢管家手動移除。", style_normal))

    story.append(Paragraph("3.5 設定（⚙️ 設定）", style_h2))
    story.append(Paragraph("主題模式（深色/淺色，與錢錢管家同步）、每月目標薪資、同步設定（詳見第五章）、匯出/匯入功能。", style_normal))

    # ─── 四、錢錢管家 ───
    story.append(Paragraph("四、錢錢管家 v3 功能說明", style_h1))
    story.append(Paragraph("導航列", style_h2))
    story.append(make_table(
        ["頁籤", "功能"],
        [["📊 總覽", "月度收支摘要、圖表"],
         ["✏️ 記帳", "新增收入/支出"],
         ["📋 明細", "瀏覽、搜尋、刪除紀錄"],
         ["🎯 目標", "儲蓄目標、固定支出"],
         ["⚙️ 設定", "主題、預算、類別、匯出"]],
        col_widths=[W*0.25, W*0.75]
    ))

    story.append(Paragraph("4.1 記帳", style_h2))
    story.append(Paragraph("選擇類型（支出/收入）→ 輸入金額 → 選擇帳戶（現金/銀行/信用卡）→ 選擇類別（僅支出）→ 日期 → 備註 → 新增。", style_normal))
    story.append(Paragraph("預設類別：飲食、交通、購物、娛樂、帳單、醫療、教育、其他（可在設定中自訂新增）。", style_normal))

    story.append(Paragraph("4.2 總覽", style_h2))
    story.append(Paragraph("收支摘要（支出/收入/結餘）、上月比較、預算進度、支出分佈環形圖（含上月比較）、每日支出長條圖、帳戶分佈、近期固定支出提醒。", style_normal))

    story.append(Paragraph("4.3 明細", style_h2))
    story.append(Paragraph("月度紀錄列表，支援搜尋。來自薪資計算機同步的紀錄會顯示「薪資計算機」標籤。", style_normal))

    story.append(Paragraph("4.4 目標", style_h2))
    story.append(Paragraph(f"{B('儲蓄目標：')}建立目標（名稱 + 目標金額），可隨時存入/取出，顯示進度條。達標時顯示 🎉。", style_normal))
    story.append(Paragraph(f"{B('固定支出：')}建立固定支出（名稱、金額、每月幾號），支援快速記帳，到期前 3 天自動提醒。", style_normal))

    story.append(Paragraph("4.5 設定", style_h2))
    story.append(Paragraph("主題模式、每月預算上限、自訂類別（圖示+顏色）、帳戶管理、資料管理（6 種格式匯出/匯入/清除）。", style_normal))

    # ─── 五、同步機制 ───
    story.append(Paragraph("五、同步機制", style_h1))
    story.append(Paragraph(f"{B('同步方向：薪資計算機 → 錢錢管家（單向）')}", style_normal))
    story.append(Paragraph("薪資計算機的紀錄可同步到錢錢管家作為「收入」紀錄。反向不支援。", style_normal))

    story.append(Paragraph("同步模式", style_h2))
    story.append(make_table(
        ["模式", "說明"],
        [["自動", "每次新增紀錄時自動同步"],
         ["手動", "手動點擊「同步」按鈕才同步"]],
        col_widths=[W*0.2, W*0.8]
    ))

    story.append(Paragraph("同步後的紀錄", style_h2))
    story.append(Paragraph("在錢錢管家的明細中，同步來的紀錄備註以 [薪資] 開頭，顯示「薪資計算機」標籤。帳戶預設為「銀行」，類別為「收入」。", style_normal))

    story.append(Paragraph("注意事項", style_h2))
    story.append(Paragraph("同步為單向，修改或刪除已同步的紀錄時，需至對應的程式手動處理。刪除已同步紀錄時，薪資計算機會彈出提醒。", style_warn))

    # ─── 六、匯出功能 ───
    story.append(Paragraph("六、匯出功能", style_h1))
    story.append(Paragraph("兩個程式皆支援 6 種匯出格式：", style_normal))
    story.append(make_table(
        ["格式", "副檔名", "說明"],
        [["JSON", ".json", "完整結構化資料，可用於備份還原"],
         ["CSV", ".csv", "Excel / Google Sheets 可開啟"],
         ["Markdown", ".md", "純文字表格，適合筆記軟體"],
         ["Excel", ".xlsx", "含紀錄 + 摘要雙工作表"],
         ["Word", ".docx", "排版好的表格文件"],
         ["PDF", ".pdf", "橫向排版，適合列印或分享"]],
        col_widths=[W*0.15, W*0.15, W*0.7]
    ))
    story.append(Spacer(1, 6))
    story.append(Paragraph(f"{B('薪資計算機額外功能：')}工作篩選（方便和家長報帳）、匯出錢錢管家 JSON 格式（異地備份）。", style_normal))

    # ─── 七、備份 ───
    story.append(Paragraph("七、資料備份與還原", style_h1))
    story.append(Paragraph(f"{B('匯出備份：')}前往「設定 → 資料管理」，選擇 JSON 格式匯出。", style_normal))
    story.append(Paragraph(f"{B('匯入還原：')}點擊「📥 匯入備份」，選擇 .json 檔案。資料會完全覆蓋現有資料。", style_normal))
    story.append(Paragraph(f"{B('清除資料：')}點擊「🗑️ 清除資料」。此操作不可還原，請先備份。", style_warn))

    # ─── 八、深色模式 ───
    story.append(Paragraph("八、深色/淺色模式", style_h1))
    story.append(Paragraph("兩個程式共用深色模式設定（儲存在 mm2-dark）。在任一程式中切換主題，另一個重新整理後即同步。預設為深色模式。", style_normal))

    # ─── 九、技術資訊 ───
    story.append(Paragraph("九、技術資訊", style_h1))
    story.append(Paragraph("資料儲存位置（localStorage keys）", style_h2))
    story.append(make_table(
        ["Key", "應用程式", "內容"],
        [["wc2-jobs", "薪資計算機", "工作類型"],
         ["wc2-records", "薪資計算機", "薪資紀錄"],
         ["wc2-settings", "薪資計算機", "設定"],
         ["mm2-tx", "錢錢管家", "交易紀錄"],
         ["mm2-budget", "錢錢管家", "預算"],
         ["mm2-cats", "錢錢管家", "類別"],
         ["mm2-accounts", "錢錢管家", "帳戶"],
         ["mm2-goals", "錢錢管家", "儲蓄目標"],
         ["mm2-fixed", "錢錢管家", "固定支出"],
         ["mm2-dark", "共用", "深色模式"]],
        col_widths=[W*0.3, W*0.3, W*0.4]
    ))

    story.append(Paragraph("使用的外部程式庫", style_h2))
    story.append(make_table(
        ["程式庫", "版本", "用途"],
        [["SheetJS (xlsx)", "0.20.3", "Excel 匯出"],
         ["jsPDF", "2.5.1", "PDF 匯出"],
         ["jspdf-autotable", "3.8.2", "PDF 表格"],
         ["docx", "8.5.0", "Word 匯出"]],
        col_widths=[W*0.35, W*0.2, W*0.45]
    ))

    # ─── 十、FAQ ───
    story.append(Paragraph("十、常見問題", style_h1))
    faqs = [
        ("Q: 兩個程式的資料不互通怎麼辦？", "A: 請確認兩個 HTML 檔案是從相同來源（同一資料夾）開啟的。不同來源的 localStorage 是隔離的。"),
        ("Q: 手機上資料會消失嗎？", "A: localStorage 在清除瀏覽器資料時會被刪除。建議定期使用 JSON 匯出功能備份。"),
        ("Q: 可以多裝置同步嗎？", "A: 目前不支援雲端同步。可透過匯出 JSON → 傳送到另一裝置 → 匯入的方式手動同步。"),
    ]
    for q, a in faqs:
        story.append(Paragraph(f"<b>{q}</b>", style_normal))
        story.append(Paragraph(a, style_normal))
        story.append(Spacer(1, 4))

    story.append(HRFlowable(width="100%", thickness=0.5, color=TABLE_BORDER, spaceAfter=8, spaceBefore=12))
    story.append(Paragraph("本說明書涵蓋薪資計算機 v2.0 與錢錢管家 v3.0 的所有功能。", style_small))

    doc.build(story)
    print(f"Created: {pdf_path}")

if __name__ == "__main__":
    build()
