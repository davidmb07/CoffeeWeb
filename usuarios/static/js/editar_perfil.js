document.addEventListener('DOMContentLoaded', function() {
    // Seleccionar el input de tipo file
    const inputFotoPerfil = document.getElementById('foto_perfil');
    // Seleccionar la imagen de previsualización
    const previewFotoPerfil = document.getElementById('previewFotoPerfil');

    // Escuchar cambios en el input de tipo file
    inputFotoPerfil.addEventListener('change', function() {
        const file = this.files[0]; // Obtener el archivo seleccionado

        if (file) {
            // Crear objeto URL para la imagen seleccionada
            const imgUrl = URL.createObjectURL(file);
            // Mostrar la imagen en el elemento de previsualización
            previewFotoPerfil.src = imgUrl;
        }
    });
});