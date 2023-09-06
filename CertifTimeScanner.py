import json
import wmi
import time
from subprocess import Popen
from datetime import datetime


# New WMI link
c = wmi.WMI()

# WMI WIN32 Logical disk object
usb_devices = c.Win32_LogicalDisk()

# Foreach loop through all the devices
i = 0
for device in usb_devices:
    print("Nom : ", device.Name)
    print("Description : ", device.Description)
    print("Identifiant du périphérique : ", device.DeviceID)

    if(device.Description == "Removable Disk"):
        
        with open(device.Name+"\certificatEset.json",'r') as f:
                data = f.read()
        print (data)

        obj = json.loads(data)

        exptsmt = obj["ExpirationTimestamp"]

        now = datetime.now()

        ts = datetime.timestamp(now)

        if(ts > exptsmt):
            print("TEMPS ECOULE !")
            p = Popen("UsbDeco.bat",cwd=r"C:\Users\BRIDGE\Desktop\USB19-06\BACKUP")
            stdout, stderr = p.communicate()
        else : 
            print("ok")

    i = i+1


