from django.shortcuts import render
from .models import GeneralSetting

def index(request):
    # Veritabanındaki tüm ayarları çekiyoruz
    all_settings = GeneralSetting.objects.all()

    # Verileri bir sözlük (dictionary) haline getiriyoruz
    # Bu sayede HTML'de {{ home_banner_name }} yazdığında Django bunu bulacak
    context = {setting.name: setting.parameter for setting in all_settings}

    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contact.html')