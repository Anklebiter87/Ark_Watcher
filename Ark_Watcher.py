#/usr/bin/env python3

import re
import os
import time
import psutil

def get_proc():
    for i in psutil.pids():
        info = psutil.Process(i)
        if re.search('ShooterGameServer',info.name()):
            return info

def connection_check(ark_server):
    for i in ark_server.connections():
        if i.laddr[0] == '10.240.0.3':
            return True
    return False

def start_sleep(sleeptime):
    time.sleep(sleeptime)

def main():
    hup = 0
    while True:
        if connection_check(get_proc()):
            start_sleep(60*60)
        else:
            os.system('systemctl restart  ark-dedicated.service')
            start_sleep(60*60*24)

if __name__ == '__main__':
    main()

