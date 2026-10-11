@echo off
cd /d "%~dp0"
where py >nul 2>nul
if errorlevel 1 (
    python run.py --demo
) else (
    py -3 run.py --demo
)
if errorlevel 1 pause
