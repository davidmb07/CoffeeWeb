document.getElementById('scroll-left').addEventListener('click', function() {
    document.querySelector('.stories-container').scrollBy({
        left: -200,
        behavior: 'smooth'
    });
});

document.getElementById('scroll-right').addEventListener('click', function() {
    document.querySelector('.stories-container').scrollBy({
        left: 200,
        behavior: 'smooth'
    });
});