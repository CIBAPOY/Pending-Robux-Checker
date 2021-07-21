import requests
import os
import json
from datetime import datetime
import time

os.system('cls')

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"{bcolors.WARNING}  _____       _                 _____ _               _             ")
print(" |  __ \     | |               / ____| |             | |            ")
print(" | |__) |___ | |__  _   ___  _| |    | |__   ___  ___| | _____ _ __ ")
print(" |  _  // _ \| '_ \| | | \ \/ / |    | '_ \ / _ \/ __| |/ / _ \ '__|")
print(" | | \ \ (_) | |_) | |_| |>  <| |____| | | |  __/ (__|   <  __/ |   ")
print(f" |_|  \_\___/|_.__/ \__,_/_/\_\\_____|_| |_|\___|\___|_|\_\___|_|   {bcolors.ENDC}")

print("\n")

while True:
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M")

    dir = os.path.dirname(os.path.abspath(__file__))
    cook = os.path.join(dir, "cookie.txt")

    f = open(cook, "r")
    cookie = f.read()
    f.close()

    testing = requests.post('https://auth.roblox.com/v2/logout', cookies = {'.ROBLOSECURITY':cookie})

    token = testing.headers['x-csrf-token']

    header = {
        '.ROBLOSECURITY': cookie,
        'x-csrf-token': token,
        'content-type': 'application/json'
    }

    player = requests.get('https://www.roblox.com/mobileapi/userinfo', headers=header, cookies = {'.ROBLOSECURITY':cookie}).json()

    userid = player['UserID']

    # https://economy.roblox.com/v2/users/userid/transaction-totals?timeFrame=month&transactionType=summary&limit=100

    r = requests.get(f"https://economy.roblox.com/v2/users/{userid}/transaction-totals?timeFrame=month&transactionType=summary&limit=100", headers=header, cookies = {'.ROBLOSECURITY':cookie})
    response = str(r.content)
    responses = response[2:len(response)-1]

    jsonData = json.loads(responses)
    pendings = jsonData['pendingRobuxTotal']

    # https://economy.roblox.com/v1/users/userid/currency

    r = requests.get(f"https://economy.roblox.com/v1/users/{userid}/currency", headers=header, cookies = {'.ROBLOSECURITY':cookie})
    response = str(r.content)
    response = response[2:len(response)-1]

    jsonData = json.loads(response)
    pending = jsonData['robux']
    print(f"{bcolors.OKGREEN}Current Robux: {bcolors.ENDC}{pending}")
    print(f"{bcolors.OKGREEN}Pending Robux: {bcolors.ENDC}{pendings}")

    pendingsss = int(pending)
    pendingss = int(pendings)

    total = pendingss+pendingsss

    print(f"{bcolors.OKGREEN}Total Robux: {bcolors.ENDC}{total}")
    input(f"{bcolors.OKCYAN}\nFinished! (Press 'enter' key to exit){bcolors.ENDC}")
    exit()
