import time
from mojang import MojangAPI
from colorama import Fore
import requests



name = input('username : ')

uuid = MojangAPI.get_uuid(name)
profile = MojangAPI.get_profile(uuid)
legacy = MojangAPI.get_name_history(uuid)


name_history = requests.get(f"https://api.mojang.com/user/profiles/{uuid}/names").json()
history = ""
name_data = list()
for data in name_history:
    name_data.append(data["name"])
print(name_data[0])



if not uuid:
    print("pas de compte a ce nom ")
else:
    print(Fore.CYAN + "UUID = " + Fore.RESET + uuid )
    print(Fore.CYAN + "NAME = " + Fore.RESET + name )
    print(Fore.CYAN + "SKIN = " + Fore.RESET + profile.skin_url)

    
    for i in range(len(name_data)):
        history += name_data[i] + " | "
        
    print(Fore.CYAN + "NAME_CHANGE = " + Fore.RESET + history)