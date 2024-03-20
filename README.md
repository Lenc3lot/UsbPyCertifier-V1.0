

                                                                                                                      
                                                                                                                      
    ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______   
  _|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|_ 
 | |  |  __ \          | |   | |                 | |  | |/ ____|  _ \ / ____|        | | (_)/ _(_)                 | |
 | |  | |__) |  _   _  | |_  | |__   ___  _ __   | |  | | (___ | |_) | |     ___ _ __| |_ _| |_ _  ___ _ __        | |
 | |  |  ___/  | | | | | __| | '_ \ / _ \| '_ \  | |  | |\___ \|  _ <| |    / _ \ '__| __| |  _| |/ _ \ '__|       | |
 | |  | |      | |_| | | |_  | | | | (_) | | | | | |__| |____) | |_) | |___|  __/ |  | |_| | | | |  __/ |          | |
 | |  |_|       \__, |  \__| |_| |_|\___/|_| |_|  \____/|_____/|____/ \_____\___|_|   \__|_|_| |_|\___|_|          | |
 | |             __/ |                                                                                             | |
 |_|______ _____|___/___ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______ ______|_|
   |______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|______|  

          __        ___  
         /_ |      / _ \ 
 __   __  | |     | | | |
 \ \ / /  | |     | | | |
  \ V /   | |  _  | |_| |
   \_/    |_| (_)  \___/ 
                         
Credits:

-> PythonUSBCertifier V1.0
-> Using Python3.11 (AT LEAST)
-> VirusTotal API v3
-> Made for @SFEC COMPUSHIP - https://compuships.fr/

------------------------------------------                                                                   
                                                                                        
                                            ██                                          
                                          ██░░██                              
                                        ██░░░░░░██                               
                                      ██░░░░░░░░░░██                                    
                                      ██░░░░░░░░░░██                                    
                                    ██░░░░░░░░░░░░░░██                                  
                                  ██░░░░░░██████░░░░░░██                                
                                  ██░░░░░░██████░░░░░░██                                
                                ██░░░░░░░░██████░░░░░░░░██                              
                                ██░░░░░░░░██████░░░░░░░░██                              
                              ██░░░░░░░░░░██████░░░░░░░░░░██                            
                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          
                            ██░░░░░░░░░░░░██████░░░░░░░░░░░░██                          
                          ██░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░██                        
                          ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                        
                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      
                        ██░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██                      
                      ██░░░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░░░██                    
                      ██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██                    
                        ██████████████████████████████████████████                      



          _____  ____   ____  _____     _______ ____      _  ___   _  ______          __
         / ____|/ __ \ / __ \|  __ \   |__   __/ __ \    | |/ / \ | |/ __ \ \        / /
        | |  __| |  | | |  | | |  | |     | | | |  | |   | ' /|  \| | |  | \ \  /\  / / 
        | | |_ | |  | | |  | | |  | |     | | | |  | |   |  < | . ` | |  | |\ \/  \/ /  
        | |__| | |__| | |__| | |__| |     | | | |__| |   | . \| |\  | |__| | \  /\  /   
         \_____|\____/ \____/|_____/      |_|  \____/    |_|\_\_| \_|\____/   \/  \/                                                                               
                                                                                 
         -------------------------------------------------------------------------------
        This program got some pre-requirement, u will find bellow the different steps to ensure a well working.                                                     
                                                                                      
STEP 1 : 
        
        Please be sure that you have installed python3 (v3.11 at least) (foundable on the Microsoft Store) on your computer and the followings         
        librairies :                                                                                           
               -> json                                                                
               -> wmi                                                                 
               -> os                                                                  
               -> requests                                                            
               -> shutil                                                              
               -> time                                                                
               -> datetime                                                            
        If those librairies are not installed, run a python cmd and type "pip install [librairieName]"                                               
                                                       
                                              
[STEP 2 (FOR AUTOMATIC EXECUTION) WHEN USB PLUGGED] : 
        
        Go to the Task Scheduler and create a new Task. Create a new trigger and select " On an event" for the 
        beggining of the task. Then you have to select the "Microsoft-Windows-DriverFrameworks-UserMode_Operational" Log and "DriverFramework-UserMode" for the source.
        
        FOR THE EVENT ID YOU WILL HAVE TO USE THE ID 2101 WICH CORRESPONDS WITH THE LAST EVENT LOGGED WHEN A USB DRIVE IS PLUGGED
        
        After that, go to the "Action" page, and create a new one, select "Start a program" and chose the "run.bat" file, in the C:\PythonUSBCertifier folder.

        Then go back to the "General" section and select the option " Run with highest privilege " 

        

        RECAP : 
            -> Log : "Microsoft-Windows-DriverFrameworks-UserMode_Operational"
            -> Source : "DriverFramework-UserMode"
            -> Event ID : 2101
        
Miscellaneous : 

    -> Please be sure to have a VirusTotal account and put your API key in the MainUSB.py file
    -> Also, please know that you will have some quota with the free version of VirusTotalAPI (find more on https://www.virustotal.com/gui/my-apikey)
    -> You can put the MainUSB.py file and the run.bat script
 
                                                                                                        
                                                                                                        



                                                         

                                                                                                                     
                                                                                                                      


