from django.contrib import admin
from .models import (
    GeneralSetting, HeroSection, AboutSection,
    Education, Certificate, Experience,
    Project, SocialLink, ContactInfo
)


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['key', 'value', 'updated_date']
    list_editable = ['value']
    search_fields = ['key', 'value']
    list_per_page = 25


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'subtitle', 'typed_titles', 'updated_date']
    search_fields = ['name', 'subtitle']
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('name', 'subtitle', 'typed_titles', 'description')
        }),
        ('Görsel', {
            'fields': ('profile_image',)
        }),
    )


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'badge_text', 'updated_date']
    fieldsets = (
        ('Başlık', {
            'fields': ('badge_text', 'title')
        }),
        ('İçerik', {
            'fields': ('paragraph_1', 'paragraph_2')
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'institution', 'date_range', 'order', 'updated_date']
    list_editable = ['order', 'date_range']
    search_fields = ['title', 'institution']
    ordering = ['order']
    list_per_page = 25


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'provider', 'date', 'order', 'updated_date']
    list_editable = ['order', 'date']
    search_fields = ['name', 'provider']
    list_filter = ['provider']
    ordering = ['order']
    list_per_page = 25


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'date_range', 'location', 'order', 'updated_date']
    list_editable = ['order']
    search_fields = ['title', 'company']
    ordering = ['order']
    list_per_page = 25


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'filter_tag', 'order', 'updated_date']
    list_editable = ['category', 'filter_tag', 'order']
    search_fields = ['title', 'category', 'description']
    list_filter = ['filter_tag', 'category']
    ordering = ['order']
    list_per_page = 25
    fieldsets = (
        ('Temel Bilgiler', {
            'fields': ('title', 'category', 'filter_tag', 'order')
        }),
        ('İçerik', {
            'fields': ('description', 'tech_description')
        }),
        ('Görsel', {
            'fields': ('image',)
        }),
    )


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'icon_class', 'order', 'updated_date']
    list_editable = ['url', 'icon_class', 'order']
    search_fields = ['platform']
    ordering = ['order']
    list_per_page = 25


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ['label', 'value', 'icon_class', 'order', 'updated_date']
    list_editable = ['value', 'icon_class', 'order']
    search_fields = ['label', 'value']
    ordering = ['order']
    list_per_page = 25