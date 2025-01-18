import requests
import random
import string
import base64
from colorama import init, Fore, Style
from pystyle import Colors, Colorate, Center
import os
import time
from getpass import getpass

init()
os.system('title ^| Eternal IMP ^| Discord.gg/cBq6GSRXgx ^| Nitro Gen V2 ^|')
os.system("mode con: cols=80 lines=20")

t = time.strftime('%H:%M:%S')

rs = "\033[0m"
d = '\033[38;2;50;100;255m'
g = "\033[32m"
r = "\033[31m"

def generate_nitro_code():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return code

def check_nitro_code(code):
    url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["uses"] == 0:
            return True
    return False

def get_image_base64(url):
    response = requests.get(url)
    if response.status_code == 200:
        return base64.b64encode(response.content).decode('utf-8')
    else:
        return None

def update_webhook(webhook_url):
    image_url = "https://cdn.discordapp.com/attachments/1250078637215060068/1262709684939259944/Red_and.png?ex=66979588&is=66964408&hm=0c384eb5d2146eadbf9af373de728f58e3b01c3a3022b1dea8d51b9000f5aba6&"
    image_base64 = get_image_base64(image_url)

    if image_base64:
        data = {
            "name": "Impossible",
            "avatar": f"data:image/png;base64,{image_base64}"
        }
        response = requests.patch(webhook_url, json=data)
        if response.status_code == 200:
            print(f"{g}[{t}] Webhook updated successfully{rs}")
        else:
            print(f"{r}[{t}] An error occurred while updating the webhook: {response.status_code} - {response.text}{rs}")

def send_to_webhook(webhook_url, code, status):
    full_code_url = f"https://discord.gift/{code}"
    data = {
        "content": f"The code link is done: {full_code_url} (Eternal IMP >> {'@here It\'s working' if status else '@here It\'s not working'})"
    }
    response = requests.post(webhook_url, json=data)
    if response.status_code == 204:
        print(f" {t} {d}[{rs}${d}]{rs} Code has been generated successfully")
    else:
        print(f"{r}[{t}] An error occurred while sending the code: {response.status_code} - {response.text}{rs}")

def print_banner():
    print(Colorate.Horizontal(Colors.blue_to_cyan, r"""
       
            _   ___ __                ______              _    _____ 
           / | / (_) /__________     / ____/__  ____     | |  / /__ \
          /  |/ / / __/ ___/ __ \   / / __/ _ \/ __ \    | | / /__/ /
         / /|  / / /_/ /  / /_/ /  / /_/ /  __/ / / /    | |/ // __/ 
        /_/ |_/_/\__/_/   \____/   \____/\___/_/ /_/     |___//____/ 
                                                             
"""))

def main():
    while True:
        print_banner()
        webhook_url = getpass(f" {t} {d}[{rs}${d}]{rs} WebHook >> ")
        num_codes = int(input(f" {t} {d}[{rs}${d}]{rs} How Many Nitro Codes >> "))

        update_webhook(webhook_url)

        for _ in range(num_codes):
            code = generate_nitro_code()
            status = check_nitro_code(code)
            send_to_webhook(webhook_url, code, status)

        input(f" {t} {d}[{rs}${d}]{rs} The nitro generator stopped successfully. Press Enter to retry")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
