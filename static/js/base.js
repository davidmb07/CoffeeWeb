document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM completamente cargado y analizado');

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

    const currentTheme = localStorage.getItem('theme') || 'system';
    applyTheme(currentTheme);

    const systemThemeChangeListener = (event) => {
        if (localStorage.getItem('theme') === 'system') {
            applyTheme(event.matches ? 'dark' : 'light');
        }
    };

    const darkModeMediaQuery = window.matchMedia("(prefers-color-scheme: dark)");
    darkModeMediaQuery.addEventListener('change', systemThemeChangeListener);

    // Función para enviar evento de cambio de tema
    const enviarEventoCambioTema = (theme) => {
        document.dispatchEvent(new CustomEvent('theme-change', { detail: { theme: theme } }));
    };

    const modoClaroButton = document.getElementById('modo-claro');
    const modoOscuroButton = document.getElementById('modo-oscuro');
    const modoAutoButton = document.getElementById('modo-auto');

    const handleClick = (theme) => {
        localStorage.setItem('theme', theme);
        applyTheme(theme);
        enviarEventoCambioTema(theme); // Envía el evento de cambio de tema
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

//buscador
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchResults = document.getElementById('searchResults');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value.trim();

        if (query.length > 0) {
            fetch(`/autocompletar-usuarios/?q=${query}`)
                .then(response => response.json())
                .then(data => {
                    searchResults.innerHTML = '';  // Limpiar resultados anteriores
                    data.forEach(usuario => {
                        const fullName = `${usuario.first_name} ${usuario.last_name}`;
                        const link = `<a href="{% url 'perfil' usuario.id %}">${fullName}</a>`;
                        const resultItem = `<div>${link}</div>`;
                        searchResults.innerHTML += resultItem;
                    });
                });
        } else {
            searchResults.innerHTML = '';  // Limpiar resultados si el campo está vacío
        }
    });
});