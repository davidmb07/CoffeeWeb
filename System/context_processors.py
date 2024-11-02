from usuarios.models import Usuario

def tipo_usuario(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(user=request.user)
            return {'tipo_usuario': usuario.tipo_usuario}
        except Usuario.DoesNotExist:
            return {}
    return {}

def user_info(request):
    if request.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(user=request.user)
            tipo_usuario = usuario.tipo_usuario
            tipo_usuario_verbose = get_tipo_usuario_verbose(tipo_usuario)
            icono_tipo_usuario = get_icono_tipo_usuario(tipo_usuario)
            
            return {
                'user_full_name': f'{usuario.nombre} {usuario.apellido}',
                'tipo_user': tipo_usuario_verbose,
                'icono_tipo_user': icono_tipo_usuario,
            }
        except Usuario.DoesNotExist:
            return {}
    return {}

def get_tipo_usuario_verbose(tipo_usuario):
    tipos_verbose = {
        'Caficultor': 'Caficultor',
        'UserCooperativa': 'Usuario de Cooperativa',
        'AdminCooperativa': 'Administrador de Cooperativa',
        'Insumos': 'Proveedor de Insumos',
        'AdminCoffeeWeb': 'Administrador de CoffeeWeb',
    }
    return tipos_verbose.get(tipo_usuario, tipo_usuario)

def get_icono_tipo_usuario(tipo_usuario):
    iconos = {
        'Caficultor': 'fa-solid fa-seedling',
        'UserCooperativa': 'fa-solid fa-users',
        'AdminCooperativa': 'fa-solid fa-user-tie',
        'Insumos': 'fa-solid fa-toolbox',
        'AdminCoffeeWeb': 'fa-solid fa-laptop-code',
    }
    return iconos.get(tipo_usuario, 'fa-solid fa-user')