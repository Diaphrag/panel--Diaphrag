class color : 
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'

    
#Coded by Diaphrag
import requests
import os
import time

def clear_console():
    if os.name in ('nt', 'dos'): 
        try:
            os.system("cls")
        except:
            pass
    else:
        try:
            os.system("clear")
        except:
            pass
def change_title():
    if os.name in ('nt', 'dos'):
        try:
            os.system('title "Diaphrag [!] Admin Panel Search"')
        except:
            pass
    else:
            pass


clear_console()
change_title()



Diaphrag = color.Red+"""

                                            ____  _             _                     
                                           |  _ \(_) __ _ _ __ | |__  _ __ __ _  __ _ 
                                           | | | | |/ _` | '_ \| '_ \| '__/ _` |/ _` |
                                           | |_| | | (_| | |_) | | | | | | (_| | (_| |
                                           |____/|_|\__,_| .__/|_| |_|_|  \__,_|\__, |
                                                         |_|                    |___/ 
 

"""

banner =color.Green+ f"""
[!] Coded By Diaphrag

       '||''|.    ||                   '||                              
        ||   ||  ...   ....   ... ...   || ..   ... ..   ....     ... . 
        ||    ||  ||  '' .||   ||'  ||  ||' ||   ||' '' '' .||   || ||  
        ||    ||  ||  .|' ||   ||    |  ||  ||   ||     .|' ||    |''   
       .||...|'  .||. '|..'|'  ||...'  .||. ||. .||.    '|..'|'  '||||. 
                               ||                               .|....' 
                              ''''                                      

"""


def slowprint(text: str, speed: float, newLine=True):
    for i in text:
        print(i, end="", flush=True)
        time.sleep(speed)
    if newLine:
        print()

print(Diaphrag)
time.sleep(5)
clear_console()
print(banner)
time.sleep(1)
slowprint(color.Red+"\n\n                   [!] Coded By Diaphrag\n",0.07)
slowprint(color.Green+"                 [!] Search Admin Panel!\n",0.07)

URL = str(input(color.Red+f"[+] Send Me Your link! [Example ---> https://google.com ] : {color.Green}")).strip()

print(color.Red+"\n[+] Searching Admin Pandel <-->   : "+color.Green+URL)
time.sleep(2)
slowprint(color.Red+"      ----> wait! IM Search To Admin Login par...",0.07)
with open("Diaphrag.txt","r",encoding="UTF-8") as words:
    for word in words.readlines():
        adminpage = URL+"/"+word.strip("\n")
        try:
            rq = requests.get(adminpage)
        except Exception as e:
            print(color.Red+"\n[!] Errored  "+e)
        if rq.status_code == 200:
            prin
            with open("Diaphrag-admin.txt",'a',encoding="UTF-8") as admin:
                admin.writelines(adminpage+"\n")
  
input(color.Red+"\n[+]  Press ( enter )to exit---> ")

