// 薪資計算機 + 錢錢管家 — 離線快取（v2）
// HTML/manifest：network-first（永遠用最新版）
// CDN 程式庫：cache-first（不會變動，加速載入）

const CACHE_NAME = 'fm-cache-v2';

// 預先快取的核心資源
const CORE_ASSETS = [
  './',
  './index.html',
  './薪資計算機v1.html',
  './薪資計算機v2.html',
  './錢錢管家v2.html',
  './錢錢管家v3.html',
  './manifest.json',
];

// CDN 資源（cache-first，永遠用快取）
const CDN_ASSETS = [
  'https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js',
  'https://cdn.jsdelivr.net/npm/docx@8.5.0/build/index.umd.min.js',
];

// 安裝：預先快取所有資源 + 立即接管
self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(cache => Promise.all([
        cache.addAll(CORE_ASSETS).catch(err => console.warn('[SW] core cache fail:', err)),
        cache.addAll(CDN_ASSETS).catch(err => console.warn('[SW] cdn cache fail:', err)),
      ]))
      .then(() => self.skipWaiting())
  );
});

// 啟用：清掉舊版快取（包括 fm-cache-v1）+ 立即接管所有分頁
self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => k !== CACHE_NAME).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

// 判斷是否為 CDN 資源（cache-first 適用）
function isCDN(url) {
  return url.startsWith('https://cdn.') ||
         url.startsWith('https://cdnjs.') ||
         url.startsWith('https://fonts.');
}

// 攔截請求
self.addEventListener('fetch', event => {
  if (event.request.method !== 'GET') return;
  if (!event.request.url.startsWith('http')) return;

  const url = event.request.url;

  // CDN 資源：cache-first（程式庫永遠不變，先用快取）
  if (isCDN(url)) {
    event.respondWith(
      caches.match(event.request).then(cached => {
        if (cached) return cached;
        return fetch(event.request).then(response => {
          if (response && response.status === 200) {
            const clone = response.clone();
            caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
          }
          return response;
        });
      })
    );
    return;
  }

  // HTML / manifest / 其他本地資源：network-first
  // 先抓網路（拿最新），失敗才用快取（離線備援）
  event.respondWith(
    fetch(event.request)
      .then(response => {
        // 抓到最新版就更新快取，下次離線也能用
        if (response && response.status === 200 && response.type === 'basic') {
          const clone = response.clone();
          caches.open(CACHE_NAME).then(c => c.put(event.request, clone));
        }
        return response;
      })
      .catch(() => {
        // 沒網路：用快取
        return caches.match(event.request).then(cached => {
          if (cached) return cached;
          // 連快取都沒：fallback 到首頁
          if (event.request.mode === 'navigate') {
            return caches.match('./index.html');
          }
        });
      })
  );
});
