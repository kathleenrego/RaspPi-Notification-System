#!/usr/bin/python
import os
import subprocess
import time
import commands

# Return CPU temperature                                    
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))

# Return RAM information (unit=kb) in a list                                       
# Index 0: total RAM                                                               
# Index 1: used RAM                                                                 
# Index 2: free RAM                                                                 
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i==2:
            return(line.split()[1:4])

# Return % of CPU                              
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
    )))

# Return information about disk space                    
# Index 0: total disk space                                                         
# Index 1: used disk space                                                         
# Index 2: remaining disk space                                                     
# Index 3: percentage of disk used                                                 
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while 1:
        i = i +1
        line = p.readline()
        if i==2:
            return(line.split()[1:5])

CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()
delay = 1

RetMyIP = commands.getoutput("hostname -I")

a_1 = "curl -u [Your_PushBullet_Token_Here]: https://api.pushbullet.com/v2/pushes -d type=note -d title='Raspberry Pi' -d body='"
msg_0 = a_1 + "Hey Sir!" + "'"
msg_ip = "IP: " + RetMyIP
msg_1 = "CPU temperature: " + CPU_temp
msg_2 = "CPU usage: " + CPU_usage
msg = a_1 + "Boot INFO..." + "\n" + msg_ip + "\n" + msg_1 + "'"
msg_3 = a_1 + "have a good day :)" + "'"
subprocess.call(msg_0 , shell=True)
time.sleep(delay)
subprocess.call(msg , shell=True)
time.sleep(3)
subprocess.call(msg_3 , shell=True)

def monitor():
  while 1:
    # Checking the system every 15 min
    time.sleep(900)
    
    msg_m = a_1 + "Checking the System..." + "'"
    subprocess.call(msg_m , shell=True)
    time.sleep(1)
  
    if float(getCPUtemperature()) < 42.0:
    
      msg_m_1 = a_1 + "CPU usage: " + getCPUuse() + "\n" + "Temperature is stable " + "[" + getCPUtemperature() + "]" + "'"
      subprocess.call(msg_m_1 , shell=True)
      monitor()
    else:
    
    
      msg_m_2 = a_1 + "CPU usage: " + getCPUuse() + "\n" + "Warning!! Temperature is unstable" + "[" + getCPUtemperature() + "]" + "'"
      subprocess.call(msg_m_2 , shell=True)
      monitor()


monitor()
