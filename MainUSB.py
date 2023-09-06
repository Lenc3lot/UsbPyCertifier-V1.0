# IMPORTS
import json
import os
import requests
import shutil
from shutil import ignore_patterns
import time
import wmi
from datetime import datetime
from subprocess import Popen

      ############ REQUIERED ############
returnlist = [] # List of file's location
scorelist = [] 
i = 0
j = 0
MaxThreatRate = 25 # % of threat you want to allow on a file, u can change it
certificate = []
bannedextension = [".xltm",".xlam",".xls",".xls",".xlsm",".docm",".dotm",".Point",".dotm",".pot",".potm",".Xlt",".xltm",".ppa",".ppam",".ppsm",".ppt"]
dangerousextenstoscan = [".386",".bat",".bin",".blf",".bll",".bmp",".bmw",".boo",".chm",".cih",".cla",".class",".cmd",".cnm",".com",".cpl",".cxq",".cyw",".dbd",".dev",".dlb",".dll",".dllx",".drv",".eml",".exe",".ezt",".gif",".hlp",".hsq",".hta",".inf",".ini",".iva",".iws",".jpeg",".jpg",".js",".jse",".lnk",".lok",".msc",".msp",".mxq",".oar",".ocx",".osa",".ozd",".pcx",".pdf",".pgm",".php",".php2",".php3",".php4",".php5",".pid",".pif",".plc",".png",".pot",".pr",".ps1",".ps1xml",".ps2",".ps2xml",".psc1",".psc2",".qit",".scf",".scr",".shs",".ska",".smm",".ssy",".swf",".sys",".tif",".tps",".vb",".vba",".vbe",".vbs",".vbx",".vexe",".vsd",".vxd",".wmf",".ws",".wsc",".wsf",".wsh",".wss",".xlm",".xlr",".xlv",".xml",".xnt",".zix",".zvz"]
maxfilesize = 650 # in MB
NbMaxFiles = 20

class compteur:

    def __init__(self,cpte):
        self.cpte = cpte
        print("Compteur initialisé à : "+str(cpte))

    def increment(self):
        self.cpte += 1
    
    def value(self):
        return self.cpte
    
NewCompteur = compteur(0)

############ ----------FUNCTIONS / PROCEDURE---------- ############

                  #    _    #
                  #   | |   #
                  #   | |   #
                  #   | |   #
                  #   | |   #
                  #   | |   #
                  # __| |__ #
                  # \ \_/ / #
                  #  \ V /  #
                  #   \_/   #
        
       ##################################
       # ----------# AVERAGE #----------# 
       # ################################  
          
def Avg(list):
    return sum(list)/len(list)

       ###################################
       # ----------# USB COPY #----------#
       ###################################

def CopyFiles(device,ListePeriph):
    try :
        savepath = "C:/SAVE/Copy of disk " + str(device.Name)[-0]+"/"
        shutil.copytree(device.DeviceID,savepath)
    except :
        print ("Saving repertory is already existing. Creation of a new one and deletion of the older one")
        shutil.rmtree("C:/SAVE/Copy of disk " + str(device.Name)[-0])
        shutil.copytree(device.DeviceID+"/",savepath,ignore=ignore_patterns("System Volume Information"))
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")
    nvElement =  {'IDPeriph':device.DeviceID, 'Desc':device.Description, 'Date':date_string}
    ListePeriph.append(nvElement)
    with open("logs.json","w+") as jsonFile:
        jsonFile.seek(0)
        json.dump(ListePeriph,jsonFile)
        jsonFile.close()


        ######################################################
        # ----------# USB DETECT WTH 1 DISK KNOWN #----------#
        ######################################################

def DetecterCle1(DisqueConnu1):
    #return list of device
    DeviceTab = []

    # New WMI link
    c = wmi.WMI()

    # WMI WIN32 Logical disk object
    usb_devices = c.Win32_LogicalDisk()

    # Return tab for every decives
    ListePeriph = []

    # Foreach loop through all the devices
    i = 0
    for device in usb_devices:
        print("Nom : ", device.Name)
        print("Description : ", device.Description)
        print("Identifiant du périphérique : ", device.DeviceID)

        # If the device connected is different than the known devices then, we add it into a JSON file & we copy it
        if (device.DeviceID != DisqueConnu1+":" and device.Description != "CD-ROM Disc"):
            print("UNKNOW DISK !")
            CopyFiles(device, ListePeriph)
            DeviceTab.append("C:/SAVE/Copy of disk " + str(device.Name)[-0])
        else:
            print("KNOWN DISK")
        print("----")

        i = i+1
    return DeviceTab

        #####################################################
        # ----------# USB DETECT WTH 2 DISK KNOWN #----------#
        #####################################################

