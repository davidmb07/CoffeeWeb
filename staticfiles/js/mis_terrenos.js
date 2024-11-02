//redirigir btn agregar a agregar terreno
document.addEventListener("DOMContentLoaded", function() {
    const agregarButton = document.getElementById("agregarButton");
    agregarButton.addEventListener("click", function() {
        const url = agregarButton.getAttribute("data-url");
        window.location.href = url;
    });
});

//redirigir editar terreno
document.addEventListener("DOMContentLoaded", function() {
    const editarButton = document.getElementById("editarButton");
    editarButton.addEventListener("click", function() {
        const url = editarButton.getAttribute("data-url");
        window.location.href = url;
    });
});

// eliminar terreno
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.eliminar').forEach(button => {
        button.addEventListener('click', function() {
            const url = this.getAttribute('data-url');
            if (confirm('¿Estás seguro de que quieres eliminar este terreno?')) {
                fetch(url, {
                    method: 'DELETE',
                    headers: {
                        'X-CSRFToken': getCookie('csrftoken'),
                    },
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        location.reload(); // Recarga la página para actualizar la lista de terrenos
                    } else {
                        alert('Error al eliminar el terreno.');
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert('Error al eliminar el terreno.');
                });
            }
        });
    });
});

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}