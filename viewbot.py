import requests
import time
import os
import signal
from printy import inputy
from printy import printy 
import colorama
from pathlib import Path
import webbrowser
import ctypes
import hashlib
import subprocess
import re
from colorama import Fore, init
import httpx

ctypes.windll.kernel32.SetConsoleTitleW("Bad Boy ViewBot | MushMash @ Nulled.To")

AUTHFILE = Path('authkey.txt')

def _auth():
    if AUTHFILE.exists():
        loaded_from_file = True
        with AUTHFILE.open() as f:
            key = f.read()
    else:
        key = input('Enter your auth key: ')
        loaded_from_file = False
        with AUTHFILE.open('w') as f:
            f.write(key)

    req = httpx.get('https://www.nulled.to/misc.php', params={
        'action': 'validateKey',
        'authKey': hashlib.md5(key.encode('utf-8')).hexdigest()
    })

    json = req.json()
    if json['status'] == 'success':
        print(f'{Fore.GREEN}Welcome {json["username"]} {Fore.RESET}({json["uid"]})')

    else:
        os.remove(AUTHFILE)
        if loaded_from_file:
            print(f'{Fore.RED}The previous valid key became invalid.{Fore.RESET}')
        else:
            print(f'{Fore.RED}Invalid key.{Fore.RESET}')

        print('Get one from https://nulled.to/auth.php')

        exit()


_auth()

os.system('cls')

def view():
    printy(f"╔══════ ≪ °❈° ≫ ══════╗", "b>B") 
    printy(f" ")
    printy(f"   Mushmash's Viewbot", "rB")
    printy(f" ")
    printy(f"╚══════ ≪ °❈° ≫ ══════╝", "b>B")
    printy
    printy(f" ")
    

    listingURL = inputy(" Enter Link : ", "rB")
    os.system('cls')

    printy(f"╔══════ ≪ °❈° ≫ ══════╗", "b>B")
    printy(f" ")
    printy(f"   Mushmash's Viewbot", "rB")
    printy(f" ")
    printy(f"╚══════ ≪ °❈° ≫ ══════╝", "b>B")
    printy
    printy(f" ")
    printy(f" \[          0%\] Testing Link","nB")    
    time.sleep(1)
    os.system('cls')
    
    printy(f"╔══════ ≪ °❈° ≫ ══════╗", "b>B")
    printy(f" ")
    printy(f"   Mushmash's Viewbot", "rB")
    printy(f" ")
    printy(f"╚══════ ≪ °❈° ≫ ══════╝", "b>B")
    printy
    printy(f" ")
    printy(f" \[==        15%\] Testing Link","nB")    
    time.sleep(1)
    os.system('cls')

    printy(f"╔══════ ≪ °❈° ≫ ══════╗", "b>B")
    printy(f" ")
    printy(f"   Mushmash's Viewbot", "rB")
    printy(f" ")
    printy(f"╚══════ ≪ °❈° ≫ ══════╝", "b>B")
    printy
    printy(f" ")
    printy(f" \[=====     45%\] Testing Link","nB")    
    time.sleep(1)

    os.system('cls')

    printy(f"╔══════ ≪ °❈° ≫ ══════╗", "b>B")
    printy(f" ")
    printy(f"   Mushmash's Viewbot", "rB")
    printy(f" ")
    printy(f"╚══════ ≪ °❈° ≫ ══════╝", "b>B")
    printy
    printy(f" ")
    printy(f" \[========  70%] Testing Link","nB")    
    time.sleep(1)

    os.system('cls')    
    
    printy(f"╔══════ ≪ °❈° ≫ ══════╗", "b>B")
    printy(f" ")
    printy(f"   Mushmash's Viewbot", "rB")
    printy(f" ")
    printy(f"╚══════ ≪ °❈° ≫ ══════╝", "b>B")
    printy
    printy(f" ")
    
    viewCount = int(inputy(" Enter Views : ", "rB"))
    printy(f" ")
    printy
    
    os.system('cls') 

    printy(f"╔══════ ≪ °❈° ≫ ══════╗", "b>B")
    printy(f" ")
    printy(f"   Mushmash's Viewbot", "rB")
    printy(f" ")
    printy(f"╚══════ ≪ °❈° ≫ ══════╝", "b>B")
    printy
    printy(f" ")


    os.system('cls')
    printy(f" \[=\] Sending views! ","nB")  
    printy(f" ")
    printy(f" \[!\] Do not close this window \[!\] ","rB") 
    print
    start_time = time.time()
    for i in range(viewCount):
        r = requests.get(listingURL)
        
    os.system('cls')
    printy(f" \[+\] Views Sent! ","nB")
    printy(f" ","nB")
    printy(f" Thanks For Using my Awesome Viewbot <3 ","nB")

    
 


if __name__ == '__main__':
  view()

ctypes.windll.user32.MessageBoxW(0, "Views Sent!", "Bad Boy Viewbot", 1)
os.kill(os.getppid(), signal.SIGTERM)