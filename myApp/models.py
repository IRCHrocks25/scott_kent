from django.db import models
from django.core.validators import URLValidator


class SiteSettings(models.Model):
    """Global site settings"""
    site_name = models.CharField(max_length=200, default="Scott & Shannon Kent")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    primary_cta_text = models.CharField(max_length=100, default="Book Diagnostic")
    primary_cta_url = models.URLField(default="#")
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return "Site Settings"


class NavigationLink(models.Model):
    """Header navigation links"""
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.label


class HeroSection(models.Model):
    """Hero section configuration"""
    show_section = models.BooleanField(default=True)
    emphasize_as_key_section = models.BooleanField(default=True)
    
    headline = models.CharField(max_length=200, default="The Engine Behind Your Next Level of Growth")
    subheadline = models.TextField(default="Reclaim up to 20+ hours a week and accelerate profit growth with AI-powered systems built for real businesses.")
    body_text = models.TextField(default="Most founders rely on guesswork. You don't have time for that. Think of us as your revenue GPS—clear, direct, data-driven. This isn't about working harder; it's about making every move count.")
    quote_text = models.TextField(default="AI should create freedom, not friction.")
    quote_author = models.CharField(max_length=200, default="Scott & Shannon Kent")
    
    primary_button_label = models.CharField(max_length=100, default="Book Your Diagnostic Assessment")
    primary_button_url = models.URLField(default="#")
    secondary_button_label = models.CharField(max_length=100, default="Download the Free Checklist")
    secondary_button_url = models.URLField(default="#")
    
    image = models.ImageField(upload_to='hero/', blank=True, null=True)
    image_alt_text = models.CharField(max_length=200, blank=True)
    background_style = models.CharField(
        max_length=50,
        choices=[
            ('gradient', 'Gradient'),
            ('texture', 'Texture'),
            ('solid', 'Solid'),
        ],
        default='gradient'
    )
    
    class Meta:
        verbose_name = "Hero Section"
        verbose_name_plural = "Hero Section"
    
    def __str__(self):
        return "Hero Section"


class CredibilitySection(models.Model):
    """Credibility, Expertise & Testimonials section"""
    show_section = models.BooleanField(default=True)
    
    headline = models.CharField(max_length=200, default="The Engine Behind Your Next Level of Growth")
    intro_paragraph = models.TextField(default="When a business looks effortless, it's because the right systems are working quietly in the background.")
    
    primary_button_label = models.CharField(max_length=100, default="Start Your Profit Reclaim Today")
    primary_button_url = models.URLField(default="#")
    background_style = models.CharField(
        max_length=50,
        choices=[
            ('light', 'Light'),
            ('neutral', 'Neutral Band'),
            ('texture', 'Texture'),
        ],
        default='neutral'
    )
    
    class Meta:
        verbose_name = "Credibility Section"
        verbose_name_plural = "Credibility Section"
    
    def __str__(self):
        return "Credibility Section"


class AuthorityBullet(models.Model):
    """Authority bullet points for credibility section"""
    section = models.ForeignKey(CredibilitySection, related_name='authority_bullets', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.text


class Testimonial(models.Model):
    """Testimonials"""
    section = models.ForeignKey(CredibilitySection, related_name='testimonials', on_delete=models.CASCADE)
    quote = models.TextField()
    author = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.author} - {self.quote[:50]}..."


class PainPointsSection(models.Model):
    """Pain Points & Solution + Statistics section"""
    show_section = models.BooleanField(default=True)
    
    headline = models.CharField(max_length=200, default="Scaling doesn't break founders. Broken systems do.")
    pain_intro_text = models.TextField(default="Growth shouldn't feel heavier the bigger you get. Every day you delay, time and profit leak out of your business.")
    
    quote = models.TextField(blank=True)
    quote_author = models.CharField(max_length=200, blank=True)
    
    primary_button_label = models.CharField(max_length=100, default="Start Clearing the Bottlenecks Today")
    primary_button_url = models.URLField(default="#")
    background_style = models.CharField(
        max_length=50,
        choices=[
            ('light', 'Light'),
            ('gradient', 'Gradient'),
        ],
        default='light'
    )
    
    class Meta:
        verbose_name = "Pain Points Section"
        verbose_name_plural = "Pain Points Section"
    
    def __str__(self):
        return "Pain Points Section"


