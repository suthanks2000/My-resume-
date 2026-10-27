@echo off
set OUT_DIR=%1
if "%OUT_DIR%"=="" set OUT_DIR=v3
echo Running Resume Builder for output folder: %OUT_DIR%
python build_resume.py %OUT_DIR%
echo Done! Files generated in %OUT_DIR%
pause

