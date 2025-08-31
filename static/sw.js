const CACHE_NAME = 'kivime-v1';
const urlsToCache = [
    '/',
    '/static/css/style.css',
    '/static/css/main-home.css',
    '/static/css/variables.css',
    '/static/js/main.js',
    '/static/js/main-home.js',
    '/static/logo.png',
    '/static/manifest.json',
    '/static/assets/vendor/bootstrap/css/bootstrap.min.css',
    '/static/assets/vendor/bootstrap-icons/bootstrap-icons.css',
    '/static/assets/vendor/boxicons/css/boxicons.min.css',
    '/static/assets/vendor/glightbox/css/glightbox.min.css',
    '/static/assets/vendor/swiper/swiper-bundle.min.css',
    '/login',
    '/signup',
    '/journal'
];

self.addEventListener('install', event => {
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then(cache => {
                console.log('Opened cache');
                return cache.addAll(urlsToCache);
            })
    );
});

self.addEventListener('fetch', event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                if (response) {
                    return response;
                }
                return fetch(event.request)
                    .then(response => {
                        if (!response || response.status !== 200 || response.type !== 'basic') {
                            return response;
                        }
                        const responseToCache = response.clone();
                        caches.open(CACHE_NAME)
                            .then(cache => {
                                cache.put(event.request, responseToCache);
                            });
                        return response;
                    });
            })
    );
}); 