class Statistic(models.Model):
    """Statistics for pain points section"""
    section = models.ForeignKey(PainPointsSection, related_name='stats', on_delete=models.CASCADE)
    stat = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    result = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.stat} - {self.description}"


class WhoWeWorkWithSection(models.Model):
    """Who We Work Best With section"""
    show_section = models.BooleanField(default=True)
    
    headline = models.CharField(max_length=200, default="Not for Everyone — Designed for Founders Like You")
    intro_text = models.TextField(blank=True)
    
    quote = models.TextField(blank=True)
    quote_author = models.CharField(max_length=200, blank=True)
    
    primary_button_label = models.CharField(max_length=100, default="See If You're the Right Fit")
    primary_button_url = models.URLField(default="#")
    background_style = models.CharField(
        max_length=50,
        choices=[
            ('light', 'Light'),
            ('highlight', 'Highlighted Band'),
        ],
        default='highlight'
    )
    
    class Meta:
        verbose_name = "Who We Work With Section"
        verbose_name_plural = "Who We Work With Section"
    
    def __str__(self):
        return "Who We Work With Section"


class BulletPoint(models.Model):
    """Bullet points for who we work with section"""
    section = models.ForeignKey(WhoWeWorkWithSection, related_name='bullet_points', on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.text


class Service(models.Model):
    """Services & Offerings"""
    show_section = models.BooleanField(default=True)
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    perfect_for = models.CharField(max_length=300, blank=True)
    icon = models.CharField(max_length=100, blank=True, help_text="FontAwesome icon class (e.g., fa-rocket)")
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class Differentiator(models.Model):
    """Differentiators section"""
    show_section = models.BooleanField(default=True)
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title


class AboutSection(models.Model):
    """About Us / Authority section"""
    show_section = models.BooleanField(default=True)
    
    headline = models.CharField(max_length=200, default="About Us")
    body_text = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)
    image_alt_text = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name = "About Section"
        verbose_name_plural = "About Section"
    
    def __str__(self):
        return "About Section"


class MethodologyStep(models.Model):
    """Methodology steps"""
    show_section = models.BooleanField(default=True)
    
    step_number = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    outcome = models.CharField(max_length=300, help_text="The result: ...")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"Step {self.step_number}: {self.title}"


class SpeakingSection(models.Model):
    """Speaking & Transformation section"""
    show_section = models.BooleanField(default=True)
    
    headline = models.CharField(max_length=200)
    body_text = models.TextField()
    cta_label = models.CharField(max_length=100, default="Download Kit")
    cta_url = models.URLField(default="#")
    image = models.ImageField(upload_to='speaking/', blank=True, null=True)
    
    class Meta:
        verbose_name = "Speaking Section"
        verbose_name_plural = "Speaking Section"
    
    def __str__(self):
        return "Speaking Section"


class FinalCTASection(models.Model):
    """Final CTA section"""
    show_section = models.BooleanField(default=True)
    
    headline = models.CharField(max_length=200, default="Get Your Business Assessment")
    body_text = models.TextField(blank=True)
    cta_label = models.CharField(max_length=100, default="Get Your Business Assessment")
    cta_url = models.URLField(default="#")
    
    class Meta:
        verbose_name = "Final CTA Section"
        verbose_name_plural = "Final CTA Section"
    
    def __str__(self):
        return "Final CTA Section"


class Footer(models.Model):
    """Footer configuration"""
    brand_mission = models.TextField(blank=True)
    address = models.TextField(blank=True)
    phone = models.CharField(max_length=50, blank=True)
    email = models.EmailField(blank=True)
    copyright_text = models.CharField(max_length=200, default="© 2024 Scott & Shannon Kent. All rights reserved.")
    
    class Meta:
        verbose_name = "Footer"
        verbose_name_plural = "Footer"
    
    def __str__(self):
        return "Footer"


class FooterLink(models.Model):
    """Footer links"""
    footer = models.ForeignKey(Footer, related_name='links', on_delete=models.CASCADE)
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    column = models.IntegerField(choices=[(1, 'Column 1'), (2, 'Column 2'), (3, 'Column 3'), (4, 'Column 4')], default=1)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['column', 'order']
    
    def __str__(self):
        return self.label


class SocialLink(models.Model):
    """Social media links"""
    footer = models.ForeignKey(Footer, related_name='social_links', on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon = models.CharField(max_length=100, blank=True, help_text="FontAwesome icon class")
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.platform
