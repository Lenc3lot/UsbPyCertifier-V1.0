@echo off
setlocal enabledelayedexpansion 
@REM Récupérer le nom du lecteur amovible 
set "driveName=" 
for /f "usebackq skip=1 delims= " %%j in (`wmic logicaldisk where "DriveType=2" get Name `) do (
    set "driveName=%%j" 
    goto :Next ) 
     
:Next 
@REM Vérifier si le nom du lecteur amovible a été récupéré 
if defined driveName (
    echo Nom du lecteur amovible : !driveName!
    cd "C:\Program Files\ESET\ESET Security"
    set "result="
    for /f "usebackq tokens=1 delims=" %%i in (`ecls /log-file=C:\PythonUsbCertifier&Disconnecter\esetscanresult\esetscanresult.txt !driveName! ^| find "Detected"`) do (
        set "result=%%i"
        echo !result!
    )
    echo !result!>esetscanresult.txt

) else ( 
    echo Aucun lecteur amovible trouvé.
)

endlocal