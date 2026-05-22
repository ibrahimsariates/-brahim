from django.db import migrations


def seed_data(apps, schema_editor):
    """Mevcut hardcoded içerikleri veritabanına yükler."""

    HeroSection = apps.get_model('contact', 'HeroSection')
    AboutSection = apps.get_model('contact', 'AboutSection')
    Education = apps.get_model('contact', 'Education')
    Certificate = apps.get_model('contact', 'Certificate')
    Experience = apps.get_model('contact', 'Experience')
    Project = apps.get_model('contact', 'Project')
    SocialLink = apps.get_model('contact', 'SocialLink')
    ContactInfo = apps.get_model('contact', 'ContactInfo')

    # --- Hero ---
    HeroSection.objects.get_or_create(
        name='İbrahim',
        defaults={
            'subtitle': 'İbrahim Metehan Sarıateş',
            'typed_titles': 'SAP Danışmanı, Full-Stack Developer, Bulut Mimarı',
            'description': '',
        }
    )

    # --- Hakkımda ---
    AboutSection.objects.get_or_create(
        badge_text='Beni Tanıyın',
        defaults={
            'title': 'Sistem Mimarisi ve Global Çözümler Konusunda Tutkulu Genç Bir Mühendis',
            'paragraph_1': 'Piri Reis Üniversitesi Bilişim Sistemleri Mühendisliği öğrencisiyim ve eş zamanlı olarak CBS Corporate Business Solutions\'da SAP Danışmanı olarak görev alıyorum. Karmaşık sistem mimarileri ile pratik yazılım çözümleri arasında köprü kurmaktan büyük keyif alıyorum.',
            'paragraph_2': '30\'dan fazla ülkede global e-fatura uyumluluğu sağlıyor, AWS üzerinde yüksek trafikli bulut mimarileri tasarlıyor ve Node.js ile full-stack web platformları (Gurmeo_O) geliştiriyorum. Hem akademik hem de profesyonel hayatta uluslararası ekiplerle çalışarak teknik yeteneklerimi her geçen gün daha da ileriye taşımaya ve yeni küresel fırsatları değerlendirmeye odaklanıyorum.',
        }
    )

    # --- Eğitim ---
    Education.objects.get_or_create(
        title='Bilişim Sistemleri Mühendisliği (Lisans)',
        defaults={
            'date_range': '2023 - 2027 (Beklenen Mezuniyet)',
            'institution': 'Piri Reis Üniversitesi, İstanbul',
            'description': 'Yazılım geliştirme, veritabanı yönetimi, algoritmalar ve sistem mimarisi üzerine aktif lisans eğitimi.',
            'order': 1,
        }
    )

    # --- Sertifikalar ---
    Certificate.objects.get_or_create(
        name='CSS Essentials',
        defaults={'provider': 'Cisco Networking Academy', 'date': 'Aralık 2025', 'order': 1}
    )
    Certificate.objects.get_or_create(
        name='HTML Essentials',
        defaults={'provider': 'Cisco Networking Academy', 'date': 'Aralık 2025', 'order': 2}
    )
    Certificate.objects.get_or_create(
        name='Introduction to Linux',
        defaults={'provider': 'Cisco Networking Academy', 'date': 'Kasım 2025', 'order': 3}
    )

    # --- Deneyim ---
    Experience.objects.get_or_create(
        title='SAP Danışmanı',
        defaults={
            'date_range': '07/2024 - Günümüz',
            'company': 'CBS Corporate Business Solutions',
            'location': 'İstanbul',
            'bullets': 'SAP sistemleri üzerinden 30\'dan fazla ülkede global e-fatura uyumluluğunu ve bulut tabanlı MCS entegrasyon süreçlerini yürütüyorum.\nJira üzerinden teknik destek biletlerini (ticket) yönetiyor, sorunların çözümü için kıdemli uzmanlara hızlı ve doğru yönlendirmeler yapıyorum.\nUluslararası teknik ekiplerle Microsoft Teams üzerinden doğrudan iletişim kurarak koordinasyon sağlıyorum.\nSistemlerin yüksek kullanılabilirliğini sürdürüyor, yasal düzenlemelere uygun kesintisiz veri akışı için aktif problem çözümü gerçekleştiriyorum.',
            'order': 1,
        }
    )

    # --- Projeler (eğer henüz yoksa) ---
    Project.objects.get_or_create(
        title='AWS Yüksek Trafikli Web Platformu',
        defaults={
            'category': 'Bulut Mimarisi',
            'description': 'AWS üzerinde ölçeklenebilir altyapı tasarımı.',
            'tech_description': 'EC2 Auto Scaling, RDS, ElastiCache, Docker ve CloudFront kullanarak ölçeklenebilir altyapı tasarımı ve WAF ile güvenlik optimizasyonu.',
            'filter_tag': 'filter-web',
            'image': 'portfolio/aws.jpg',
            'order': 1,
        }
    )
    Project.objects.get_or_create(
        title='Global E-Fatura Optimizasyonu',
        defaults={
            'category': 'SAP & ABAP',
            'description': 'ABAP kod düzeyinde hata ayıklama.',
            'tech_description': 'ABAP kod düzeyinde hata ayıklama yaparak global e-fatura iş akışlarındaki kök neden analizini sağlama ve sistem darboğazlarını çözme.',
            'filter_tag': 'filter-sap',
            'image': 'portfolio/sap.png',
            'order': 2,
        }
    )
    Project.objects.get_or_create(
        title='Gurmeo_O Keşif Platformu',
        defaults={
            'category': 'Full-Stack Geliştirme',
            'description': 'Node.js, Express ve MySQL tabanlı platform.',
            'tech_description': 'Node.js, Express ve MySQL kullanılarak geliştirilmiş, diyet tabanlı filtreleme algoritmaları ve sosyal modüllere sahip entegre platform.',
            'filter_tag': 'filter-web',
            'image': 'portfolio/gurmeo.jpg',
            'order': 3,
        }
    )

    # --- Sosyal Linkler ---
    SocialLink.objects.get_or_create(
        platform='Github',
        defaults={
            'url': 'https://github.com/ibrahimsariates',
            'icon_class': 'bi bi-github',
            'order': 1,
        }
    )
    SocialLink.objects.get_or_create(
        platform='LinkedIn',
        defaults={
            'url': 'https://www.linkedin.com/in/ibrahim-metehan-sar%C4%B1ate%C5%9F-696996356/',
            'icon_class': 'bi bi-linkedin',
            'order': 2,
        }
    )

    # --- İletişim Bilgileri ---
    ContactInfo.objects.get_or_create(
        label='Email Adresi',
        defaults={
            'icon_class': 'bi bi-envelope',
            'value': 'metehansariates37@gmail.com',
            'order': 1,
        }
    )
    ContactInfo.objects.get_or_create(
        label='Konum',
        defaults={
            'icon_class': 'bi bi-geo-alt',
            'value': 'İstanbul, Türkiye',
            'order': 2,
        }
    )


def reverse_seed(apps, schema_editor):
    """Geri alma: Seed verilerini siler."""
    pass  # Veriyi silmek istemiyoruz, boş bırakıyoruz


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_aboutsection_certificate_contactinfo_education_and_more'),
    ]

    operations = [
        migrations.RunPython(seed_data, reverse_seed),
    ]
