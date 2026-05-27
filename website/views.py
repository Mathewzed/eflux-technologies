from django.shortcuts import render, redirect
from .models import Project, Contact, Settings

def home(request):
    projects = Project.objects.all().order_by('-created_at')
    settings_obj = Settings.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )
        return redirect('/')

    context = {
        'projects': projects,
        'settings': settings_obj
    }

    return render(request, 'website/index.html', context)