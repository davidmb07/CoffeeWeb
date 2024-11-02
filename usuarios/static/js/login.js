/* cambio de apariencia */
document.addEventListener('DOMContentLoaded', function() {
    const applyTheme = (theme) => {
        const htmlElement = document.documentElement;
        if (theme === 'dark') {
            htmlElement.setAttribute('data-theme', 'dark');
            htmlElement.classList.remove('light-mode');
            htmlElement.classList.add('dark-mode');
        } else if (theme === 'light') {
            htmlElement.setAttribute('data-theme', 'light');
            htmlElement.classList.remove('dark-mode');
            htmlElement.classList.add('light-mode');
        } else {
            const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
            applyTheme(prefersDarkScheme ? 'dark' : 'light');
        }
    };

    const updateGoogleButton = () => {
        const theme = localStorage.getItem('theme') || 'system';
        const googleButton = document.querySelector('.btn-google');
        if (googleButton) {
            if (theme === 'dark' || (theme === 'system' && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
                googleButton.classList.remove('btn-outline-dark');
                googleButton.classList.add('btn-outline-light');
            } else {
                googleButton.classList.remove('btn-outline-light');
                googleButton.classList.add('btn-outline-dark');
            }
        }
    };

    const currentTheme = localStorage.getItem('theme') || 'system';
    applyTheme(currentTheme);
    updateGoogleButton();

    const systemThemeChangeListener = (event) => {
        if (localStorage.getItem('theme') === 'system') {
            applyTheme(event.matches ? 'dark' : 'light');
            updateGoogleButton();
        }
    };

    const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    darkModeMediaQuery.addEventListener('change', systemThemeChangeListener);

    const modoClaroButton = document.getElementById('modo-claro');
    const modoOscuroButton = document.getElementById('modo-oscuro');
    const modoAutoButton = document.getElementById('modo-auto');

    const handleClick = (theme) => {
        localStorage.setItem('theme', theme);
        applyTheme(theme);
        updateGoogleButton();
    };

    if (modoClaroButton) {
        modoClaroButton.addEventListener('click', function(e) {
            e.preventDefault();
            handleClick('light');
        });
    }

    if (modoOscuroButton) {
        modoOscuroButton.addEventListener('click', function(e) {
            e.preventDefault();
            handleClick('dark');
        });
    }

    if (modoAutoButton) {
        modoAutoButton.addEventListener('click', function(e) {
            e.preventDefault();
            handleClick('system');
            systemThemeChangeListener(darkModeMediaQuery);
        });
    }
});

/* ver contraseña */
document.addEventListener('DOMContentLoaded', function() {
    const togglePasswordIcon = document.querySelector('.toggle-password-icon');
    const passwordInput = document.getElementById('exampleInputPassword1');

    togglePasswordIcon.addEventListener('click', function() {
        const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
        passwordInput.setAttribute('type', type);

        // Cambia los iconos de Font Awesome
        if (type === 'password') {
            togglePasswordIcon.classList.remove('fa-eye');
            togglePasswordIcon.classList.add('fa-eye-slash');
        } else {
            togglePasswordIcon.classList.remove('fa-eye-slash');
            togglePasswordIcon.classList.add('fa-eye');
        }
    });
});

// comportamiento label e input
document.addEventListener('DOMContentLoaded', function () {
    const inputs = document.querySelectorAll('.user-box input');

    inputs.forEach(input => {
        input.addEventListener('input', function () {
            const label = this.nextElementSibling; // Obtener el label siguiente al input
            if (this.value.trim() !== '') {
                label.classList.add('active'); // Agregar clase cuando hay contenido
            } else {
                label.classList.remove('active'); // Quitar clase cuando no hay contenido
            }
        });
    });
});

// Activar el carrusel para que pase automáticamente cada 5 segundos
document.addEventListener('DOMContentLoaded', function() {
    var myCarousel = document.getElementById('carouselExampleCaptions');
    var carousel = new bootstrap.Carousel(myCarousel, {
        interval: 5000, // Cambiar a 5000 para 5 segundos
        wrap: true
    });
});