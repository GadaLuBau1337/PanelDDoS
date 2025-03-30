import os
import pathlib
import sys
import shutil
import threading
import subprocess
import shlex
import json
import stat
import requests
import signal
import subprocess
import time
import sys
import traceback
import time
import datetime
current_time = datetime.datetime.now()
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

def clear(kiohana):
    print ("Clear 😁, Bye")
    sys.exit()

class Color:
    def blue(): return '\033[94m'
    def green(): return '\033[92m'
    def yellow(): return '\033[93m'
    def red(): return '\033[91m'
    def reset(): return '\033[0m'
    def bg_green(i=""): return '\x1b[6;30;42m' + str(i) + '\x1b[0m'

class bin:
    def is_dir(dir): return pathlib.Path(dir).is_dir()
    def is_file(file): return pathlib.Path(file).is_file()
    def touch(file): return pathlib.Path(file).touch()
    def err(e): print("{}: missing operand".format(e))
    def title(): os.system("title Shell") if os.name == 'nt' else os.system("")
    def owner_group(file):
        if os.name == 'nt':
            return ""
        return "{}\t{}".format(pathlib.Path(file).owner(),pathlib.Path(file).group())
    def shell_split(cmd=""):
        if os.name == 'posix': return shlex.split(cmd)
        else:
            if not cmd: return []
            return json.loads(subprocess.check_output('{} {}'.format(subprocess.list2cmdline([sys.executable, '-c', 'import sys, json; print(json.dumps(sys.argv[1:]))']), cmd)).decode())
    def chmod(file,chmod_per=9999,is_chmod=1):
        if bin.is_file(file) and bin.is_dir(file):
            print("chmod: cannot access '{}': No such file or directory".format(file))
        elif is_chmod == 0:
            return eval("stat.filemode({})".format(oct(os.stat(file).st_mode)))
        elif chmod_per == 9999:
            print("chmod: missing operand after '{}'".format(file))
        elif len(chmod_per)>3 or len([str(char) for char in str(chmod_per) if int(char)<=7]) != 3:
            print("chmod: invalid mode: '{}'".format(chmod_per))
            return
        os.chmod(str(file),int(chmod_per))

#Fungsi untuk meminta input username dan password
def login():
    while True:
        username = input(f"\033[92mMasukkan \033[93musername:\033[94m ")
        password = input(f"\033[92mMasukkan \033[93mpassword:\033[94m ")
        username_benar = "admin"
        password_benar = "don't sell bitch"
        if username == username_benar and password == password_benar:
            print(f"\033[92mLogin berhasil!")
            time.sleep(5)
            break
        else:
            print(f"\033[91mUsername atau password salah. Coba lagi!")
            time.sleep(5)
login()

def menu():
        print("\nWelcome To Sonic Panel")
        print(f'''
\033[92m__Building__Author__  : \033[93m@GadaLuBau
\033[92m__Collaborative__Author : \033[93m@Valen
\033[92m__Shell__Author : \033[93m @GadaLuBau X Valen
\033[92m__Total__User__Access__ : \033[93m[ 192 ]
           ''')

def Help():
    print('''
      \x1b[38;2;59;241;250m ソ\033[94mニ\x1b[38;2;224;0;142mッ\x1b[38;2;224;0;042m・\x1b[38;2;124;0;342mクパ・ネルHelp.                                    
            \033[94m—   \x1b[38;2;0;255;189mLa\033[94myer\033[92m7    
            \033[94m—   \x1b[38;2;0;255;189mLa\033[94myer\033[92m4
   ''')

def handler(sig, frame):
    file_path = "ㅤ"
    os.remove(file_path)
    print("\nBye Bye 😒")
    sys.exit(0)
def set_terminal_title(title):
    sys.stdout.write(f"\x1b]2;{title}\x07")


def Layer7():
	print('''
               \x1b[38;2;59;241;250m ソ\033[94mニ\x1b[38;2;224;0;142mッ\x1b[38;2;224;0;042m・\x1b[38;2;124;0;342mクパ・ネルMethods.                                    
            \033[94m—   \x1b[38;2;0;255;189mTls  \033[94m  — \033[92m  Null   \033[94m —   \033[93mNull    
            \033[94m—   \x1b[38;2;0;255;189mNull \033[94m  — \033[92m  Null  \033[94m  —   \033[93mNull 
            \033[94m—   \x1b[38;2;0;255;189mNull \033[94m  — \033[92m  Null   \033[94m —   \033[93mNull     
            \033[94m—   \x1b[38;2;0;255;189mNull \033[94m  — \033[92m  Null   \033[94m —   \033[93mNull     
            \033[94m—   \x1b[38;2;0;255;189mNull \033[94m  — \033[92m  Null   \033[94m —   \033[93mNull       
   ''')