def DetecterCle2(DisqueConnu1, DisqueConnu2):
    #return list of device
    DeviceTab = []

    # New WMI link
    c = wmi.WMI()

    # WMI WIN32 Logical disk object
    usb_devices = c.Win32_LogicalDisk()

    # Return tab for every decives
    ListePeriph = []

    # Foreach loop through all the devices
    i = 0
    for device in usb_devices:
        print("Nom : ", device.Name)
        print("Description : ", device.Description)
        print("Identifiant du périphérique : ", device.DeviceID)

        # If the device connected is different than the known devices then, we add it into a JSON file & we copy it
        if (device.DeviceID != DisqueConnu1+":" and device.DeviceID != DisqueConnu2+":" and device.Description != "CD-ROM Disc"):
            print("UNKNOW DISK !")
            CopyFiles(device, ListePeriph)
            DeviceTab.append("C:/SAVE/Copy of disk " + str(device.Name)[-0])
        else:
            print("KNOWN DISK")
        print("----")

        i = i+1
    return DeviceTab
        ######################################################
        # ----------# USB DETECT WTH 3 DISK KNOWN #----------#
        ######################################################

def DetecterCle3(DisqueConnu1, DisqueConnu2, DisqueConnu3):
    #return list of device
    DeviceTab = []

    # New WMI link
    c = wmi.WMI()

    # WMI WIN32 Logical disk object
    usb_devices = c.Win32_LogicalDisk()

    # Return tab for every decives
    ListePeriph = []

    # Foreach loop through all the devices
    i = 0
    for device in usb_devices:
        print("Nom : ", device.Name)
        print("Description : ", device.Description)
        print("Identifiant du périphérique : ", device.DeviceID)

        # If the device connected is different than the known devices then, we add it into a JSON file & we copy it
        if (device.DeviceID != DisqueConnu1+":" and device.DeviceID != DisqueConnu2+":" and device.DeviceID != DisqueConnu3+":" and device.Description != "CD-ROM Disc"):
            print("UNKNOW DISK !")
            CopyFiles(device, ListePeriph)
            DeviceTab.append("C:/SAVE/Copy of disk " + str(device.Name)[-0])
        else:
            print("KNOWN DISK")
        print("----")

        i = i+1
    
    return DeviceTab

        #####################################################
        # ----------# LIST DIRECTORY FOR A DRIVE #----------#
        #####################################################

def ListeDir(dir):

    dir_list = os.listdir(dir)
    try:
        dir_list.remove("System Volume Information")
    except : 
        print("System Volume Information doesn't exist !")
        
    #Nombre de fichiers/dossiers de la clé
    conr = len(dir_list)
    print("Le dossier comporte : "+str(conr)+" fichiers/dossiers")
    print(dir_list)
    print("-----------------------------------------------------------------------------------------------------------------")
    testtab = []
    
    i = 0
    
    for file in dir_list:
        # On ajoute a la table de retour chaque fichier et son extension A L'ENVERS #
        # (test.exe devient => txt.tset)                                            #
        
        testtab.append(dir_list[i][::-1])
        #print("LISTE DE RETOUR : "+str(returnlist))

        # Si on trouve un " . " dans un des éléments du répertoire ALORS #
        # on récupère la châine de caractère jusqu'au point (compris)    #
        # et c'est donc un fichier.                                      #

        if ("." in testtab[i]):
            pointposition = testtab[i].index(".")
            try :
                testtab[i][pointposition+1]
            except : 
                print ("Fichier commencant par un '.', merci de vérifier manuellement !")
                try:
                    newdir = dir+"/"+str(testtab[i][::-1])
                    print("Detection du dossier ' "+ testtab[i][::-1]+ " ' ! ")
                    ListeDir(newdir)
                except :
                    ("C'est un fichier") 
                    returnlist.append(dir+"/"+testtab[i][::-1])
            else:
                print("Une extension existe dans " +testtab[i][::-1])
                print("L'extension est : "+(testtab[i][: pointposition+1])[::-1])
                extension = (testtab[i][: pointposition+1])[::-1]
                j = 0
                for banelem in bannedextension:
                    if (extension == bannedextension[j]):
                        print("Extension interdite ! ARRET DU SCAN !")
                        time.sleep(2)
                        return None
                    j = j+1
                filesize = (round(os.path.getsize(dir+"/"+testtab[i][::-1])/1000000,2))
                if (filesize < maxfilesize):
                    returnlist.append(dir+"/"+testtab[i][::-1])
                    NewCompteur.increment()
                else:
                    print("Fichier trop volumineux !")
                
        # Sinon c'est un répertoire et on change le répertoire et on répète l'opération #

        else:
            print("L'extension n'existe pas dans "+str(testtab[i][::-1])+", c'est un dossier.")
            newdir = dir+"/"+str(testtab[i][::-1])
            ListeDir(newdir)

        i = i+1

    nbFiles = NewCompteur.value()
    print(nbFiles)
    if (nbFiles > NbMaxFiles):
        print("Too Many Files !")
        return False
    return returnlist


        #########################################
        # ----------# ANALYSE API VT #----------#
        #########################################

