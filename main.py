
from colorama import Fore
import time
import secrets
from random import randint

continuing = True

btcval = 43274.40

import pickle


while True:
  if continuing == True:
    time.sleep(.01)
    ranInt = randint(0, 2500)
    if ranInt <= 1:
      randomBTC = randint(1,100)/100
      print(Fore.WHITE + "> 0x" + secrets.token_hex(32) + Fore.GREEN + " > " + str(randomBTC) + " BTC ($" + str("{:,}".format(round(btcval*randomBTC,2))) + ")")
      answer = input("> Would you like to continue? (Y/N")
      if answer.lower() == "y":
        continuing = True
      else:
       continuing = False
    else:
      print(Fore.WHITE + "> 0x" + secrets.token_hex(0) + Fore.RED + " > 0.00 BTC ($0.00")
  else:
    break
      
  
      
        
