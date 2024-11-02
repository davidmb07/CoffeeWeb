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
    const togglePasswordIcons = document.querySelectorAll('.toggle-password-icon');

    togglePasswordIcons.forEach(icon => {
        icon.addEventListener('click', function() {
            const passwordField = icon.closest('.input-group').querySelector('input');

            if (passwordField.type === 'password') {
                passwordField.type = 'text';
                icon.classList.remove('fa-eye-slash');
                icon.classList.add('fa-eye');
            } else {
                passwordField.type = 'password';
                icon.classList.remove('fa-eye');
                icon.classList.add('fa-eye-slash');
            }
        });
    });
});

// Verificar coincidencia de contraseñas
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        const password = document.getElementById('inputPassword').value;
        const confirmPassword = document.getElementById('confirmPassword').value;
        const passwordMatchError = document.getElementById('passwordMatchError');

        if (password !== confirmPassword) {
            passwordMatchError.textContent = 'Las contraseñas no coinciden.';
            event.preventDefault(); // Evita que se envíe el formulario si las contraseñas no coinciden
        } else {
            passwordMatchError.textContent = ''; // Borra el mensaje de error si las contraseñas coinciden
        }
    });
});

//texto de largo de contraseña
document.getElementById('registro-form').addEventListener('submit', function(event) {
    var password = document.getElementById('inputPassword').value;
    var confirmPassword = document.getElementById('confirmPassword').value;
    var passwordMatchError = document.getElementById('passwordMatchError');

    if (password.length < 8 || password.length > 50) {
        passwordMatchError.textContent = 'La contraseña debe tener entre 8 y 50 caracteres.';
        event.preventDefault();
    } else if (password !== confirmPassword) {
        passwordMatchError.textContent = 'Las contraseñas no coinciden.';
        event.preventDefault();
    } else {
        passwordMatchError.textContent = '';
    }
});

//verificacion de marcacion de terminos y condiciones
document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registro-form'); // Asegúrate de que el formulario tenga este ID
    const checkbox = document.getElementById('flexSwitchCheckDefault');
    const submitButton = document.querySelector('.registrarse');

    submitButton.addEventListener('click', function(event) {
        if (!checkbox.checked) {
            event.preventDefault();
            alert('Debes aceptar el aviso de privacidad y los términos y condiciones.');
        } else {
            form.submit();
        }
    });
});

//cuadro de dialogo usuario registrado exitosamente
document.addEventListener('DOMContentLoaded', function() {
    var successRedirectUrl = document.getElementById('successRedirectUrl').value;
    var successMessage = document.getElementById('successMessage').value === 'true';

    function showSuccessDialog() {
        document.getElementById('overlay').style.display = 'block';
        document.getElementById('dialog').style.display = 'block';

        setTimeout(function() {
            window.location.href = successRedirectUrl;
        }, 3000); // 3 segundos
    }

    if (successMessage) {
        showSuccessDialog();
    }
});