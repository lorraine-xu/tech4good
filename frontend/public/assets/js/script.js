document.addEventListener('DOMContentLoaded', () => {
    console.log('Website loaded!');
    // Future interactive scripts can go here.

    new Vue({
        el: '#app',
        data: {
            items: [
                { src: 'assets/images/earth-globe.png', alt: 'Smiling Earth', width: '300' },
                null,
                null,
                null,
                null,
                null
            ]
        }
    });
});
