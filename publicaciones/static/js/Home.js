// En tu archivo Home.js (o un script separado)
$(document).ready(function() {
    // Simulación de datos de publicaciones (puedes reemplazarlo con datos dinámicos desde Django)
    const publicaciones = [
        {
            id: 1,
            usuario: {
                nombre: "Usuario 1",
                fotoPerfil: "{% static 'ruta/a/foto1.jpg' %}", // Asegúrate de tener esta imagen en tu proyecto
            },
            fecha: new Date("2024-06-20T12:00:00Z"),
            contenido: {
                tipo: "texto",
                texto: "Este es un ejemplo de publicación con solo texto.",
                imagen: null,
                video: null,
            },
            comentarios: [],
            likes: 0,
        },
        // Agrega más objetos de publicaciones según sea necesario
    ];

    // Función para cargar las publicaciones
    function cargarPublicaciones() {
        const $publicacionesContainer = $(".publicaciones");

        // Limpiar container antes de cargar nuevas publicaciones
        $publicacionesContainer.empty();

        // Iterar sobre el array de publicaciones y crear elementos HTML dinámicamente
        publicaciones.forEach((publicacion) => {
            const $publicacionElement = $("<div>").addClass("publicacion").attr("data-publicacion-id", publicacion.id);

            // Encabezado de la publicación (foto de perfil, nombre de usuario y fecha)
            const $encabezado = $("<div>").addClass("encabezado");
            $encabezado.append($("<img>").attr("src", publicacion.usuario.fotoPerfil).addClass("foto-perfil"));
            $encabezado.append($("<span>").text(publicacion.usuario.nombre).addClass("nombre-usuario"));
            $encabezado.append($("<span>").text(calcularTiempoPublicacion(publicacion.fecha)).addClass("tiempo-publicacion"));
            $publicacionElement.append($encabezado);

            // Contenido de la publicación (texto, imagen o video)
            const $contenido = $("<div>").addClass("contenido");
            if (publicacion.contenido.tipo === "texto") {
                $contenido.append($("<p>").text(publicacion.contenido.texto));
            } else if (publicacion.contenido.tipo === "imagen") {
                $contenido.append($("<img>").attr("src", publicacion.contenido.imagen).addClass("imagen-publicacion"));
            } else if (publicacion.contenido.tipo === "video") {
                $contenido.append($("<video>").attr("src", publicacion.contenido.video).addClass("video-publicacion"));
            }
            $publicacionElement.append($contenido);

            // Sección de interacción (comentarios, likes, compartir)
            const $interaccion = $("<div>").addClass("interaccion");
            $interaccion.append($("<button>").text("Comentar").addClass("btn-comentar"));
            $interaccion.append($("<button>").text("Like").addClass("btn-like"));
            $interaccion.append($("<button>").text("Compartir").addClass("btn-compartir"));
            $interaccion.append($("<span>").text(`${publicacion.likes} Likes`).addClass("contador-likes"));
            $publicacionElement.append($interaccion);

            // Agregar la publicación al contenedor principal
            $publicacionesContainer.append($publicacionElement);
        });
    }

    // Función para calcular el tiempo desde la publicación
    function calcularTiempoPublicacion(fechaPublicacion) {
        const ahora = new Date();
        const diferenciaMs = ahora - fechaPublicacion;
        const segundos = Math.round(diferenciaMs / 1000);
        if (segundos < 60) {
            return `Hace ${segundos} segundos`;
        }
        const minutos = Math.round(segundos / 60);
        if (minutos < 60) {
            return `Hace ${minutos} minutos`;
        }
        const horas = Math.round(minutos / 60);
        if (horas < 24) {
            return `Hace ${horas} horas`;
        }
        const dias = Math.round(horas / 24);
        return `Hace ${dias} días`;
    }

    // Cargar las publicaciones al cargar la página
    cargarPublicaciones();
});