# wizfer :
----

![N|](https://i.imgur.com/uVg7nVb.png)
_____
# what is wizfer ?? :
wizfer is a simple Information Gathering Tool written in python  🕵️ 🔎
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

wizfer requires [Python3](https://www.python.org/downloads/release/python-3810/) v3.8.10+ to run.
also You need [pip](https://pypi.org/project/pip/) v20.0.2+ to run.
Install the dependencies and devDependencies from the git clone command and the requirtment file then start the tool.

```sh
sudo apt update
git clone https://github.com/rexerf16/wizfer.git
cd wizfer/
pip install -r requirements.txt
python3 wizfer.py
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

# Version :
| Version    | Featurtes                                                                                                                                                                                                                                                          |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| V('0.1.0') | The first Minor release with basic features - Getting inforamtion from phone numbers - Scan open ports Using IP addresses - Ping any target Using IP/Website - Extracting information from IP addresses - Checking email validty  - Extracting Website information |
| V('0.2.1)  | Minor relase with patch + changed the repository & the name of the project from ‘ wireme ‘ to ‘ wizfer ‘                                                                                                                                                           |
| V('1.2.1') | **WORKING ON IT ......** " Major extra key features & major patches "                                                                                                                                                                                              |

# License
MIT license

Copyright (c) 2021 Mohammed Farhan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
