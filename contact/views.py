from django.shortcuts import render
from .models import GeneralSetting, Project, Resume, SocialLink

def index(request):
    # Tüm verileri veritabanından çek
    context = {
        'settings': {s.key: s.value for s in GeneralSetting.objects.all()},
        'projects': Project.objects.all(),
        'resumes': Resume.objects.all(),
        'social_links': SocialLink.objects.all(),
    }
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')