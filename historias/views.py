from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def historias (request):
    return render(request, 'stories.html')