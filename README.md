# wireme :
----

![N|](https://i.imgur.com/uVg7nVb.png)
_____
# what is wireme ?? :
wireme is a simple Information Gathering Tool written in python  🕵️ 🔎
___
# screenshots :
![N](https://i.imgur.com/TWT2rga.jpg)

## Features :

- Getting inforamtion from phone numbers
- Scan open ports Using IP addresses
- Ping any target Using IP/Website
- Extracting information from IP addresses
- Checking email validty 
- Extracting Website information

# what is information gathering :

> Information Gathering means gathering different kinds of information about the target. It is basically, the first step or the beginning stage of Ethical Hacking, where the penetration testers or hackers (both black hat or white hat) tries to gather all the information about the target, in order to use it for Hacking

for more reading click here [geeksforgeeks.Information.Gathering](https://www.geeksforgeeks.org/kali-linux-information-gathering-tools/)



## Tested On :
```sh
Ubuntu
Kali linux 
Termux
```

## Installation :

wireme requires [Python3](https://www.python.org/downloads/release/python-3810/) v3.8.10+ to run.
also You need [pip](https://pypi.org/project/pip/) v20.0.2+ to run.
Install the dependencies and devDependencies from the git clone command and the requirtment file then start the tool.

```sh
sudo apt update
git clone jndfbsbfsib
cd wireme/
pip install -r requirements.txt
python3 wireme.py
```
# Technical problems that you might face :
You might face this Error while using the tool :
```sh
AttributeError: 'module' object has no attribute 'PortScanner'
```
# solution :
You likely installed the package "nmap", not "python-nmap"
to solve this problem follow the steps below :
```sh
pip uninstall nmap
pip uninstall python-nmap
pip install python-nmap
```
That should fix the problem if it doesn't Start Troubleshooting....

# License
MIT license
