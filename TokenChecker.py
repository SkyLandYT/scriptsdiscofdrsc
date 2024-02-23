from time import time, sleep
from os import system
from terminut import BetaConsole
import requests
from pypresence import Presence
import os

# Discord RPC
RPC = Presence("1207858419411849226")
RPC.connect()

# Discord API
class CustomDiscordAPI:
    def __init__(self, version: str = "v9"):
        self.version = version

    def getUser(self, token):
        headers = {
            "Authorization": token,
            "Content-Type": "application/json",
        }
        response = requests.get(f"https://discord.com/api/{self.version}/users/@me", headers=headers)

        return response

if __name__ == "__main__":
    c = BetaConsole(speed=2)
    timestamp = c.getTimestamp()
    discordApi = CustomDiscordAPI()
    system("cls || clear")
    
    print(f"""
 _______ ____  _  ________ _   _      ____ _    _ _______ ____ _____ ___________
|__   __/ __ \| |/ /  ____| \ | |   / ____| |  | |  ____/ ____| |/ /  ____|  __ \ 
   | | | |  | | ' /| |__  |  \| |  | |    | |__| | |__ | |    | ' /| |__  | |__) |
   | | | |  | |  < |  __| | . ` |  | |    |  __  |  __|| |    |  < |  __| |  _  / 
   | | | |__| | . \| |____| |\  |  | |____| |  | | |___| |____| . \| |____| | \ \ 
   |_|  \____/|_|\_\______|_| \_|   \_____|_|  |_|______\_____|_|\_\______|_|  \_\
  
   |                     Discord :       xaa.su/skyteam                           |
    """)
    file_path = input("Enter the path to the text file: ")

    with open(file_path, "r") as file:
        totalTokens = len(file.readlines())
        file.seek(0)
        RPC.update(details=f"Checking {totalTokens} Discord Tokens...", state="xaa.su/skyteam", start=time())
        c.alphaPrint("", f"[{timestamp}] Checking {totalTokens} Discord Tokens...")

        for token in file:
            token = token.strip()
            userData = discordApi.getUser(token)

            if userData.status_code == 200:
                user = userData.json()
                userId = user["id"]
                userEmail = user["email"]
                userName = user["username"]
                userLocale = user["locale"]
                c.alphaPrint("", f"[{timestamp}] [\033[92mVALID\033[0m] ID: {userId} | Email: {userEmail} | Username: {userName} | Locale: {userLocale}")
                with open("./Data/DS/TokenChecker/valid.txt", "w") as f:
                    f.write(f"Token: {token} | ID: {userId} | Email: {userEmail} | Username: {userName} | Locale: {userLocale}")
            else:
                c.alphaPrint("", f"[{timestamp}] [\033[91mINVALID\033[0m] {token}")
open_file = input("Would you like to open the 'valid.txt' file? (Y/N): ")
if open_file.lower() == "n":
    os.remove(__file__)
elif open_file.lower() == "y":
    os.system("notepad valid.txt")
    os.remove(__file__)
