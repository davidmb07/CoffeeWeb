//redirigir btn editar_perfil
document.addEventListener("DOMContentLoaded", function() {
    const editarperfil = document.getElementById("editarperfil");
    editarperfil.addEventListener("click", function(event) {
        event.preventDefault();
        const url = editarperfil.getAttribute("data-url");
        window.location.href = url;
    });
});