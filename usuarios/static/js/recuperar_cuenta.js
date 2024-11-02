/* cambio de apariencia */
document.addEventListener("DOMContentLoaded", function() {
    // Función para aplicar el tema basado en la preferencia actual
    const applySystemTheme = () => {
        const htmlElement = document.documentElement;
        const prefersDarkScheme = window.matchMedia("(prefers-color-scheme: dark)").matches;
        htmlElement.setAttribute('data-theme', prefersDarkScheme ? 'dark' : 'light');
    };

    // Aplicar el tema basado en la preferencia inicial del sistema
    applySystemTheme();

    // Escuchar los cambios en la preferencia de color del sistema
    const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    darkModeMediaQuery.addEventListener('change', function(event) {
        applySystemTheme();
    });

    // Escuchar los cambios de tema externos (si es necesario)
    window.addEventListener("message", function(event) {
        if (event.data.type === "theme-change") {
            const theme = event.data.theme;
            const htmlElement = document.documentElement;
            htmlElement.setAttribute('data-theme', theme);
        }
    });
});

/* funcion btn cancelar */
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('btn_cancelar').addEventListener('click', function() {
        window.location.href = "/";
    });
});