@echo off
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
    python bootstrap.py --demo
) else (
    py -3 bootstrap.py --demo
)
if errorlevel 1 pause
