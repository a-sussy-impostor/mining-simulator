from setup import *
  

print(blue + title())
print(cyan + "Press [ENTER] to start " + reset)

enter = input()
clear()

while True:
  print(heading)
  print(f"You are at biome {biome}. Your pickaxe is {pick}. What do you want to do? Type your {blue}action{reset}.")
  print("1: Mine")
  print("2: Shop")
  print("3: Gift Code")
  if cango == True:
    print("4: Go to Another Biome")
  else:
    print("4: LOCKED")
  if netlock == False:
    print("5: Go To Nether")
  else:
    print("5: LOCKED")
  if endlock == False:
    print("6: Go To Ender")
  else:
    print("6: LOCKED")
  if gamefin == True:
    print("7: Upload Data To Leaderboard")
  else:
    print("7: LOCKED")
  print()
  if access == True:
    print("8: Console")
  else:
    print(f"{red}Admin Console Is Only Accessable by admins{reset}")
  print(line + " 📊  Stats " + line)
  print(f" Mining Times: {green}{total}{reset} \n Money Collected: {pink}{allm}{reset} \n Mines Discovered: {cyan}{minesDisc}{reset} \n Discovered Minerals: {green}{discMinerals}{reset} \n Played Minutes: {yellow}{playtime}{reset} \n Daytime: {blue}{daytime}{reset}")
  inputAction = input("Action: ")
  try:
    action = int(inputAction)
    if action == 1:
      mine()
    elif action == 2:
      shop()
  except Exception as e:
    if inputAction != "sus":
      report(e)
      wait(3)
    else:
      amongus()
  finally:
    clear()
      
