// porcentaje sombra
document.addEventListener('DOMContentLoaded', function() {
    const range = document.getElementById('porcentaje');
    const porcentajeValor = document.getElementById('porcentajeValor');

    range.addEventListener('input', function() {
        porcentajeValor.textContent = this.value;
    });
});

// rellenar campo altitud
document.addEventListener('DOMContentLoaded', function() {
    var terrenoSelect = document.getElementById('terrenoSelect');
    var altitudInput = document.getElementById('altitud');

    terrenoSelect.addEventListener('change', function() {
        var selectedOption = this.options[this.selectedIndex];
        var altitud = selectedOption.getAttribute('data-altitud');
        altitudInput.value = altitud;
    });
});