def Scan(FileName):
    api_key = "" #INSERT YOUR API KEY#
    api_url = "https://www.virustotal.com/vtapi/v2/file/scan"
    pathfile = FileName
    with open(pathfile, 'rb') as file:
        file_data = file.read()
        print(file_data)
    params = {"apikey": api_key}
    response = requests.post(api_url, files={'file': (os.path.basename(pathfile), file_data)}, params=params)
    time.sleep(25)
    if response.status_code == 200:
        json_response = response.json()
        if json_response["response_code"] == 1:

            resource = json_response["resource"]
            print(f"Fichier soumis avec succes. Ressource : {resource}")
            api_url2 = f"https://www.virustotal.com/vtapi/v2/file/report?apikey={api_key}&resource={resource}"
            response2 = requests.get(api_url2)

            if response2.status_code == 200:
                json_response2 = response2.json()
                if json_response2["response_code"] == 1:
                    nbpositif = json_response2["positives"]
                    nbtotal = json_response2["total"]
                    print("Nombre de positif = "+str(nbpositif) +
                          " sur un total de : "+str(nbtotal))
                    score = float((nbpositif/nbtotal)*100)
                    resultat = "Le score de danger du fichier est de : " + \
                        str(round(score, 2))+"%"
                    print(resultat)
                    return score
        else:
            return "Analyse échouée"
    else:
        return "Erreur"


        ###############################################
        # ----------# DELIVER CERTIFICATES #----------#
        ###############################################

def DeliverCertificate(device,trustlvl):
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")
    ts = datetime.timestamp(now)
    exp = datetime.timestamp(now)+3600
    
    nvcerticate = {
        'IDPeriph':device,
        'TrustLvl':trustlvl, 
        'AllowAccess': True, 
        'DelivrationDate': date_string, 
        'DelivrationTimeStamp':ts, 
        'ExpirationTimestamp':exp
    }
    
    json_obj = json.dumps(nvcerticate, indent= 4)
    pathcertif = device+"\certificat.json"
    print (pathcertif)
    with open(pathcertif,"w+") as outfile:
        outfile.write(json_obj)

def  DeliverCertificateESET(device):
    now = datetime.now()
    date_string = now.strftime("%Y-%m-%d %H:%M:%S")
    ts = datetime.timestamp(now)
    exp = ts + 3600
    nvcerticate = {
        'IDPeriph':device, 
        'AllowAccess': True, 
        'DelivrationDate': date_string, 
        'DelivrationTimeStamp':ts, 
        'ExpirationTimestamp':exp 
        }
    json_obj = json.dumps(nvcerticate, indent= 4)
    pathcertif = device+"\certificatEset.json"
    print (pathcertif)
    with open(pathcertif,"w+") as outfile:
        outfile.write(json_obj)


        ####################################
        # ----------# ESET SCAN #----------#
        ####################################

def EsetScan():
    p = Popen("scaneset.bat",cwd=r"C:\PythonUsbCertifier&Disconnecter")
    stdout, stderr = p.communicate()
    time.sleep(2)
    with open(r'C:\PythonUsbCertifier&Disconnecter\esetscanresult\esetscanresult.txt','r') as fd:
        lines = fd.readlines()
        for line in lines:
            if line.find("Detected") != -1:
                print("Detected has been found !")
                print("Line number = ",lines.index(line))
                print("Line = ",line)
                return line


############ ---------- MAIN ---------- ############

nbDisk = int(input("HOW MANY KNOWN DISKS ? "))
tpsdebut =  datetime.now()
print ("Hello "+ str(nbDisk))
if(int(nbDisk) == 1):
    print("KNOWN DISK NAME ")
    DisqueConnuN1 = (input(""))
    DeviceTab = DetecterCle1(DisqueConnuN1)
elif(int(nbDisk) == 2):
    print("KNOWNS DISKS NAMES")
    DisqueConnuN1 = (input(""))
    DisqueConnuN2 = (input(""))
    DeviceTab = (DetecterCle2(DisqueConnuN1,DisqueConnuN2))
