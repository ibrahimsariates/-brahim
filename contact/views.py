from django.shortcuts import render
from .models import GeneralSetting


def index(request):
    # Veritabanındaki tüm ayarları çekiyoruz [cite: 710]
    all_settings = GeneralSetting.objects.all()

    # Verileri direkt isimleriyle kullanabilmek için sözlüğü açıyoruz
    context = {setting.name: setting.parameter for setting in all_settings}

    # Debug için terminale basalım (Hangi veriler geliyor gör)
    print(f"DEBUG - Sayfaya Giden Veriler: {context}")

    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
