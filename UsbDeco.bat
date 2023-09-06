
@echo off
setlocal enabledelayedexpansion

REM Récupérer le PNPDeviceID de la clé USB
set "deviceID="
for /f "usebackq tokens=1,2,3" %%i in (`wmic diskdrive get PNPDeviceID ^| find "USBSTOR"`) do (
    set "deviceID=%%i"
)

@REM Vérifier si le PNPDeviceID a été récupéré
if defined deviceID (
    echo PNPDeviceID de la cle USB : !deviceID!
    echo.
    
    @REM Désinstaller le périphérique par PNPDeviceID
    pnputil /remove-device "!deviceID!"
    pause
    exit
) else (
    echo Aucune clé USB trouvée.
)