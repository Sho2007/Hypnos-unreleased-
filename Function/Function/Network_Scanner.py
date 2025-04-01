import subprocess
import os

class Network_Scanner():
    def __init__(self,ip_address=None,port=None,new_terminal=False):
        self.ip_address = ip_address
        self.Port = port
        self.new_terminal = new_terminal

    def IP_address_scan(self):
        if self.new_terminal == True:
            subprocess.run(f'start cmd /K "nmap {self.ip_address}"', shell=True)
        else:
            subprocess.run(f"nmap {self.ip_address}", shell=True)

        # note
        text = ""
        list_switch = text.split(" ")

        scanall = False if text.find("-scanall") == -1 else True
        ip = list_switch[list_switch.index("-v")+1]
        file = list_switch[list_switch.index("-r")+1]