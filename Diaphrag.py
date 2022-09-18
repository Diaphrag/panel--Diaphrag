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
                
print(Fore.Green+ "")
x = """


____________$$$$$$$$$$
____________$$$$$$$$$$$
_____________$$$$$$$$$
_____$$$$$$_____$$$$$$$$$$
____$$$$$$$$__$$$$$$_____$$$
___$$$$$$$$$$$$$$$$_________$
___$$$$$$$$$$$$$$$$______$__$
___$$$$$$$$$$$$$$$$_____$$$_$
___$$$$$$$$$$$__________$$$_$_____$$
____$$$$$$$$$____________$$_$$$$_$$$$
______$$$__$$__$$$______________$$$$
___________$$____$_______________$
____________$$____$______________$
_____________$$___$$$__________$$
_______________$$$_$$$$$$_$$$$$
________________$$____$$_$$$$$
_______________$$$$$___$$$$$$$$$$
_______________$$$$$$$$$$$$$$$$$$$$
_______________$$_$$$$$$$$$$$$$$__$$
_______________$$__$$$$$$$$$$$___$_$
______________$$$__$___$$$______$$$$   Diaphrag Hear
______________$$$_$__________$$_$$$$
______________$$$$$_________$$$$_$_$
_______________$$$$__________$$$__$$
_____$$$$_________$________________$
___$$$___$$______$$$_____________$$
__$___$$__$$_____$__$$$_____$$__$$
_$$____$___$_______$$$$$$$$$$$$$
_$$_____$___$_____$$$$$_$$___$$$
_$$_____$___$___$$$$____$____$$
__$_____$$__$$$$$$$____$$_$$$$$
__$$_____$___$_$$_____$__$__$$$$$$$$$$$$
___$_____$$__$_$_____$_$$$__$$__$______$$$
____$$_________$___$$_$___$$__$$_________$
_____$$_$$$$___$__$$__$__________________$
______$$____$__$$$____$__________________$
_______$____$__$_______$$______________$$
_______$$$$_$$$_________$$$$$$$__$$$$$$

              Coded by Diaphrag
"""
for c in x:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.003)


input(color.Red+"\n[+]  Press ( enter )to exit---> ")

