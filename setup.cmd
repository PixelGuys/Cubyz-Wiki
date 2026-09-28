@echo off
setlocal
set "SCRIPT=%~nx0"

echo %SCRIPT%: Creating virtual environment...
py -3 -m venv .env || python -m venv .env
if errorlevel 1 (
    echo %SCRIPT%: Failed to create virtual environment. Is Python installed and on PATH?
    exit /b 1
)

echo %SCRIPT%: Entering virtual env...
call ".env\Scripts\activate.bat"
if errorlevel 1 (
    echo %SCRIPT%: Failed to activate virtual environment.
    exit /b 1
)

echo %SCRIPT%: Installing wiki dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo %SCRIPT%: Dependency installation failed.
    exit /b 1
)

echo %SCRIPT%: Setup complete
echo.
echo %SCRIPT%: To start the wiki server, run:
echo %SCRIPT%:   '.env\Scripts\activate.bat'
echo %SCRIPT%:   'zensical serve'

