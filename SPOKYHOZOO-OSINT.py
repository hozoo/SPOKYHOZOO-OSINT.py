import googlesearch
from googlesearch import search
import requests
import time
from os.path import exists
import os
import random
import re
import argparse
import urllib
global user_agents
user_agents = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36']

if os.name == 'posix':  # Untuk sistem seperti Linux atau macOS
    os.system('clear')
elif os.name == 'nt':   # Untuk sistem Windows
    os.system('cls')
yellow = '\033[1;33m'
blue = '\033[1;34m'
green = '\033[1;32m'
red = '\033[1;91m'
print(f"""
.,,.
                                                                            ..  ;kOc
                                                                             ...'dOx
                                                                            '.,,,lOO
                                                                           .';,c:okO
                                                              .         .. .';;l:lkO
                                                   .          .     .   .,' .,;:clxO
                                                  ..         . .     '   ,;.....l,xO
                                                 ,..        .. ...   ..  ';,..  ';lO
                        ...                    .;:'         . ....   ..  .;;..  .,'k
                                              .,::'       .. ...'.       .,...   '.o
                                            .;.:::.      .   ..',         .     .. '
                       .....               .:''::,     ..    ..;,               .
                       ...               .'::.::,    ..      .,:'   .
     .                            ..    .;::.,:'  ..        .,;:.  ..
     .                      .......  .,;;::.':..,.          .,::. .,.
   . ..     ...       ....',,;,..  ......'.''.':'         ..,;:,  ,;.
  . .;,      ..             ....;,;;;;,.     .'.         ..;;:;  .:,.
    .,,   .  ..       ....  .'    .',,,,..;;'.          ..;;:,   '..
 ....''  .'. '.....,;:;:::;cO,'..'.  .'.'''.        ....,;,'.  .....               .
 ,;,.;; .;,. .......';;,:loodoldlcc:....''.........'',,;,''''....               .. .
 ','':; .;,. .      .',,,,:::cccccc:;;;;;:::;;;::::::;,;,.. . .                 ''.
    .;;..;,'.        ',:::cc;;;;;;:::::::::::::::::;;,;;:kcc:,cc;',..           .'.
    .;;. ;;,.. .    .';;:::::::::::::::::::::::::::::,coollllll::o....         ..  .
     ,;. ;;;.. .     ';,:::::::::::::::::::::::::::::::c:::;;,..:.           ..   'o
     .;. ';;,. .     .;;;:::::::::::::::::::::::::::::::::;,,,;c.            ..  ;:c
.     '. .;;;..      .;:;;:::::::::::::::::::::::ccc:::::::::co.             .'  ;ld
.      . ..;;;.      ..::;;::::::::::::::::::::::cxdcc::::::lx,              ..' .xo
 .    .. , .;;,..    ..':::;::::::::::::::::::::::okdc:::::ok;               .,'. ld
      .  .' ';,..    .'',:::;:::::::::::::::::::c:lkoc:::cdk:                .'c'..d
       .  .  ';'..   ..;',:::;;:::::::::::::::;;;;cccc::lxk,                  ;o:'.c
       .  ..  .'.'   ..,;''::::;:::::::::::::::c:::::::okd.        .        . lld:..
               ....   ..;;..::::;;::::::::::::::::::clxx,          .,        .'ddol'
                 ..   . '::,.;;:::;;;;,;;;;;:::cccccdd,            'c'       .'odxoo
                       . ;::;.,;'',,,,,''';c;ccclll:.               ,o.       .:kxxo
                       .  ;::;..;;;;;;co:cllllll;.                  .:l.       'dkxx
                        .  ;:::..,;,,;;ldoool;.            .        ..lc.       ;kxx
                            ;:::..,::clllc;'      .                 .;.o:.       ;xd
                             ':::.';clc,......    .......           .;c'd;...     ;x
                               ..'.,;'...........  :...  .......  ...,ol,o;....    ,
                                      .............c;................;:xo,l;........
                                       ..........  :c...  ..  ........;llc.c......⠀⠀
{red}
██╗░░██╗░█████╗░███████╗░█████╗░░█████╗░
██║░░██║██╔══██╗╚════██║██╔══██╗██╔══██╗  
███████║██║░░██║░░███╔═╝██║░░██║██║░░██║ 
██╔══██║██║░░██║██╔══╝░░██║░░██║██║░░██║
██║░░██║╚█████╔╝███████╗╚█████╔╝╚█████╔╝
╚═╝░░╚═╝░╚════╝░╚══════╝░╚════╝░░╚════╝░

                                                                 
{blue}
Methods :
Email, Phone Numbers, Full Name
Select Mode:
1. Email
2. Phone Numbers
3. Full Name
""")
ans = input(" : ")
if ans == ("3"):
    try:
        fn = input(f"Full Name Target : ")
        print(f"{yellow}[ + ] Finding For {fn} In Google Dorking.. [ + ]")
        time.sleep(1)
        for fn in search(f'intext:{fn}', tld='com', num=1, start=0, stop=None, pause=2):
            keyword = ["Location", "Gmail", "Phone Numbers", "Full Name", "Address", "Data", "Password", "Username"]
            response = requests.get(fn)
            print(f"{blue} [ + ] Successfully Finding Data For {fn} [ + ]")
            print(green + fn)
            for i in keyword:
                if i in response.text:
                    print(f"[ + ] Columns Name {i} On {fn} Its Exists ! [ + ]")
                else:
                    print(f"{blue}[ + ] Finding... For {i}[ + ]")
        print(green + f"[ + ] Kerosint Done.. [ + ]")
    except KeyboardInterrupt:
        print("Interrupt Detected, Exiting")
        exit()
    except TimeoutError:
        print("timed out while finding victim data..")
    except ValueError:
        print(f"{red}[ + ] Value Error Detected !! [ + ]")
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print(f"Wh00pz ! E 429, Please Wait 10 Sec..")
            time.sleep(10)
