// 薪資計算機 + 錢錢管家 — 離線快取
// 第一次連網開啟後，所有 HTML 與外部程式庫會被快取，之後可離線使用

const CACHE_NAME = 'fm-cache-v1';

// 預先快取的核心資源
const CORE_ASSETS = [
  './',
  './薪資計算機v1.html',
  './薪資計算機v2.html',
  './錢錢管家v2.html',
  './錢錢管家v3.html',
  './manifest.json',
  // 外部程式庫（匯出功能用）
  'https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js',
  'https://cdn.jsdelivr.net/npm/docx@8.5.0/build/index.umd.min.js',
];

// 安裝：預先快取所有核心資源
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => cache.addAll(CORE_ASSETS).catch(err => {
        // 即使部分外部資源失敗（網路問題）也不影響本地檔案快取
        console.warn('[SW] partial cache failed:', err);
      }))
      .then(() => self.skipWaiting())
  );
});

// 啟用：清掉舊版快取
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// 攔截請求：cache-first 策略（離線優先）
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  // 跳過 chrome-extension / 非 http(s) 請求
  if (!event.request.url.startsWith('http')) return;

  event.respondWith(
    caches.match(event.request).then(cached => {
      if (cached) return cached;
      // 沒快取就抓網路，順便存起來
      return fetch(event.request).then(response => {
        // 只快取成功且非錯誤的回應
        if (response && response.status === 200 && response.type !== 'opaque') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(cache => cache.put(event.request, clone));
        }
        return response;
      }).catch(() => {
        // 完全離線且無快取：fallback 到首頁
        if (event.request.mode === 'navigate') {
          return caches.match('./錢錢管家v3.html');
        }
      });
    })
  );
});
