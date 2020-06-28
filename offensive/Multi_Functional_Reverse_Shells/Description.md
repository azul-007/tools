# Project Description

In this project I will create my own reverse shell based on the TCP client and TCP server.
This project is based on two programs: the client and server. The client will listen for the
incoming connection and the server will issue the payload. This project will be using Python 2.7

## Wine & Pyinstaller installation

**Add architecture to 32bit**
````
dpkg --add-architecture i386
````


**Update Respositories**
````
apt-get update
````

**Install Wine32**
````
apt-get install wine32
````
This will allow us to run Windows commands in Linux

Go to the root directoryand you will see a .wine directory. This is where the "C" drive will be located.

**Install Python27**
1) python.org/downloads/release/python-2714/
2) Windows x86 MSI installer
3) wine msiexec /i python-2.7.14.msi
4) After it is installed, under the .wine folder, you will see 'Python27' directory successfully installed.

**Install Pyinstaller**
````
wine /path/to/.wine/drive_c/Python27/python.exe -m pip install pyinstaller
````
> This library will allow us to compile python code into .exe files

