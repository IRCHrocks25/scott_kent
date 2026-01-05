# Scott & Shannon Kent - Business Growth Systems Website

A premium, calm confidence website built with Django, featuring a complete content management system and modern design system.

## Features

- **Complete CMS**: All content editable through Django admin
- **Premium Design System**: Calm, confident, founder-to-founder aesthetic
- **Responsive Layout**: Mobile-first design with smooth animations
- **Section Management**: Toggle sections on/off, customize all content
- **Image Management**: Upload and manage images for all sections
- **Testimonials**: Dynamic testimonial system
- **Statistics**: Display key metrics and results
- **Methodology Timeline**: Step-by-step process visualization

## Quick Setup

### Option 1: Automated Setup (Recommended)

**Windows (PowerShell):**
```powershell
.\setup.ps1
```

**Windows (Command Prompt):**
```cmd
setup.bat
```

**Manual Setup:**
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Create and run migrations
python manage.py makemigrations
python manage.py migrate

# 3. Populate initial content (IMPORTANT!)
python manage.py populate_initial_data

# 4. Create superuser (optional)
python manage.py createsuperuser

# 5. Run server
python manage.py runserver
```

### What Gets Populated

The `populate_initial_data` command automatically fills in:
- ✅ Hero section with all copy
- ✅ Credibility section with testimonials and authority bullets
- ✅ Pain points with statistics
- ✅ Who we work with section
- ✅ All 3 services
- ✅ 5 differentiators
- ✅ About section with full story
- ✅ 5 methodology steps
- ✅ Speaking section
- ✅ Final CTA
- ✅ Footer with contact info and social links

Visit `http://localhost:8000` to see your site and `http://localhost:8000/admin` to manage content.

## Admin Configuration

### Initial Setup

1. **Site Settings**: Go to Admin → Site Settings and configure:
   - Site name
   - Logo (optional)
   - Primary CTA text and URL

2. **Navigation Links**: Add header navigation links with order and URLs

3. **Hero Section**: Configure the main hero section with:
   - Headline, subheadline, body text
   - Quote and author
   - Primary and secondary CTAs
   - Hero image

4. **Credibility Section**: Add:
   - Authority bullets (e.g., "12+ Businesses Built")
   - Testimonials with quotes, authors, roles

5. **Pain Points Section**: Add statistics and pain point messaging

6. **Who We Work With**: Add bullet points describing ideal clients

7. **Services**: Add service cards with icons, descriptions, and "perfect for" text

8. **Differentiators**: Highlight what makes you different

9. **About Section**: Add your story and team photo

10. **Methodology**: Add step-by-step process (1-5 steps)

11. **Speaking Section**: Configure speaking/transformation content

12. **Final CTA**: Set up the final call-to-action section

13. **Footer**: Configure footer content, links, and social media

## Design System

### Colors
- **Primary**: Deep navy (#1e3a5f) - Trust, intelligence
- **Accent**: Soft teal (#2d7d7d) - Growth, clarity
- **Highlight**: Warm amber (#d4a574) - Momentum
- **Backgrounds**: Soft warm white, light grey

### Typography
- **Headings**: Clean modern sans-serif (system fonts)
- **Body**: High-legibility serif or humanist sans

### Spacing
- Generous spacing throughout
- Consistent vertical rhythm
- Comfortable padding on all elements

### Visual Elements
- Rounded corners (large radius)
- Soft shadows
- Subtle gradients
- Gentle animations (respects reduced motion)

## Section Toggles

Each section has a `show_section` toggle in the admin. Uncheck to hide any section from the homepage.

## Image Guidelines

- Use high-quality images
- Recommended formats: JPG, PNG, WebP
- Optimize images before uploading
- Alt text is important for accessibility

## Customization

### CSS Variables

Edit `static/css/main.css` to customize:
- Colors (CSS variables in `:root`)
- Typography
- Spacing
- Shadows
- Border radius

### Templates

All templates are in `templates/myApp/`:
- `base.html` - Base layout
- `home.html` - Homepage
- `partials/` - Individual section templates

## Deployment

### Railway Deployment

The site is configured for Railway with:
- `ALLOWED_HOSTS` includes Railway domain
- `CSRF_TRUSTED_ORIGINS` configured
- Static files ready for collection

### Environment Variables

For production, set:
- `DEBUG=False`
- `SECRET_KEY` (use environment variable)
- `ALLOWED_HOSTS` (already configured)

## Support

For questions or issues, refer to the Django documentation or contact the development team.
