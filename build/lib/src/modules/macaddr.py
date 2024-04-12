# Imports.
import os
import sys
import json
import requests
from colorama import Fore # For text colour.
import json
import prints

# Pre-run.
os.system("clear")

# Hide tracebacks - change to 1 for dev mode.
sys.tracebacklimit = 0

# API.
# Example, uncomment lines 30-32 if API required.
#with open('var/pipes/api_config.json') as f:
#    data = json.load(f)
#    #{api_name} = data["{api_name}"]

# Program.
def macaddr():
   addr = input("Enter a MAC address: ")

   r = requests.get(f"https://www.macvendorlookup.com/oui.php?mac={addr}")

   if r.status_code == 200:
       try:
           results = r.json()
       except json.decoder.JSONDecodeError:
           print(f"{prints.failed} Address not found in database!")
       else:
           print(f"Company: {results[0]['company']}")
           print(f"Country: {results[0]['country']}")
           print(f"Address: {results[0]['addressL1']}, {results[0]['addressL3']}")
   elif r.status_code == 204:
       print(f"{prints.failed} Address not found in database!")
   elif r.status_code == 404:
       print(f"{prints.failed} Status Code 404: Page not found!")
   else:
       print(f"{prints.failed} An error has occurred! Status Code: {r.status_code}")
# Run module_name module.

if __name__ == '__main__':
    macaddr()
