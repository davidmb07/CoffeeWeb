// rellenar campo altitud
document.addEventListener('DOMContentLoaded', function() {
    // Obtener los elementos del DOM
    var terrenoSelect = document.getElementById('terrenoSelect');
    var altitudInput = document.getElementById('altitud');

    // Agregar evento para cuando se cambie el terreno seleccionado
    terrenoSelect.addEventListener('change', function() {
        // Obtener la opción seleccionada
        var selectedOption = this.options[this.selectedIndex];

        // Obtener la altitud de la opción seleccionada
        var altitud = selectedOption.getAttribute('data-altitud');

        // Asignar la altitud al campo de entrada
        altitudInput.value = altitud ? altitud : '';
    });
});

// Control deslizante para Humedad
const humedadRange = document.getElementById('humedad');
const humedadValor = document.getElementById('humedadValor');

humedadRange.addEventListener('input', function () {
    humedadValor.textContent = this.value;
});

// Control deslizante para Materia Orgánica
const materiaOrganicaRange = document.getElementById('materiaOrganica');
const materiaOrganicaValor = document.getElementById('materiaOrganicaValor');

materiaOrganicaRange.addEventListener('input', function () {
    materiaOrganicaValor.textContent = this.value;
});