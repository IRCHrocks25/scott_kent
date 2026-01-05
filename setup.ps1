Write-Host "Setting up Scott & Shannon Kent website..." -ForegroundColor Cyan
Write-Host ""

Write-Host "Step 1: Creating database migrations..." -ForegroundColor Yellow
python manage.py makemigrations
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to create migrations" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Step 2: Running migrations..." -ForegroundColor Yellow
python manage.py migrate
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to run migrations" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Step 3: Populating initial content..." -ForegroundColor Yellow
python manage.py populate_initial_data
if ($LASTEXITCODE -ne 0) {
    Write-Host "ERROR: Failed to populate initial data" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "✅ Setup complete!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Create a superuser (optional): python manage.py createsuperuser"
Write-Host "2. Run the server: python manage.py runserver"
Write-Host "3. Visit http://localhost:8000 to see your site"
Write-Host "4. Visit http://localhost:8000/admin to manage content"
Write-Host ""