elif(int(nbDisk) == 3):
    print("KNOWNS DISKS NAMES")
    DisqueConnuN1 = (input(""))
    DisqueConnuN2 = (input(""))
    DisqueConnuN3 = (input(""))
    DeviceTab = DetecterCle3(DisqueConnuN1,DisqueConnuN2,DisqueConnuN3)
elif(nbDisk == 22525):

    print("*****************")
    print("* ADMIN MODE ON *")
    print("*****************")
    
    #Reglage taille max : 
    rep = input("Redifine the max file size ?[Y/N] (Default = 650MB) :")
    print(rep)

    while (rep !="Y" and rep !="N"):
        print("Incorrect entry, please answer Y or N")
        rep = input("Redifine the max file size ?[Y/N] (Default = 650MB) :")
    
    if(rep=="Y"):
        maxfilesize = int(input("Max file size ? (in MB) [0-650] = "))
        if (maxfilesize >= 650 or maxfilesize <= 0):
            while (maxfilesize >= 650 or maxfilesize <= 0):
                print("Incorrect size ! Please select a correct one.")
                maxfilesize = int(input("Max file size ? (in MB) [0-650] = "))
           
    #NbFichiers max :
    rep = input("Redifine the max file amount ?[Y/N] (Default = 20) :")

    while (rep !="Y" and rep !="N"):
        rep = input("Redifine the max file amount ?[Y/N] (Default = 20) :")

    if(rep == "Y"):
        NbMaxFiles = int(input("Max files amount ? = "))
        if (NbMaxFiles >= 20 or NbMaxFiles <=0):
            print("Incorrect entry ! Please answer a correct one.")
            NbMaxFiles = int(input("Max files amount ? = "))

    print("Changements done !")

    nbDisk = int(input("HOW MANY KNOWN DISKS ? "))

    if(nbDisk == 1):
        print("KNOWN DISK NAME ")
        DisqueConnuN1 = (input(""))
        DeviceTab = DetecterCle1(DisqueConnuN1)
    elif(nbDisk == 2):
        print("KNOWNS DISKS NAMES")
        DisqueConnuN1 = (input(""))
        DisqueConnuN2 = (input(""))
        DeviceTab = (DetecterCle2(DisqueConnuN1,DisqueConnuN2))
    elif(nbDisk == 3):
        print("KNOWNS DISKS NAMES")
        DisqueConnuN1 = (input(""))
        DisqueConnuN2 = (input(""))
        DisqueConnuN3 = (input(""))
        DeviceTab = DetecterCle3(DisqueConnuN1,DisqueConnuN2,DisqueConnuN3)


for disk in DeviceTab:
    PathFiles = (ListeDir(DeviceTab[i]))
    fp=open("logs.json")
    data=json.load(fp)
    for element in data:
            periph = element['IDPeriph']

    if (PathFiles == None):
        print("Fichier non voulu, début scan ESET")
        resultScan = []
        resultScan.append(EsetScan())
        if ("-" in resultScan[0]):
            pos = resultScan[0][resultScan[0].index("-")+2]
            print (pos)
            if (pos != "0"):
                print("Fichier dangereux détecté ! Clé non autorisée")
                quit()
            else:
                print("USB authorized after the ESET SCAN !")
                DeliverCertificateESET(periph)
    else :
        print("*********************************************** "+DeviceTab[i])
        j = 0
        for files in PathFiles:
            print("TESTING FILE : "+PathFiles[j])
            time.sleep(25)
            score = Scan(PathFiles[j])
            ScoreFile = score
            scorelist.append(ScoreFile)
            print (scorelist)
            time.sleep(2)
            if (ScoreFile > 100):
                print(" DANGEROUS FILE ! THIS DEVICE WILL NOT BE ALLOWED TO CONNECT ON OTHER COMPUTER. THIS PROGRAMM WILL SHUT DOWN")
                time.sleep(1) 
                quit()
            j = j+1
            print("NEXT FILE ->")

        average = round(Avg(scorelist),2)

        if(average >= 0):
            DeliverCertificate(periph, average)
            print("CERTIFICAT DELIVERED")

        print("ESET SCAN IS STARTING !")

        resultScan = []
        resultScan.append(EsetScan())
        
        if ("-" in resultScan[0]):
            pos = resultScan[0][resultScan[0].index("-")+2]
            print (pos)
            if (pos != "0"):
                print("Fichier dangereux détecté ! Clé non autorisée")
                quit()
            else:
                print("USB autorisé  après the ESET SCAN !")
                DeliverCertificateESET(periph)
        i = i+1



datefni = datetime.now()
tps = datefni-tpsdebut
print(tps)
shutil.rmtree("C:\SAVE")
os.remove("C:\PythonUsbCertifier&Disconnecter/esetscanresult/esetscanresult.txt")