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
) else (
    echo Aucune clé USB trouvée.
)

@REM Récupérer le nom du lecteur amovible 
set "driveName=" 
for /f "usebackq skip=1 delims= " %%j in (`wmic logicaldisk where "DriveType=2" get Name `) do (
    set "driveName=%%j" 
    goto :Next ) 
     
:Next 
@REM Vérifier si le nom du lecteur amovible a été récupéré 
if defined driveName (
    echo Nom du lecteur amovible : %driveName%
    @REM Check si les 2 certificats sont présents, si oui, va vérifier avec script py leur tmstp d'expiration
    if exist %driveName%/certificat.json goto scanTime
    
    
    echo "hello"
    pnputil /remove-device "!deviceID!"
    

    :scanTime
    python CertifTimeScanner.py 
    if exist %driveName%/certificatEset.json goto scanTime2

    

    :scanTime2
    python CertifTimeScanner.py 
    goto endexit


) else ( 
    echo Aucun lecteur amovible trouvé.
)


:endexit
pause

endlocal

