# ipaddress

Code for playing with Python’s ipaddress module.

Features:
- IPv4 Address 
- IPv4 Networks  
- IPv4 Interfaces
 

Checking funcionality
```
$ python3 network.py 
my address: 189.6.233.225
my address(int): 3171346913
my address(bytes): b'\xbd\x06\xe9\xe1'
my address hash: -5759520378644387949


my network: 192.168.0.0/24
n addresses: 256
prefix len: 24
prefix len: 255.255.255.0
broadcast: 192.168.0.255
addr1 is in net: True
addr2 is in net: False
small is subnet of big: 1
big is supernet of small: -1


my interface: 192.168.0.10/24
host ifc: 192.168.0.10
```

This code focuses on Internet Protocol version 4 (IPv4) addresses. There are also IPv6 addresses. Since the arithmetic of addresses is largely the same, this tutorial cuts one variable out of the equation and focuses on IPv4 addresses.