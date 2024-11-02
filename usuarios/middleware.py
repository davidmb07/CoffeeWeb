from django.shortcuts import redirect
from django.urls import reverse

class PreventBackToLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Si el usuario está autenticado y trata de acceder al login, registro o recuperar_cuenta,
        # redirigirlo a la página principal
        restricted_paths = [reverse('login'), reverse('registro'), reverse('recuperar_cuenta')]
        if request.user.is_authenticated and request.path in restricted_paths:
            return redirect('home')

        return response

class AdminCoffeeWebPermissionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Si el usuario es AdminCoffeeWeb, otorgar acceso completo
        if request.user.is_authenticated and hasattr(request.user, 'usuario') and request.user.usuario.tipo_usuario == 'AdminCoffeeWeb':
            request.user.is_superuser = True
            request.user.is_staff = True

        # Restringir acceso al panel de administración solo a AdminCoffeeWeb
        admin_path = reverse('admin:index')
        if request.path.startswith(admin_path):
            if not (request.user.is_authenticated and hasattr(request.user, 'usuario') and request.user.usuario.tipo_usuario == 'AdminCoffeeWeb'):
                return redirect('login')

        response = self.get_response(request)
        return response