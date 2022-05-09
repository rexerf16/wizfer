import json
import socket
from datetime import datetime
import re
import urllib.request as urllib2
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import colorama
import platform
import subprocess
import sys
from colorama import Back, Style, Fore
from phonenumbers.phonenumberutil import _raw_input_contains_national_prefix
import nmap


regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

colorama.init(autoreset=True)


version = Fore.MAGENTA+"                    V('0.1.0')              "

line = Fore.LIGHTWHITE_EX+"*********************************"

Signature = Fore.LIGHTRED_EX+"""
 __          ___      __          
 \ \        / (_)    / _|         
  \ \  /\  / / _ ___| |_ ___ _ __ 
   \ \/  \/ / | |_  /  _/ _ \ '__|
    \  /\  /  | |/ /| ||  __/ |   
     \/  \/   |_/___|_| \___|_|   
                                  
                    V('0.2.1')	
"""


def Admin():
    print(Fore.LIGHTCYAN_EX+" ✦✦✦✦✦* ♛ welcome ♛ *✦✦✦✦✦ ")
    print("")
    print("")
    print(line)
    Service()


def Service():
    print(Fore.LIGHTWHITE_EX+"(" + Fore.LIGHTYELLOW_EX + "1" +
          Fore.LIGHTWHITE_EX + ")" + Fore.LIGHTBLUE_EX + " Get phone number info")
    print(Fore.LIGHTWHITE_EX+"(" + Fore.LIGHTYELLOW_EX + "2" +
          Fore.LIGHTWHITE_EX + ")" + Fore.LIGHTBLUE_EX + " Scan ports By IP")
    print(Fore.LIGHTWHITE_EX+"(" + Fore.LIGHTYELLOW_EX + "3" +
          Fore.LIGHTWHITE_EX + ")" + Fore.LIGHTBLUE_EX + " Ping your target By IP/Website ")
    print(Fore.LIGHTWHITE_EX+"(" + Fore.LIGHTYELLOW_EX + "4" +
          Fore.LIGHTWHITE_EX + ")" + Fore.LIGHTBLUE_EX + " Get IP info")
    print(Fore.LIGHTWHITE_EX+"(" + Fore.LIGHTYELLOW_EX + "5" +
          Fore.LIGHTWHITE_EX + ")" + Fore.LIGHTBLUE_EX + " Check email")
    print(Fore.LIGHTWHITE_EX+"(" + Fore.LIGHTYELLOW_EX + "6" +
          Fore.LIGHTWHITE_EX + ")" + Fore.LIGHTBLUE_EX + " Get website info")
    print(Fore.LIGHTWHITE_EX+"(" + Fore.LIGHTYELLOW_EX + "7" +
          Fore.LIGHTWHITE_EX + ")" + Fore.LIGHTBLUE_EX + " Exit")
    print(Fore.LIGHTWHITE_EX +
          "*********************************")


def ping(host):
    n = input("How many times do you want to ping the target '10,20,30,....' ?? : ")
    print("")
    print(Fore.GREEN+"Starting the service....")
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', '-c', n, host]
    return subprocess.call(command)


def pingg():
    try:
        host = input(Fore.LIGHTYELLOW_EX+"Enter the IP target : ")
        print(ping(host))
        Var = input(Fore.LIGHTYELLOW_EX +
                    "do you want to start pinging again ?? 'Yes/No' ?? : ")
        if Var.lower() == "no":
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == "yes":
            while True:
                pingg()
    except Exception:
        print(Fore.LIGHTRED_EX +
              "Somthing went worng !! please report the Error to the author on https://github.com/rexerf16 ")
        os.execl(sys.executable, sys.executable, *sys.argv)


def check(email):
    try:
        if (re.search(regex, email)):
            print(Fore.LIGHTYELLOW_EX + "Email: " +
                  email+Fore.LIGHTGREEN_EX+" is [Valid]")
        else:
            print(Fore.LIGHTYELLOW_EX+"Email: "+email +
                  Fore.LIGHTRED_EX+" is [Invalid]")
    except Exception:
        print(Fore.LIGHTRED_EX +
              "Somthing went worng !! please report the Error to the author on https://github.com/rexerf16 ")


def PhoneNumbers():
    try:
        mobileNo = input(Fore.LIGHTYELLOW_EX +
                         "Enter Mobile number. with country code : ")
        mobileNo = phonenumbers.parse(mobileNo)
        print(timezone.time_zones_for_number(mobileNo))
        print(carrier.name_for_number(mobileNo, Fore.LIGHTRED_EX+"en"))
        print(geocoder.description_for_number(mobileNo, Fore.LIGHTRED_EX+"en"))
        print(Fore.LIGHTYELLOW_EX+"Valid Mobile Number:",
              phonenumbers.is_valid_number(mobileNo))
        print(Fore.LIGHTYELLOW_EX+"Checking possibility of Number:",
              phonenumbers.is_possible_number(mobileNo))
        var = input(Fore.LIGHTYELLOW_EX +
                    "do you want to search again 'Yes/No ?? : ")
        if var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower() == 'yes':
            while True:
                PhoneNumbers()
    except phonenumbers.phonenumberutil.NumberParseException:
        print(Fore.LIGHTRED_EX +
              "Wrong phone format input !! Right Ex >>>  '+190765....' , '+96653.....' ")
        var = input(Fore.LIGHTYELLOW_EX +
                    "do you want to search again 'Yes/No ?? : ")
        if var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if var.lower() == 'yes':
            while True:
                PhoneNumbers()


