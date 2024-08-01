import os
import argparse
import time
from colorama import Fore, Style, init

os.system('clear')

init(autoreset=True)

parser = argparse.ArgumentParser(description="Name of file and port")
parser.add_argument("-t", required=True, help="File with IP range")
parser.add_argument("-b", required=True, help="1 or 2 (Bruter 1 and Bruter 2)")
parser.add_argument("-p", required=True, help="Password fro Bruter1")
args = parser.parse_args()

File = args.t
Bruter = args.b
Password = args.p

def start_ua(File, Bruter, Password):
    os.system('clear')
    print(f"""{Fore.RED}

███╗░░░███╗░█████╗░░██████╗░██████╗░█████╗░░█████╗░███╗░░██╗░░░░░░██████╗░████████╗░██████╗██████╗░
████╗░████║██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░██║░░░░░░██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║███████║╚█████╗░╚█████╗░██║░░╚═╝███████║██╔██╗██║█████╗██████╔╝░░░██║░░░╚█████╗░██████╔╝
██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗██║░░██╗██╔══██║██║╚████║╚════╝██╔══██╗░░░██║░░░░╚═══██╗██╔═══╝░
██║░╚═╝░██║██║░░██║██████╔╝██████╔╝╚█████╔╝██║░░██║██║░╚███║░░░░░░██║░░██║░░░██║░░░██████╔╝██║░░░░░
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝░░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═╝░░░░░
""")

    print(File, Bruter, Password)

def mas_scan(File):
    os.system(f"masscan -iL {File} -p554 --rate 10000 >> out.txt && sed 's/Discovered open port [0-9]*\\/tcp on //g' out.txt > masmap.txt && rm out.txt")
    print("Masscan is complet!")
    
def bruter_o(Bruter, Password):
    if Bruter == '1':
        os.system(f"python3 Bruter1.py -t ./masmap.txt -u ./user.txt -password {Password} run")

    if Bruter == '2':
        os.system(f"python3 Bruter2.py")
            

def start_scan(File, Bruter, Password):
    start_ua(File, Bruter, Password)

    mas_scan(File)
    time.sleep(1)
    
    bruter_o(Bruter, Password)
    time.sleep(1)

    print("Scan is Complete.")

if __name__ == "__main__":
    start_scan(File, Bruter, Password)