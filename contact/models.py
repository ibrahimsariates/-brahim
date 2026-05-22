from django.db import models

class AbstractModel(models.Model):
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True

# 1. Genel Ayarlar (Mail, Konum, Telefon vb.)
class GeneralSetting(AbstractModel):
    key = models.CharField(max_length=100, verbose_name="Ayar Anahtarı (örn: Email)")
    value = models.CharField(max_length=254, verbose_name="Ayar Değeri")
    def __str__(self): return f"{self.key}: {self.value}"

# 2. Projeler (Görseldeki Proje Kartları)
class Project(AbstractModel):
    title = models.CharField(max_length=200, verbose_name="Proje Başlığı")
    category = models.CharField(max_length=100, verbose_name="Kategori")
    description = models.TextField(verbose_name="Açıklama")
    image = models.ImageField(upload_to='portfolio/', verbose_name="Görsel")
    def __str__(self): return self.title

# 3. Özgeçmiş (Deneyim ve Eğitim)
class Resume(AbstractModel):
    title = models.CharField(max_length=200, verbose_name="Başlık (örn: Junior SAP Consultant)")
    date = models.CharField(max_length=100, verbose_name="Tarih Aralığı")
    content = models.TextField(verbose_name="Açıklama/Detay")
    def __str__(self): return self.title

# 4. Sosyal Linkler
class SocialLink(AbstractModel):
    platform = models.CharField(max_length=100, verbose_name="Platform (Github, LinkedIn)")
    url = models.URLField(verbose_name="Link")
    def __str__(self): return self.platform