@echo off
title Servidor Django - Micro-sitio SENASOFT (ADSO 3232516)
echo ==========================================================
echo   INICIANDO MICRO-SITIO SENASOFT EN DJANGO
echo   Estudiante: Jhossep David Arce - ADSO 3232516
echo ==========================================================
echo.
python manage.py makemigrations
python manage.py migrate
echo.
echo Abriendo navegador en http://127.0.0.1:8000/senasoft/ ...
start http://127.0.0.1:8000/senasoft/
python manage.py runserver
pause
