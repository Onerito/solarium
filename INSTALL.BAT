@echo off
setlocal

:: Save the current directory
set "orig_dir=%~dp0"
cd /d "%orig_dir%"

:: Check for administrative privileges
openfiles >nul 2>&1
if %errorlevel% neq 0 (
    echo This script requires administrative privileges.
    echo Please right-click the script and select "Run as administrator".
    pause
    exit /b 1
)

:: Your installer code here
echo Running from: %orig_dir%
miniconda\python.exe installer.py

endlocal
pause