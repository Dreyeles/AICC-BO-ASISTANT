@echo off
title AICC BO Assistant - Suite de Simuladores N2
cls
echo =====================================================================
echo           AICC BO ASSISTANT - SUITE DE DEMOSTRACION N2
echo             Hackathon Huawei Cloud MaaS / Ascend 910B
echo                    Equipo: Los Ejecutores
echo =====================================================================
echo.
echo Seleccione el sistema que desea iniciar:
echo.
echo [1] Master Video Demo Automatizado (Flujo Completo Intercalado)
echo [2] Panel Principal Hackathon (Pitch + Locucion IA Guiada)
echo [3] Simulador Huawei AICC (Customer Service Cloud + Teleprompter)
echo [4] Simulador BMC Helix ITSM (Remedy + Panel de Actividad N2)
echo [5] Simulador SIAC Unico (Sistema de Gestion de Reclamos Claro)
echo [6] Abrir los 3 sistemas operacionales simultaneamente
echo [0] Salir
echo.
set /p opcion="Ingrese opcion [1-6]: "

if "%opcion%"=="1" goto opc1
if "%opcion%"=="2" goto opc2
if "%opcion%"=="3" goto opc3
if "%opcion%"=="4" goto opc4
if "%opcion%"=="5" goto opc5
if "%opcion%"=="6" goto opc6
if "%opcion%"=="0" goto salir

echo Opcion no valida.
pause
goto salir

:opc1
start "" "%~dp0demo_video_completo.html"
goto salir

:opc2
start "" "%~dp0index.html"
goto salir

:opc3
cd /d "%~dp0AICC"
start "" "index.html"
goto salir

:opc4
cd /d "%~dp0bmc helix"
start "" "index.html"
goto salir

:opc5
cd /d "%~dp0siac unico"
start "" "index.html"
goto salir

:opc6
echo Abriendo los 3 sistemas en pestañas de su navegador...
start "" "%~dp0AICC\index.html"
timeout /t 1 /nobreak >nul
start "" "%~dp0bmc helix\index.html"
timeout /t 1 /nobreak >nul
start "" "%~dp0siac unico\index.html"
goto salir

:salir
exit
