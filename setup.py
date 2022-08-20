from os import system,environ
from time import sleep as wait
from colorama import Fore as f
import tkinter as tk
import json
from random import randint, choice, randrange

red = f.RED
blue = f.BLUE
cyan = f.LIGHTBLUE_EX
yellow = f.LIGHTYELLOW_EX
lime = f.LIGHTGREEN_EX
green = f.GREEN
reset = f.RESET
brown = f.YELLOW
purple = f.MAGENTA
pink = f.LIGHTMAGENTA_EX

title1 = "███╗░░░███╗██╗███╗░░██╗██╗███╗░░██╗░██████╗░"
title2 = "████╗░████║██║████╗░██║██║████╗░██║██╔════╝░"
title3 = "██╔████╔██║██║██╔██╗██║██║██╔██╗██║██║░░██╗░"
title4 = "██║╚██╔╝██║██║██║╚████║██║██║╚████║██║░░╚██╗"
title5 = "██║░╚═╝░██║██║██║░╚███║██║██║░╚███║╚██████╔╝"
title6 = "╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝╚═╝░░╚══╝░╚═════╝░"
title7 = "░██████╗██╗███╗░░░███╗██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░"
title8 = "██╔════╝██║████╗░████║██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗"
title9 = "╚█████╗░██║██╔████╔██║██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝"
title10 = "░╚═══██╗██║██║╚██╔╝██║██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗"
title11 = "██████╔╝██║██║░╚═╝░██║╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║"
title12 = "╚═════╝░╚═╝╚═╝░░░░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝"
def listToString(list,join): 
    
    # initialize an empty string
    str1 = "" 
    
    # traverse in the string  
    for ele in list:
        str1 += ele  
        str1 += join
    
    # return string  
    return str1 

def title():
    # join the title
    titleall = [title1,title2,title3,title4,title5,title6,title7,title8,title9,title10,title11,title12]
    return listToString(titleall,"\n")
# sets the username
username = environ["REPL_OWNER"]

# customize the menu
heading = "———————————————————————————————————————— ⛏  Mining Simulator  ———————————————————————————————————————— "
line = "———————————————————————————————————————— "

# more convenient
def clear(): system("clear")

def report(e,write = False):
  print(f"{red}An Error Occurred while running: {e} {reset}")
  if write == True:
     with open("error.txt","w") as f:
        f.write(str(e))
# Gamedata
biome = green + "Plains" + reset
bionum = 0
pick = purple + "Noob Pickaxe" + reset
picknum = 0
money = 0
cango = False
netlock = True
endlock = True
gamefin = False

# Stats 
total = 0
went = 0
discMinerals = 0
minesDisc = 0
playtime = 0
daytime = 0
collected = 0
allm = 0