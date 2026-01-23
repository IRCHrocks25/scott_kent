"""
Management command to populate initial website content.
Run: python manage.py populate_initial_data
"""
from django.core.management.base import BaseCommand
from myApp.models import (
    SiteSettings, NavigationLink, HeroSection, CredibilitySection,
    AuthorityBullet, Testimonial, PainPointsSection, Statistic,
    WhoWeWorkWithSection, BulletPoint, Service, Differentiator,
    AboutSection, MethodologyStep, SpeakingSection, FinalCTASection,
    Footer, FooterLink, SocialLink
)


class Command(BaseCommand):
    help = 'Populates the database with initial website content'

    def handle(self, *args, **options):
        self.stdout.write('Populating initial data...')
        self.stdout.write('')
        
        # Check if migrations have been run
        try:
            from django.db import connection
            with connection.cursor() as cursor:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='myApp_sitesettings'")
                if not cursor.fetchone():
                    self.stdout.write(self.style.ERROR('❌ ERROR: Database tables not found!'))
                    self.stdout.write(self.style.WARNING('Please run migrations first:'))
                    self.stdout.write('  1. python manage.py makemigrations')
                    self.stdout.write('  2. python manage.py migrate')
                    self.stdout.write('  3. python manage.py populate_initial_data')
                    return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ ERROR: {str(e)}'))
            self.stdout.write(self.style.WARNING('Please run migrations first:'))
            self.stdout.write('  1. python manage.py makemigrations')
            self.stdout.write('  2. python manage.py migrate')
            return
        
        # Site Settings
        site_settings, created = SiteSettings.objects.get_or_create(
            id=1,
            defaults={
                'site_name': 'Scott & Shannon Kent',
                'primary_cta_text': 'Book Diagnostic',
                'primary_cta_url': '#',
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Site Settings'))
        
        # Navigation Links
        NavigationLink.objects.all().delete()
        nav_links_data = [
            {'label': 'Services', 'url': '#services', 'order': 1},
            {'label': 'About', 'url': '#about', 'order': 2},
            {'label': 'Methodology', 'url': '#methodology', 'order': 3},
        ]
        for nav_data in nav_links_data:
            NavigationLink.objects.create(**nav_data)
        self.stdout.write(self.style.SUCCESS('✓ Navigation Links'))
        
        # Hero Section
        hero, created = HeroSection.objects.get_or_create(
            id=1,
            defaults={
                'show_section': True,
                'emphasize_as_key_section': True,
                'headline': 'The Engine Behind Your Next Level of Growth',
                'subheadline': 'Reclaim up to 20+ hours a week and accelerate profit growth using AI-powered systems',
                'body_text': "Most founders rely on guesswork. You don't have time for that. Think of us as your Revenue GPS, charting the fastest and clearest path to profit. We help you stop flying blind and start leading with a solid, data driven flight plan. This isn't about working harder. It's about making every move count.",
                'quote_text': 'AI should create freedom, not friction.',
                'quote_author': 'Scott & Shannon Kent',
                'primary_button_label': 'Book your diagnostic assessment –unlock your fastest path to scalable revenue today!',
                'primary_button_url': '#',
                'secondary_button_label': 'Download a Free Checklist',
                'secondary_button_url': '#',
                'background_style': 'gradient',
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Hero Section'))
        
        # Credibility Section
        credibility, created = CredibilitySection.objects.get_or_create(
            id=1,
            defaults={
                'show_section': True,
                'headline': "The Engine Behind Your Next Level of Growth",
                'intro_paragraph': "When a business looks effortless, it's because the right systems are working quietly in the background.\nWe built and scaled 12+ companies ourselves. Our results come from decades of hands-on experience as founders and enterprise-level engineers. We know what it takes to build a business from scratch and the systems it needs to scale.",
                'primary_button_label': 'Start Your Profit Reclaim Today',
                'primary_button_url': '#',
                'background_style': 'neutral',
            }
        )
        
        # Authority Bullets
        AuthorityBullet.objects.filter(section=credibility).delete()
        authority_bullets = [
            {'text': '12+ Businesses Built and Scaled: Scott is a lifelong entrepreneur with a mechanical eye for solving complex problems and creating workflows that last.', 'order': 1},
            {'text': '25+ Years Designing Systems: Shannon has built operations for enterprise organizations, designing processes that keep businesses running smoothly and customers coming back.', 'order': 2},
            {'text': 'Proven Playbook, Not Just Theory: We bring tested systems to every client. Our focus is on solutions that work in practice, not just academic concepts.', 'order': 3},
            {'text': 'Clarity: We start by understanding what your business needs, then design systems that fit.', 'order': 4},
        ]
        for bullet_data in authority_bullets:
            AuthorityBullet.objects.create(section=credibility, **bullet_data)
        
        # Testimonials
        Testimonial.objects.filter(section=credibility).delete()
        testimonials = [
            {
                'quote': "These systems gave us our time back. We were overwhelmed by the noise, but Scott and Shannon showed us where to focus. Now we save 10–20 hours a week and actually drive profit.",
                'author': 'Founder',
                'role': 'SaaS Company',
                'location': 'U.S.',
                'order': 1,
            },
            {
                'quote': 'Our lead conversion jumped 30%. We thought we needed more marketing, but they showed us how to maximize the leads we already had. Their process is a revenue engine.',
                'author': 'CEO',
                'role': 'Manufacturing Firm',
                'location': 'EU',
                'order': 2,
            },
            {
                'quote': "The best part is the confidence we feel. We now know how to scale with a clear plan, not just a hope. It's a true partnership, and it's a game-changer.",
                'author': 'Entrepreneur',
                'role': 'Professional Services',
                'location': 'U.K.',
                'order': 3,
            },
        ]
        for testimonial_data in testimonials:
            Testimonial.objects.create(section=credibility, **testimonial_data)
        self.stdout.write(self.style.SUCCESS('✓ Credibility Section'))
        
        # Pain Points Section
        pain_points, created = PainPointsSection.objects.get_or_create(
            id=1,
            defaults={
                'show_section': True,
                'headline': "Scaling doesn't break founders. Broken systems do.",
                'pain_intro_text': "Are you're experiencing overwhelm, frustration, and burnout trying to stay ahead of your competitors? We will design tools and systems that will free you from the emotional stress your business is causing you.\nGrowth shouldn't feel heavier the bigger you get. Most founder-led businesses hit a ceiling when their systems fall behind. It's not your effort that's holding you back; it's the way your business systems operate.",
                'quote': "No complexity. No hype. Just clean, smart systems that help you deliver what your customers expect. Consistently and confidently.",
                'quote_author': 'Scott & Shannon Kent',
                'primary_button_label': 'Start Clearing the Bottlenecks Today',
                'primary_button_url': '#',
                'background_style': 'light',
            }
        )
        
        Statistic.objects.filter(section=pain_points).delete()
        statistics = [
            {
                'stat': '69 days',
                'description': 'SMB teams lose per year to manual admin tasks.',
                'result': 'Companies using our Enterprise Growth Engine™ reclaim that time, boosting productivity by up to 20% and cutting costs by up to 15%.',
                'order': 1,
            },
            {
                'stat': '20–30%',
                'description': 'of annual revenue drained from SMBs by inefficiencies.',
                'result': 'With the Enterprise Growth Engine™, founders often see ROI of up to 500%+ from better lead nurturing and engagement.',
                'order': 2,
            },
            {
                'stat': '5x faster',
                'description': 'Competitors respond to customers while only 15% of small businesses use marketing automation.',
                'result': 'Early adopters who plug into our framework see up to 50% more leads and 70% shorter sales cycles.',
                'order': 3,
            },
            {
                'stat': '19%',
                'description': 'Annual growth drops without structural change when founder-led sales bottlenecks stall growth beyond ~$3.5M.',
                'result': 'Our Enterprise Growth Engine™ wipes away bottlenecks so you can lead with confidence and scale faster.',
                'order': 4,
            },
        ]
        for stat_data in statistics:
            Statistic.objects.create(section=pain_points, **stat_data)
        self.stdout.write(self.style.SUCCESS('✓ Pain Points Section'))
        
        # Who We Work With Section
        who_we_work_with, created = WhoWeWorkWithSection.objects.get_or_create(
            id=1,
            defaults={
                'show_section': True,
                'headline': 'Not for Everyone, Just for Founders Like You.',
                'intro_text': 'We partner with leaders who move fast, think bigger, and refuse to stay stuck.\nWe are not built for hesitation or half-measures. The founders we serve are ready to invest in clarity, build systems that last, and free themselves from the daily grind of "doing it all."',
                'quote': "We're not just optimizing systems, we're freeing founders to lead their life and business by design, not by default.",
                'quote_author': 'Scott & Shannon Kent',
                'primary_button_label': "See If You're the Right Fit",
                'primary_button_url': '#',
                'background_style': 'highlight',
            }
        )
        
        BulletPoint.objects.filter(section=who_we_work_with).delete()
        bullet_points = [
            {'text': 'A business pushing past $1M-$30M and aiming higher.', 'order': 1},
            {'text': 'A leader who wants scalable systems, not more hustle.', 'order': 2},
            {'text': 'A team caught in the noise of tools but craving clarity.', 'order': 3},
            {'text': 'A founder obsessed with growth, profit, and customer experience.', 'order': 4},
            {'text': 'Someone who values partnership and execution, not just advice.', 'order': 5},
        ]
        for bullet_data in bullet_points:
            BulletPoint.objects.create(section=who_we_work_with, **bullet_data)
        self.stdout.write(self.style.SUCCESS('✓ Who We Work With Section'))
        
        # Services
        Service.objects.all().delete()
        services = [
            {
                'title': 'AI Readiness Diagnostic + Roadmap',
                'description': 'Your first step toward clarity. We map your workflows, uncover leaks, and design a tailored roadmap for growth.',
                'perfect_for': 'Founders who feel stuck in the noise and want a clear path forward.',
                'icon': 'fas fa-search',
                'order': 1,
                'show_section': True,
            },
            {
                'title': '90-Day ACTIV Sprint',
                'description': 'Our flagship transformation program. In just 90 days, we install high-impact systems that reclaim time, optimize processes, and deliver measurable ROI.',
                'perfect_for': 'Companies ready to move fast and see real results.',
                'icon': 'fas fa-rocket',
                'order': 2,
                'show_section': True,
            },
            {
                'title': 'Fractional AI Advisor / Embedded Partner',
                'description': 'When growth demands an ongoing partner, we step in as your embedded advisor. We evolve systems, coach leadership, and keep growth on track long-term.',
                'perfect_for': 'Scaling teams who want a trusted partner, not just a consultant.',
                'icon': 'fas fa-handshake',
                'order': 3,
                'show_section': True,
            },
        ]
        for service_data in services:
            Service.objects.create(**service_data)
        self.stdout.write(self.style.SUCCESS('✓ Services'))
        
        # Differentiators
        Differentiator.objects.all().delete()
        differentiators = [
            {
                'title': 'Needs-First, Not Tools-First',
                'description': 'We start with your business needs and goals, not with the latest software. Every system we design serves your growth, not a vendor\'s agenda.',
                'icon': 'fas fa-bullseye',
                'order': 1,
                'show_section': True,
            },
            {
                'title': 'Founder-LED Experience + Enterprise Systems Expertise',
                'description': 'Battle Tested Growth Playbook, Not Theoretical Advice',
                'icon': 'fas fa-shield-alt',
                'order': 2,
                'show_section': True,
            },
            {
                'title': 'Execution Partnership, Not Just Consulting',
                'description': "We don't just leave you with homework. We roll up our sleeves and stay with you through the entire implementation process.",
                'icon': 'fas fa-users-cog',
                'order': 3,
                'show_section': True,
            },
            {
                'title': 'Founder Coaching Built In',
                'description': 'Scaling is as much about leadership as systems. We coach founders through the mindset shifts that are essential to growth, your personal support team.',
                'icon': 'fas fa-chalkboard-teacher',
                'order': 4,
                'show_section': True,
            },
            {
                'title': 'Adaptive Partnership',
                'description': 'We don\'t disappear after the sprint. We stay as your partner, evolving your systems as your business and the market change.',
                'icon': 'fas fa-sync-alt',
                'order': 5,
                'show_section': True,
            },
        ]
        for diff_data in differentiators:
            Differentiator.objects.create(**diff_data)
        self.stdout.write(self.style.SUCCESS('✓ Differentiators'))
        
        # About Section
        about, created = AboutSection.objects.get_or_create(
            id=1,
            defaults={
                'show_section': True,
                'headline': 'Meet Your AI Profit Architects',
                'body_text': "We're not consultants who only preach from a whiteboard. We are founders who have lived the grind and built the systems to escape it.\n\nWe're Scott and Shannon Kent, a husband-and-wife team who know what it feels like to face a business-defining moment. We transformed a declining printing business into a future-proof consultancy and, in the process, gained something invaluable: the time to build smarter systems.\n\nScott Kent: The Entrepreneur\nScott has built more than a dozen companies from scratch, including a 70-employee retail chain. A lifelong entrepreneur with a mechanical mind, Scott instantly sees where workflows jam and how to fix them fast. His grit comes with humor, and his focus is always on the bottom line. Always looking for the efficiency angle, Scott puts functional systems in place to save time, money and which increase customer experience.\n\nShannon Kent: The Systems Expert\nShannon brings 25+ years of corporate operations and system design. As a Multimedia Solutions Architect, she built high-stakes systems and trained enterprise teams to use them. She's a natural at mapping customer journeys, known for her precision in process design.\n\nOur Story, Your Advantage\nTogether, we bring a rare blend of entrepreneurial grit and corporate systems mastery. Our clients don't just get a plan; they get a partnership that blends lived founder experience with enterprise-level execution. The result is simple: clarity, profit, and growth without the drag.",
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ About Section'))
        
        # Methodology Steps
        MethodologyStep.objects.all().delete()
        methodology_steps = [
            {
                'step_number': 1,
                'title': 'Revenue Workflow Audit',
                'description': 'We map your sales, marketing, and customer experience processes to pinpoint what\'s costing you time, money, and momentum.',
                'outcome': 'Clarity on hidden leaks and bottlenecks.',
                'order': 1,
                'show_section': True,
            },
            {
                'step_number': 2,
                'title': 'Growth Mapping',
                'description': 'We design a tailored system that eliminates friction, automates what matters, and amplifies ROI where money moves.',
                'outcome': 'A strategic blueprint directly tied to revenue growth.',
                'order': 2,
                'show_section': True,
            },
            {
                'step_number': 3,
                'title': 'Intelligent Systems Installation',
                'description': 'We design, install and integrate solutions that run quietly in the background, saving hours and compounding your margin.',
                'outcome': 'Systems that work reliably without disrupting your team.',
                'order': 3,
                'show_section': True,
            },
            {
                'step_number': 4,
                'title': 'Performance Optimization',
                'description': 'We track results, fine-tune automations, and scale what\'s working.',
                'outcome': 'Continuous improvement tied to profit, time savings, and lead flow.',
                'order': 4,
                'show_section': True,
            },
            {
                'step_number': 5,
                'title': 'Strategic Partnership Support',
                'description': "We don't disappear after setup. We stay with you to adapt, coach, and evolve systems as your business grows.",
                'outcome': 'Long-term confidence and sustainable growth.',
                'order': 5,
                'show_section': True,
            },
        ]
        for step_data in methodology_steps:
            MethodologyStep.objects.create(**step_data)
        self.stdout.write(self.style.SUCCESS('✓ Methodology Steps'))
        
        # Speaking Section
        speaking, created = SpeakingSection.objects.get_or_create(
            id=1,
            defaults={
                'show_section': True,
                'headline': 'More than speakers, catalysts for change.',
                'body_text': "This Speaker Kit captures Scott and Shannon Kent's mission, keynotes, and media presence, giving event organizers everything they need to bring insight, momentum, and lasting transformation to their audience.",
                'cta_label': 'Bring Transformation to Your Stage',
                'cta_url': '#',
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Speaking Section'))
        
        # Final CTA Section
        final_cta, created = FinalCTASection.objects.get_or_create(
            id=1,
            defaults={
                'show_section': True,
                'headline': 'Get Your Business Assessment',
                'body_text': "Your competitors aren't waiting and neither should you. Every day you delay fixing broken systems, you lose time and money to competitors who are already scaling smart.\n\nOne diagnostic today can reveal the leaks, bottlenecks, and opportunities shaping your future growth.\n\n\"Nobody ever succeeds by waiting for the right time.\" — Scott & Shannon Kent\n\nWe'll show you where your systems drag, where profit is leaking, and how the Enterprise Growth Engine™ can fix it.",
                'cta_label': 'Get Your Business Assessment',
                'cta_url': '#',
            }
        )
        self.stdout.write(self.style.SUCCESS('✓ Final CTA Section'))
        
        # Footer
        footer, created = Footer.objects.get_or_create(
            id=1,
            defaults={
                'brand_mission': "Our systems don't just make your business run smoother, they help you show up better for the people you serve.",
                'address': 'Ventura, California',
                'email': 'hello@scottandshannon.com',
                'phone': '(placeholder phone number)',
                'copyright_text': '© 2025 Scott & Shannon Kent. All rights reserved.',
            }
        )
        
        FooterLink.objects.filter(footer=footer).delete()
        footer_links = [
            {'label': 'Services', 'url': '#services', 'column': 2, 'order': 1},
            {'label': 'About', 'url': '#about', 'column': 2, 'order': 2},
            {'label': 'Methodology', 'url': '#methodology', 'column': 2, 'order': 3},
        ]
        for link_data in footer_links:
            FooterLink.objects.create(footer=footer, **link_data)
        
        SocialLink.objects.filter(footer=footer).delete()
        social_links = [
            {'platform': 'LinkedIn', 'url': '#', 'icon': 'fab fa-linkedin', 'order': 1},
            {'platform': 'YouTube', 'url': '#', 'icon': 'fab fa-youtube', 'order': 2},
        ]
        for social_data in social_links:
            SocialLink.objects.create(footer=footer, **social_data)
        self.stdout.write(self.style.SUCCESS('✓ Footer'))
        
        self.stdout.write(self.style.SUCCESS('\n✅ All initial data populated successfully!'))
        self.stdout.write(self.style.WARNING('\nNext steps:'))
        self.stdout.write('1. Run: python manage.py migrate')
        self.stdout.write('2. Run: python manage.py populate_initial_data')
        self.stdout.write('3. Visit http://localhost:8000 to see your site')