if ans == ("1"):
    try:
        fn = input(f"Email Target : ")
        print(f"{yellow}[ + ] Finding For {fn} In Google Dorking.. [ + ]")
        time.sleep(1)
        for fn in search(f'intext:{fn}', tld='com', num=1, start=0, stop=None, pause=2):
            keyword = ["Location", "Gmail", "Phone Numbers", "Full Name", "Address", "Data", "Password", "Username"]
            response = requests.get(fn)
            print(f"{blue} [ + ] Successfully Finding Data For {fn} [ + ]")
            print(green + fn)
            for i in keyword:
                if i in response.text:
                    print(f"[ + ] Columns Name {i} On {fn} Its Exists ! [ + ]")
                else:
                    print(f"{blue}[ + ] Finding... For {i}[ + ]")
        print(green + f"[ + ] Kerosint Done.. [ + ]")
    except KeyboardInterrupt:
        print("Interrupt Detected, Exiting")
        exit()
    except TimeoutError:
        print("timed out while finding victim data..")
    except ValueError:
        print(f"{red}[ + ] Value Error Detected !! [ + ]")
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print(f"Wh00pz ! E 429, Please Wait 10 Sec..")
            time.sleep(10)
if ans == ("2"):
    try:
        fn = input(f"Full Phone Num Target : ")
        print(f"{yellow}[ + ] Finding For {fn} In Google Dorking.. [ + ]")
        time.sleep(1)
        for fn in search(f'intext:{fn}', tld='com', num=1, start=0, stop=None, pause=2):
            keyword = ["Location", "Gmail", "Phone Numbers", "Full Name", "Address", "Data", "Password", "Username"]
            response = requests.get(fn)
            print(f"{blue} [ + ] Successfully Finding Data For {fn} [ + ]")
            print(green + fn)
            for i in keyword:
                if i in response.text:
                    print(f"[ + ] Columns Name {i} On {fn} Its Exists ! [ + ]")
                else:
                    print(f"{blue}[ + ] Finding... For {i}[ + ]")
        print(green + f"[ + ] Kerosint Done.. [ + ]")
    except KeyboardInterrupt:
        print("Interrupt Detected, Exiting")
        exit()
    except TimeoutError:
        print("timed out while finding victim data..")
    except ValueError:
        print(f"{red}[ + ] Value Error Detected !! [ + ]")
    except urllib.error.HTTPError as e:
        if e.code == 429:
            print(f"Wh00pz ! E 429, Please Wait 10 Sec..")
            time.sleep(10)