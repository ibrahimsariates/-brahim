from django.contrib import admin
from django.urls import path, include
from django.conf import settings # Bu satırı kontrol et [cite: 194, 418, 655]
from django.conf.urls.static import static # Bu satırı kontrol et [cite: 195, 419, 656]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contact.urls')),
]

# BURASI ÇOK KRİTİK:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # [cite: 198, 422, 659]
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # [cite: 199, 423, 660]