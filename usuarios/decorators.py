from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from functools import wraps

def admin_coffeeweb_or_permission(permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.is_authenticated and request.user.usuario.tipo_usuario == 'AdminCoffeeWeb':
                return view_func(request, *args, **kwargs)
            if request.user.has_perm(permission):
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
        return _wrapped_view
    return decorator