def Layer4():
	print('''
               \x1b[38;2;59;241;250m ソ\033[94mニ\x1b[38;2;224;0;142mッ\x1b[38;2;224;0;042m・\x1b[38;2;124;0;342mクパ・ネルMethods.                                    
            \033[94m—   \x1b[38;2;0;255;189mUdp  \033[94m  — \033[92m  Null   \033[94m —   \033[93mNull    
            \033[94m—   \x1b[38;2;0;255;189mSamp \033[94m  — \033[92m  Null  \033[94m  —   \033[93mNull 
            \033[94m—   \x1b[38;2;0;255;189mNull \033[94m  — \033[92m  Null   \033[94m —   \033[93mNull     
            \033[94m—   \x1b[38;2;0;255;189mNull \033[94m  — \033[92m  Null   \033[94m —   \033[93mNull     
            \033[94m—   \x1b[38;2;0;255;189mNull \033[94m  — \033[92m  Null   \033[94m —   \033[93mNull       
   ''')

def main():
       menu()
       while(True):
        cnc = input(f"""\x1b[38;2;239;239;239m┏━━[\x1b[38;2;255;99;71mPanel\x1b[38;2;239;239;239m] - [\x1b[38;2;255;234;0msonic\x1b[38;2;239;239;239m]\n\x1b[38;2;239;239;239m┗━━➤ """)
        if cnc == "Help":
            Help()
        elif cnc == "Layer7":
             Layer7()
        elif cnc == "Layer4":
            Layer4()
        elif cnc == "Author":
            Author()
        elif cnc == "Rank":
            Rank()
        elif cnc =="Clear":
            Clear()
        elif cnc =="Exit":
             Exit()

#layer4
        elif "Udp" in cnc:
              try:
                    ip=cnc.split()[1]
                    port=cnc.split()[2]
                    packet=cnc.split()[3]
                    threads=cnc.split()[4]
                    times=cnc.split()[5]
                    os.system(f"python udp.py {ip} {port} {packet} {threads} {times}")
              except IndexError:
                    print("Usage : udp <ip> <port> <packet> <threads> <times>")
                    print("Example : udp 127.0.0.1:53 60")
        elif "Samp" in cnc:
              try:
                    ip=cnc.split()[1]
                    port=cnc.split()[2]
                    choice=cnc.split()[3]
                    times=cnc.split()[4]
                    threads=cnc.split()[5]
                    os.system(f"python samp.py {ip} {port} {choice} {times} {threads}")
              except IndexError:
                    print("Usage : Samp <ip> <port> <choice (y)> <packet> <threads>")
                    print("Example : Samp 127.0.0.1 7777 y 1000 1000")
#layer7
        elif "Tls" in cnc:
              try:
                    target=cnc.split()[1]
                    time=cnc.split()[2]
                    rate=cnc.split()[3]
                    threads=cnc.split()[4]
                    proxyfile=cnc.split()[5]
                    os.system(f"node TLS.js {target} {time} {rate} {threads} {proxyfile}")
              except IndexError:
                    print("Usage : Tls <target> <time> <rate> <threads> <proxyfile>")
                    print("Example : Tls https://fbi.gov/ 120 1000 10 proxy.txt")
def author(kiohana):
	print ("Shell Credit : GadaLuBau")
	print ("Building The Methods : Xinzu")
	print ("Fixed,Tester : GadaLuBau X Xinzu")
	print ("""
Infomation GadaLuBau :
https://github.com/gadalubau1337
https://tiktok.com/@gadalubau1337
Infomation Xinzu :
https://github.com/XINZU4546
https://tiktok com/@xinzuxyzz""")
def exit(kiohana):
    if arg==[]:
        arg=["0"]
    try:
        sys.exit(int(arg[0]))
    except ValueError:
        print("\rshell: exit: {}: numeric argument required".format(arg[0]))
        

if __name__ == '__main__':
    os.system('clear')
    set_terminal_title(f"Sonic Panel, All User_Access : ")
    HOME = os.path.expanduser('~') # Gán giá trị cho biến uyen
    


    main()
