from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Usuario, AdministradorCooperativa, UsuarioCooperativa, Caficultor, ProveedorInsumos

# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar al usuario usando el email o el teléfono
        try:
            usuario = Usuario.objects.get(email=email)
        except Usuario.DoesNotExist:
            try:
                usuario = Usuario.objects.get(telefono=email)
            except Usuario.DoesNotExist:
                messages.error(request, "El usuario no existe.")
                return render(request, 'login')

        # Autenticar y verificar la contraseña
        user = authenticate(request, username=usuario.email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Contraseña incorrecta.")
            return render(request, 'login')
    else:
        return render(request, 'login.html')

def registro(request):
    if request.method == 'POST':
        tipo_usuario = request.POST.get('Tipo_usuario')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        contrasena = request.POST.get('password')
        confirmar_contrasena = request.POST.get('confirmPassword')

        # Validación de la contraseña
        if not contrasena or len(contrasena) < 8 or len(contrasena) > 50:
            messages.error(request, 'La contraseña debe tener entre 8 y 50 caracteres.')
            return redirect('registro')

        # Validación de que las contraseñas coinciden
        if contrasena != confirmar_contrasena:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('registro')

        # Verificación si el usuario ya existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'El usuario ya existe.')
            return redirect('registro')

        # Generar el ID personalizado
        usuario_id = Usuario.generate_custom_id()

        # Creación del usuario en la tabla de Django y en la tabla personalizada
        try:
            user = User.objects.create_user(username=email, email=email, password=contrasena)
            usuario = Usuario(
                id=usuario_id,
                user=user,
                nombre=nombre,
                apellido=apellido,
                email=email,
                telefono=telefono,
                tipo_usuario=tipo_usuario,
                contrasena=make_password(contrasena)  # Encriptar la contraseña
            )
            usuario.save()
            
            # Guardar el ID_Usuario en la tabla correspondiente según el tipo de usuario
            if tipo_usuario == 'AdminCooperativa':
                AdministradorCooperativa.objects.create(usuario=usuario)
            elif tipo_usuario == 'UserCooperativa':
                UsuarioCooperativa.objects.create(usuario=usuario)
            elif tipo_usuario == 'Caficultor':
                Caficultor.objects.create(usuario=usuario)
            elif tipo_usuario == 'Insumos':
                ProveedorInsumos.objects.create(usuario=usuario)

            messages.success(request, 'Cuenta creada exitosamente.')
            return redirect('registro')
        
        except Exception as e:
            messages.error(request, f'Error al crear la cuenta: {str(e)}')
            return redirect('registro')

    return render(request, 'registro.html')

def recuperar_cuenta(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        email = request.POST.get('recover_email')
        password = request.POST.get('password')

        if action == 'authenticate':
            try:
                usuario = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                messages.error(request, "El usuario no existe.")
                return render(request, 'recuperar_cuenta.html')

            user = authenticate(request, username=usuario.email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Contraseña incorrecta.")
                return render(request, 'recuperar_cuenta.html')

        elif action == 'recover':
            try:
                usuario = Usuario.objects.get(email=email)
            except Usuario.DoesNotExist:
                messages.error(request, "El usuario no existe.")
                return render(request, 'recuperar_cuenta.html')
            
            # Generar token para la recuperación de contraseña
            token = usuario_token_generator.make_token(usuario)
            uid = urlsafe_base64_encode(force_bytes(usuario.pk))
            link = request.build_absolute_uri(
                reverse('cambiar_clave', kwargs={'uidb64': uid, 'token': token})
            )
            
            # Enviar el correo electrónico
            subject = "Recuperación de contraseña - CoffeeWeb"
            message = render_to_string('emails/recover_password.html', {
                'user': usuario,
                'link': link,
            })
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [usuario.email])
            
            messages.success(request, "Se ha enviado un correo con las instrucciones para recuperar su contraseña.")
            return redirect('login')
    return render(request, 'recuperar_cuenta.html')

def cambiar_clave(request, uidb64, token):
    if request.method == 'POST':
        new_password = request.POST.get('newpassword')
        confirmar_new_password = request.POST.get('confirmar_newpassword')

        if new_password != confirmar_new_password:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'cambiar_clave.html')

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            usuario = Usuario.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, Usuario.DoesNotExist):
            usuario = None

        if usuario is not None and default_token_generator.check_token(usuario, token):
            usuario.contrasena = make_password(new_password)
            usuario.save()
            messages.success(request, "Contraseña actualizada con éxito.")
            return redirect('login')
        else:
            messages.error(request, "El enlace no es válido o ha expirado.")
            return render(request, 'cambiar_clave.html')
    else:
        return render(request, 'cambiar_clave.html')
    
class UsuarioTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)
        )

usuario_token_generator = UsuarioTokenGenerator()

@login_required
def mi_perfil(request):
    usuario = request.user.usuario
    return render(request, 'perfil.html', {'usuario': usuario})

@login_required
def perfil(request, enlace_perfil):
    usuario = get_object_or_404(Usuario, enlace_perfil=enlace_perfil)
    return render(request, 'perfil.html', {'usuario': usuario})

@login_required
def editar_perfil(request):
    usuario = request.user.usuario
    
    if request.method == 'POST':
        # Actualizar los campos del usuario
        usuario.nombre = request.POST.get('nombre')
        usuario.apellido = request.POST.get('apellido')
        usuario.telefono = request.POST.get('telefono')
        usuario.email = request.POST.get('email')
        usuario.descripcion = request.POST.get('descripcion')
        
        # Verificar si se está enviando una nueva foto de perfil
        if 'foto_perfil' in request.FILES:
            # Eliminar la foto de perfil anterior si existe
            if usuario.foto_perfil:
                usuario.foto_perfil.delete()
            
            # Guardar la nueva foto de perfil
            usuario.foto_perfil = request.FILES['foto_perfil']
        
        usuario.save()
        return redirect('mi_perfil')
    
    context = {
        'usuario': usuario,
    }
    
    return render(request, 'editar_perfil.html', context)

@login_required
def buscar_usuarios(request):
    query = request.GET.get('q')
    if query:
        # Filtrar usuarios por nombre, apellido o enlace de perfil que contengan el texto de búsqueda
        usuarios = Usuario.objects.filter(
            Q(nombre__icontains=query) |  # Busca por nombre
            Q(apellido__icontains=query)  # Busca por apellido
        )
    else:
        usuarios = Usuario.objects.none()

    return render(request, 'buscar_usuarios.html', {'usuarios': usuarios, 'query': query})

@login_required
def autocompletar_usuarios(request):
    query = request.GET.get('q')
    if query:
        # Filtrar usuarios por nombre o apellido que comiencen con el texto de búsqueda
        usuarios = User.objects.filter(
            Q(nombre__istartswith=query) | Q(apellido__istartswith=query)
        )[:5]  # Limitar los resultados a 5 usuarios para autocompletado
        usuarios_list = list(usuarios.values('id', 'nombre', 'apellido'))
    else:
        usuarios_list = []

    return JsonResponse(usuarios_list, safe=False)