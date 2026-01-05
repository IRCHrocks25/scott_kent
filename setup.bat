@echo off
echo Setting up Scott & Shannon Kent website...
echo.

echo Step 1: Creating database migrations...
python manage.py makemigrations
if %errorlevel% neq 0 (
    echo ERROR: Failed to create migrations
    pause
    exit /b 1
)

echo.
echo Step 2: Running migrations...
python manage.py migrate
if %errorlevel% neq 0 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)

echo.
echo Step 3: Populating initial content...
python manage.py populate_initial_data
if %errorlevel% neq 0 (
    echo ERROR: Failed to populate initial data
    pause
    exit /b 1
)

echo.
echo ✅ Setup complete!
echo.
echo Next steps:
echo 1. Create a superuser (optional): python manage.py createsuperuser
echo 2. Run the server: python manage.py runserver
echo 3. Visit http://localhost:8000 to see your site
echo 4. Visit http://localhost:8000/admin to manage content
echo.
pause

