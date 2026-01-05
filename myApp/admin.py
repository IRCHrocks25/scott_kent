from django.contrib import admin
from .models import (
    SiteSettings, NavigationLink, HeroSection, CredibilitySection,
    AuthorityBullet, Testimonial, PainPointsSection, Statistic,
    WhoWeWorkWithSection, BulletPoint, Service, Differentiator,
    AboutSection, MethodologyStep, SpeakingSection, FinalCTASection,
    Footer, FooterLink, SocialLink
)


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSettings.objects.exists()


class NavigationLinkInline(admin.TabularInline):
    model = NavigationLink
    extra = 1


@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ['label', 'url', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['headline', 'show_section']
    list_editable = ['show_section']


class AuthorityBulletInline(admin.TabularInline):
    model = AuthorityBullet
    extra = 1


class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1
    fields = ['quote', 'author', 'role', 'location', 'avatar', 'order']


@admin.register(CredibilitySection)
class CredibilitySectionAdmin(admin.ModelAdmin):
    inlines = [AuthorityBulletInline, TestimonialInline]
    list_display = ['headline', 'show_section']
    list_editable = ['show_section']


class StatisticInline(admin.TabularInline):
    model = Statistic
    extra = 1


@admin.register(PainPointsSection)
class PainPointsSectionAdmin(admin.ModelAdmin):
    inlines = [StatisticInline]
    list_display = ['headline', 'show_section']
    list_editable = ['show_section']


class BulletPointInline(admin.TabularInline):
    model = BulletPoint
    extra = 1


@admin.register(WhoWeWorkWithSection)
class WhoWeWorkWithSectionAdmin(admin.ModelAdmin):
    inlines = [BulletPointInline]
    list_display = ['headline', 'show_section']
    list_editable = ['show_section']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'show_section']
    list_editable = ['order', 'show_section']


@admin.register(Differentiator)
class DifferentiatorAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'show_section']
    list_editable = ['order', 'show_section']


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['headline', 'show_section']
    list_editable = ['show_section']


@admin.register(MethodologyStep)
class MethodologyStepAdmin(admin.ModelAdmin):
    list_display = ['step_number', 'title', 'order', 'show_section']
    list_editable = ['order', 'show_section']


@admin.register(SpeakingSection)
class SpeakingSectionAdmin(admin.ModelAdmin):
    list_display = ['headline', 'show_section']
    list_editable = ['show_section']


@admin.register(FinalCTASection)
class FinalCTASectionAdmin(admin.ModelAdmin):
    list_display = ['headline', 'show_section']
    list_editable = ['show_section']


class FooterLinkInline(admin.TabularInline):
    model = FooterLink
    extra = 1


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    inlines = [FooterLinkInline, SocialLinkInline]
    def has_add_permission(self, request):
        return not Footer.objects.exists()
