from django.shortcuts import render
from django.db import OperationalError
from .models import (
    SiteSettings, NavigationLink, HeroSection, CredibilitySection,
    PainPointsSection, WhoWeWorkWithSection, Service, Differentiator,
    AboutSection, MethodologyStep, SpeakingSection, FinalCTASection,
    Footer
)


def get_or_default(model_class, default_instance=None):
    """Safely get first object or return default, handling missing tables"""
    try:
        obj = model_class.objects.first()
        if obj:
            return obj
        return default_instance or model_class()
    except OperationalError:
        # Database tables don't exist yet - return default instance
        return default_instance or model_class()


def get_queryset_or_empty(model_class):
    """Safely get queryset or return empty list, handling missing tables"""
    try:
        return model_class.objects.filter(show_section=True)
    except OperationalError:
        # Database tables don't exist yet - return empty list
        return []


def get_nav_links():
    """Safely get navigation links"""
    try:
        return NavigationLink.objects.filter(is_active=True)
    except OperationalError:
        return []


def home(request):
    """Homepage view with all sections"""
    try:
        # Try to access the database - if tables don't exist, show setup page
        SiteSettings.objects.first()
        
        context = {
            'site_settings': get_or_default(SiteSettings),
            'nav_links': get_nav_links(),
            'hero': get_or_default(HeroSection),
            'credibility': get_or_default(CredibilitySection),
            'pain_points': get_or_default(PainPointsSection),
            'who_we_work_with': get_or_default(WhoWeWorkWithSection),
            'services': get_queryset_or_empty(Service),
            'differentiators': get_queryset_or_empty(Differentiator),
            'about': get_or_default(AboutSection),
            'methodology_steps': get_queryset_or_empty(MethodologyStep),
            'speaking': get_or_default(SpeakingSection),
            'final_cta': get_or_default(FinalCTASection),
            'footer': get_or_default(Footer),
        }
        return render(request, 'myApp/home.html', context)
    except OperationalError:
        # Database tables don't exist - show setup instructions
        return render(request, 'myApp/migrations_needed.html', {
            'migrations_needed': True
        })
