@echo off
REM To run type ./run.bat in powershell
start cmd /k run_backend.bat
start cmd /k run_frontend.bat

start "" "http://localhost:4200/"