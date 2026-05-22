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
    class Meta:
        verbose_name = "Genel Ayar"
        verbose_name_plural = "Genel Ayarlar"


# 2. Hero Bölümü (Ana Sayfa Banner)
class HeroSection(AbstractModel):
    name = models.CharField(max_length=100, verbose_name="İsim (Büyük başlık)")
    subtitle = models.CharField(max_length=200, verbose_name="Alt Başlık (h2)")
    typed_titles = models.CharField(
        max_length=500,
        verbose_name="Yazı Animasyonu Başlıkları",
        help_text="Virgülle ayırarak yazın. Örn: SAP Danışmanı, Full-Stack Developer"
    )
    description = models.TextField(verbose_name="Açıklama Metni")
    profile_image = models.ImageField(upload_to='hero/', verbose_name="Profil Fotoğrafı", blank=True, null=True)

    def __str__(self): return self.name
    class Meta:
        verbose_name = "Hero Bölümü"
        verbose_name_plural = "Hero Bölümü"


# 3. Hakkımda Bölümü
class AboutSection(AbstractModel):
    badge_text = models.CharField(max_length=100, verbose_name="Rozet Metni", default="Beni Tanıyın")
    title = models.CharField(max_length=300, verbose_name="Başlık")
    paragraph_1 = models.TextField(verbose_name="1. Paragraf")
    paragraph_2 = models.TextField(verbose_name="2. Paragraf", blank=True, default="")

    def __str__(self): return self.title[:50]
    class Meta:
        verbose_name = "Hakkımda Bölümü"
        verbose_name_plural = "Hakkımda Bölümü"


# 4. Eğitim Bilgileri
class Education(AbstractModel):
    title = models.CharField(max_length=200, verbose_name="Bölüm / Program")
    date_range = models.CharField(max_length=100, verbose_name="Tarih Aralığı")
    institution = models.CharField(max_length=200, verbose_name="Kurum / Üniversite")
    description = models.TextField(verbose_name="Açıklama", blank=True, default="")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    def __str__(self): return f"{self.title} - {self.institution}"
    class Meta:
        verbose_name = "Eğitim"
        verbose_name_plural = "Eğitimler"
        ordering = ['order']


# 5. Sertifikalar
class Certificate(AbstractModel):
    provider = models.CharField(max_length=200, verbose_name="Sağlayıcı (örn: Cisco)")
    name = models.CharField(max_length=200, verbose_name="Sertifika Adı")
    date = models.CharField(max_length=100, verbose_name="Tarih")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    def __str__(self): return f"{self.name} ({self.provider})"
    class Meta:
        verbose_name = "Sertifika"
        verbose_name_plural = "Sertifikalar"
        ordering = ['order']


# 6. İş Deneyimi
class Experience(AbstractModel):
    title = models.CharField(max_length=200, verbose_name="Pozisyon")
    date_range = models.CharField(max_length=100, verbose_name="Tarih Aralığı")
    company = models.CharField(max_length=200, verbose_name="Şirket")
    location = models.CharField(max_length=200, verbose_name="Konum", blank=True, default="")
    bullets = models.TextField(
        verbose_name="Maddeler",
        help_text="Her satır bir madde olarak gösterilecek."
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    def __str__(self): return f"{self.title} - {self.company}"

    def bullet_list(self):
        """Maddeleri liste olarak döndürür"""
        return [b.strip() for b in self.bullets.strip().split('\n') if b.strip()]

    class Meta:
        verbose_name = "İş Deneyimi"
        verbose_name_plural = "İş Deneyimleri"
        ordering = ['order']


# 7. Portfolyo Projeleri (genişletildi)
class Project(AbstractModel):
    title = models.CharField(max_length=200, verbose_name="Proje Başlığı")
    category = models.CharField(max_length=100, verbose_name="Kategori")
    description = models.TextField(verbose_name="Kısa Açıklama")
    tech_description = models.TextField(verbose_name="Teknik Detay", blank=True, default="")
    filter_tag = models.CharField(
        max_length=50,
        verbose_name="Filtre Etiketi",
        help_text="CSS sınıfı. Örn: filter-web, filter-sap",
        default="filter-web"
    )
    image = models.ImageField(upload_to='portfolio/', verbose_name="Görsel")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    def __str__(self): return self.title
    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projeler"
        ordering = ['order']


# 8. Sosyal Medya Linkleri (genişletildi)
class SocialLink(AbstractModel):
    platform = models.CharField(max_length=100, verbose_name="Platform (Github, LinkedIn)")
    url = models.URLField(verbose_name="Link")
    icon_class = models.CharField(
        max_length=100,
        verbose_name="İkon Sınıfı",
        help_text="Bootstrap Icons sınıfı. Örn: bi bi-github",
        default="bi bi-link"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    def __str__(self): return self.platform
    class Meta:
        verbose_name = "Sosyal Link"
        verbose_name_plural = "Sosyal Linkler"
        ordering = ['order']


# 9. İletişim Bilgileri
class ContactInfo(AbstractModel):
    icon_class = models.CharField(
        max_length=100,
        verbose_name="İkon Sınıfı",
        help_text="Bootstrap Icons sınıfı. Örn: bi bi-envelope",
        default="bi bi-info-circle"
    )
    label = models.CharField(max_length=100, verbose_name="Etiket (örn: Email Adresi)")
    value = models.CharField(max_length=254, verbose_name="Değer")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    def __str__(self): return f"{self.label}: {self.value}"
    class Meta:
        verbose_name = "İletişim Bilgisi"
        verbose_name_plural = "İletişim Bilgileri"
        ordering = ['order']