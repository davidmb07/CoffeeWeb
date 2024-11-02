//redirigir btn editar_perfil
document.addEventListener("DOMContentLoaded", function() {
    const editarperfil = document.getElementById("editarperfil");
    editarperfil.addEventListener("click", function(event) {
        event.preventDefault();
        const url = editarperfil.getAttribute("data-url");
        window.location.href = url;
    });
});

// Función para copiar el enlace del perfil al portapapeles
function copiarEnlace(slug) {
    if (!slug) {
        console.error('El slug no está definido correctamente.');
        return;
    }
    var perfilURL = window.location.origin + '/perfil/' + slug + '/';
    navigator.clipboard.writeText(perfilURL).then(function() {
        alert('Enlace del perfil copiado al portapapeles!');
    }).catch(function(err) {
        console.error('Error al copiar el enlace: ', err);
    });
}

// Función para compartir en WhatsApp
function compartirWhatsApp(slug) {
    if (!slug) {
        console.error('El slug no está definido correctamente.');
        return;
    }
    var perfilURL = window.location.origin + '/perfil/' + slug + '/';
    var url = 'https://wa.me/?text=' + encodeURIComponent(perfilURL);
    window.open(url, '_blank');
}

// Función para compartir en Messenger
function compartirMessenger(slug) {
    if (!slug) {
        console.error('El slug no está definido correctamente.');
        return;
    }
    var perfilURL = window.location.origin + '/perfil/' + slug + '/';
    var url = 'fb-messenger://share/?link=' + encodeURIComponent(perfilURL);
    window.open(url, '_blank');
}