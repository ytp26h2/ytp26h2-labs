const CACHE = "ytp-vocabuddy-v1";     // 改版時把 v1 改成 v2，舊快取才會換新
const SHELL = ["./", "index.html", "words.js", "srs.js", "manifest.json"];

self.addEventListener("install", e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)));   // 安裝時先存一份
});

self.addEventListener("fetch", e => {
  e.respondWith(
    caches.match(e.request).then(hit => hit || fetch(e.request)) // 先問快取，沒有才上網
  );
});
