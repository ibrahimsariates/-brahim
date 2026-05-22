from django.shortcuts import render
from .models import (
    GeneralSetting, HeroSection, AboutSection,
    Education, Certificate, Experience,
    Project, SocialLink, ContactInfo
)


def index(request):
    hero = HeroSection.objects.first()
    about = AboutSection.objects.first()
    context = {
        'hero': hero,
        'about': about,
        'educations': Education.objects.all().order_by('order'),
        'certificates': Certificate.objects.all().order_by('order'),
        'experiences': Experience.objects.all().order_by('order'),
        'projects': Project.objects.all().order_by('order'),
        'social_links': SocialLink.objects.all().order_by('order'),
        'contact_infos': ContactInfo.objects.all().order_by('order'),
        'settings': {s.key: s.value for s in GeneralSetting.objects.all()},
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')