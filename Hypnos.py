# Copyright (c) 2025 | ©Hypnos (https://www.youtube.com/@ShoEasyCode) 

# WARNING   | Do not use it in a wrong way or cause trouble to others.
# Objective | For Ethical Hacking & Education (2E)

# By. ©Hypnos

# EN 
# ├── Do not modify the source code and use it as your own. (credit it to yours.)
# |
# ├── Do not use it for illegal purposes, otherwise it may violate the Computer Act and we will not be involved.
# |
# └── The purpose of this program is for educational and ethical hacking purposes only.

# CH
# ├── 請勿修改原始程式碼並將其用作自己的程式碼。 （ 歸功於你。）
# |
# ├── 請勿將其用於非法目的，否則可能違反電腦法，我們不會介入。
# |
# └── 此程序的目的僅用於教育和道德黑客目的。


import os
import time
from datetime import datetime
import getpass
from Function.Config.Config import *
from Function.Config.Banner import *

import Function.Config.list_menu as list_menu

os.system('cls')


list_of_len_message = []
for i in range(1,len(list_menu.list_menu)+1):
    message_menu = list(dict(list_menu.list_menu)[i])[0]
    list_of_len_message.append(len(message_menu))
    
max_len_of_message = max(list_of_len_message)

menu_sequence_number = []
for i in range(1,len(list_menu.list_menu)+1):
    menu_sequence_number.append(i)

message_menu_box = []
for i in range(1,len(list_menu.list_menu)+1,2):
  if i in menu_sequence_number: message = f"│  [{i}] {list(dict(list_menu.list_menu)[i])[0]}"
  if i+1 in menu_sequence_number: message2 = f"[{i+1}] {list(dict(list_menu.list_menu)[i+1])[0]}"
  else: message2 = ""
  sum_message = f"{message}{((max_len_of_message-len(message)+10) * ' ')}  {message2}{((max_len_of_message-len(message2)+10) * ' ')}│"
  message_menu_box.append(len(sum_message))

def Banner():
  for line in banner.split("\n"):
      print(CYAN,line,RESET)
      time.sleep(0.02)

def List_menu():
  print(f"┌{(max(message_menu_box)-2) * "─"}┐")
  for i in range(1,len(list_menu.list_menu)+1,2):
    if i in menu_sequence_number: message = f"│  [{i}] {list(dict(list_menu.list_menu)[i])[0]}"
    if i+1 in menu_sequence_number: message2 = f"[{i+1}] {list(dict(list_menu.list_menu)[i+1])[0]}"
    else: message2 = ""

    print(f"{message}{((max_len_of_message-len(message)+10) * ' ')}  {message2}{((max_len_of_message-len(message2)+10) * ' ')}│")
  print(f"└{(max(message_menu_box)-2) * "─"}┘\n")

def Error_message(message, error_type, current_page=None):
  if error_type == "invalid_choice":
    print(f"[{datetime.now().strftime("%H:%M:%S")}] | [X] Not found : {message}")

def Input_choice():
  try:
    menu_selected = input(f" ┌──({getpass.getuser()} @ Hypnos)─[~]\n └─$ ")
  except:
    Error_message(message=menu_selected, error_type="invalid_choice", current_page=None)

def Menu():
  Banner()
  List_menu()
  Input_choice()

Menu()