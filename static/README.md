# Static Files Directory

This directory contains static files for the website, including images, CSS, and JavaScript files.

## Directory Structure

```
static/
├── images/          # Image files (PNG, JPG, SVG, etc.)
├── css/             # CSS files (if needed)
└── js/              # JavaScript files (if needed)
```

## Using Images in Templates

To use images in your Django templates:

1. **Load the static tag** at the top of your template:
   ```django
   {% load static %}
   ```

2. **Reference the image** using the static tag:
   ```django
   <img src="{% static 'images/logo.png' %}" alt="Logo">
   ```

## Example

```django
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>My Page</title>
</head>
<body>
    <img src="{% static 'images/hero-image.jpg' %}" alt="Hero Image">
    <img src="{% static 'images/logo.png' %}" alt="Company Logo">
</body>
</html>
```

## Adding Images

Simply place your image files in the `static/images/` directory. Supported formats include:
- PNG (.png)
- JPEG/JPG (.jpg, .jpeg)
- SVG (.svg)
- GIF (.gif)
- WebP (.webp)

## Production

In production, run `python manage.py collectstatic` to collect all static files into the `STATIC_ROOT` directory for serving by your web server.