def ScanPorts():
    try:
        target = input(Fore.LIGHTYELLOW_EX+"Enter the IP target : ")
        begin = int(input(Fore.LIGHTYELLOW_EX+"Enter the begin port range : "))
        end = int(input(Fore.LIGHTYELLOW_EX+"Enter the end port range : "))
        print("")
        print(Fore.GREEN+" Starting scanning ..... "+target)
        print("")
        scanner = nmap.PortScanner()
        for i in range(begin, end+1):
            res = scanner.scan(target, str(i))
            res = res['scan'][target]['tcp'][i]['state']
            print(f'port {i} is {res}.')
        print("")
        print(Fore.GREEN+"Scanned successfuly !! ")
        Var = input(Fore.LIGHTYELLOW_EX +
                    "Do you want to scan again ?? 'Yes/No' ?? : ")
        if Var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == 'yes':
            while True:
                ScanPorts()
    except KeyError:
        print(Fore.LIGHTRED_EX+"Wrong IP input !!")
        Var = input(Fore.LIGHTYELLOW_EX +
                    "Do you want to scan again ?? 'Yes/No' ?? : ")
        if Var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == 'yes':
            while True:
                ScanPorts()
    except ValueError:
        print(Fore.LIGHTRED_EX+"Wrong Range input !!")
        Var = input(Fore.LIGHTYELLOW_EX +
                    "Do you want to scan again ?? 'Yes/No' ?? : ")
        if Var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == 'yes':
            while True:
                ScanPorts()


def ip_info():
    try:
        while True:
            ip = input(Fore.LIGHTYELLOW_EX+"Enter your Target IP : ")
            url = "http://ip-api.com/json/"
            response = urllib2.urlopen(url + ip)
            data = response.read()
            values = json.loads(data)
            print("")
            print("[ IP: " + values['query']+" ]")
            print("[ status: " + values['status'] + " ]")
            print("[ country: " + values['country'] + " ]")
            print("[ region: " + values['region'] + " ]")
            print("[ regionName: " + values['regionName'] + " ]")
            print("[ city: " + values['city'] + " ]")
            print("[ timezone: " + values['timezone'] + " ]")
            print("[ isp: " + values['isp'] + " ]")
            break
        print("")
        Var = input(Fore.LIGHTYELLOW_EX +
                    "Do you wnat to Scan again ?? 'Yes/No : ")
        if Var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == 'yes':
            while True:
                ip_info()
    except KeyError:
        print(Fore.LIGHTRED_EX+"Wrong IP input !!")
        Var = input(Fore.LIGHTYELLOW_EX +
                    "Do you wnat to Scan again ?? 'Yes/No : ")
        if Var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == 'yes':
            while True:
                ip_info()
    except Exception:
        print(Fore.LIGHTRED_EX+"Wrong IP input !!")
        Var = input(Fore.LIGHTYELLOW_EX +
                    "Do you wnat to Scan again ?? 'Yes/No : ")
        if Var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == 'yes':
            while True:
                ip_info()


def check_email():
    try:
        if __name__ == "__main__":
            email = input(Fore.LIGHTYELLOW_EX+"Enter Email : ")
            check(email)
        Var = input(Fore.LIGHTYELLOW_EX +
                    "Do you wnat to Check again ?? 'Yes/No : ")
        if Var.lower() == 'no':
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == 'yes':
            while True:
                check_email()
    except Exception:
        print(Fore.LIGHTRED_EX +
              "Somthing went worng !! please report the Error to the author on 'https://github.com/rexerf16' ")


def website_info():
    try:
        website = input(Fore.LIGHTYELLOW_EX + "Enter the website nmae : ")
        full_web_url = f"www.{website}.com"
        ip_add = socket.gethostbyname(full_web_url)
        while True:
            url = "http://ip-api.com/json/"
            response = urllib2.urlopen(url + ip_add)
            data = response.read()
            values = json.loads(data)
            print("")
            print("[ IP: " + values['query']+" ]")
            print("[ status: " + values['status'] + " ]")
            print("[ country: " + values['country'] + " ]")
            print("[ region: " + values['region'] + " ]")
            print("[ regionName: " + values['regionName'] + " ]")
            print("[ city: " + values['city'] + " ]")
            print("[ timezone: " + values['timezone'] + " ]")
            print("[ isp: " + values['isp'] + " ]")
            break
        print("")
        Var = input(Fore.LIGHTYELLOW_EX +
                    "Do you want to search again 'Yes/No' ?? : ")
        if Var.lower() == "no":
            os.execl(sys.executable, sys.executable, *sys.argv)
        if Var.lower() == "yes":
            while True:
                website_info()
    except Exception:
        print(Fore.LIGHTRED_EX +
              "Somthing went worng !! please report the Error to the author on 'https://github.com/rexerf16' ")


# First thing that will be executed ....
print(Signature)
print(Fore.LIGHTYELLOW_EX+"Programmed By : Mohammed Farhan")
print(Fore.LIGHTYELLOW_EX +
      "Github Page >>>> 'https://github.com/rexerf16'")

print("")

try:
    Admin()
    SS = input(
        Fore.WHITE+"Choose one of the options that you see by Entering the option number : ")
    print(Fore.WHITE+"*******************************************************")
    print("")

    if SS == '1':
        PhoneNumbers()

    if SS == '2':
        ScanPorts()

    if SS == '3':
        pingg()

    if SS == '4':
        ip_info()

    if SS == '5':
        check_email()

    if SS == '6':
        website_info()

    if SS == '6':
        sys.exit()


except KeyboardInterrupt:
    print(Fore.LIGHTRED_EX + "\n KeyboardInterrupt !!")
