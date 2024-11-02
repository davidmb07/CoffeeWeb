//redirigir btn cancelar a terrenos
document.addEventListener("DOMContentLoaded", function() {
    const cancelarButton = document.getElementById("cancelarButton");
    cancelarButton.addEventListener("click", function(event) {
        event.preventDefault();
        const url = cancelarButton.getAttribute("data-url");
        window.location.href = url;
    });
});