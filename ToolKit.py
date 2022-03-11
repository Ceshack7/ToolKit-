import requests
import json
import os
import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
BLACK = '\033[30m'
os.system("clear")
print(RED+ """
████████╗░█████╗░██╗░░░░░██╗░░██╗██╗████████╗
╚══██╔══╝██╔══██╗██║░░░░░██║░██╔╝██║╚══██╔══╝
░░░██║░░░██║░░██║██║░░░░░█████═╝░██║░░░██║░░░
░░░██║░░░██║░░██║██║░░░░░██╔═██╗░██║░░░██║░░░
░░░██║░░░╚█████╔╝███████╗██║░╚██╗██║░░░██║░░░
░░░╚═╝░░░░╚════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░╚═╝░░░\n \n""")
print(GREEN+"""▄▄▄                  ──────────────   ▄▀█▀█▀▄   
  █▀█▀█ █▀█  █▀█ ▄███▄  ─────────────  ▀▀▀▀▀▀▀▀▀  ▄▄▄▄▄
  █▀█▀█ █▀██ █▀█ █▄█▄█             ▄▄     ░░░   ▄█▄█▄█▄█▄
  █▀█▀█ █▀████▀█ █▄█▄█    ── ▄▄─── ▐▌      +       ░░░
  █▀█▀█ █▀████▀█ █▄█▄█ ▌██▐▌▐█▐▐▌█▌█▌█▌▌   +       ░░░\n""")
   
print(MAGENTA+"""
                       ToolKit v1.1""")
print(CYAN+"--------------------------------------------------------")
print(CYAN+"Author : Ceshack7")
print("--------------------------------------------------------")
time.sleep(1)
print("redes sociales : TikTok Github")
print("--------------------------------------------------------")
time.sleep(1)
print("@Ceshack7 @SoyCeshack7 Git : Ceshack7")
print("---------------------------------------------------------")
time.sleep(1)
print("Contacto : @SoyCeshack7")
print("--------------------------------------------------------")
time.sleep(1)
print("Derechos de Author: Ceshack7")
print("-------------------------------------------------------- \n")

api_url = "http://ip-api.com/json/"
parametros = 'status,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query'
data = {"fields":parametros}

def ip_scraping(ip=""):
 res = requests.get(api_url+ip, data=data)
 api_json_res = json.loads(res.content)
 return api_json_res

if __name__ == '__main__':
 ip = input(WHITE+"Ingrese la dirección IP >>> "+GREEN)


par = parametros.split(",")
for x in par:
 print(x.upper(), ":")
 print( ip_scraping(ip)[x])
 print("===================================")