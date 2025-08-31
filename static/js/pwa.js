let deferredPrompt;
const installButton = document.getElementById('installButton');

window.addEventListener('beforeinstallprompt', (e) => {
    // Prevent Chrome 67 and earlier from automatically showing the prompt
    e.preventDefault();
    // Stash the event so it can be triggered later
    deferredPrompt = e;
    // Show the install button
    if (installButton) {
        installButton.style.display = 'block';
    }
});

if (installButton) {
    installButton.addEventListener('click', async () => {
        if (deferredPrompt) {
            // Show the install prompt
            deferredPrompt.prompt();
            // Wait for the user to respond to the prompt
            const { outcome } = await deferredPrompt.userChoice;
            console.log(`User response to the install prompt: ${outcome}`);
            // Clear the deferredPrompt variable
            deferredPrompt = null;
            // Hide the install button
            installButton.style.display = 'none';
        }
    });
}

// Check if the app is installed
window.addEventListener('appinstalled', (evt) => {
    console.log('App was installed');
    if (installButton) {
        installButton.style.display = 'none';
    }
});

// Service Worker Registration
if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/static/sw.js')
            .then((registration) => {
                console.log('ServiceWorker registration successful with scope: ', registration.scope);
            })
            .catch((err) => {
                console.log('ServiceWorker registration failed: ', err);
            });
    });
} 