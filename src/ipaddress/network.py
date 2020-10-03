'''
author: Rodrigo Dal Ri
email: rodrigodalri1995@gmail.com
'''

from ipaddress import IPv4Address, IPv4Network, IPv4Interface, IPV4LENGTH


def main():

    # IPv4 Address
    addr = IPv4Address("189.6.233.225")
    print(f"my address: {addr}")

    addrInt = int(addr)
    print(f"my address(int): {addrInt}")

    addrBytes = addr.packed
    print(f"my address(bytes): {addrBytes}")

    addrHash = hash(addr)
    print(f"my address hash: {addrHash}")

    print("\n")

    # IPv4 Networks
    net = IPv4Network("192.168.0.0/24")
    print(f"my network: {net}")

    nAddr = net.num_addresses
    print(f"n addresses: {nAddr}")

    netPLen = net.prefixlen
    print(f"prefix len: {netPLen}")

    netMask = net.netmask
    print(f"prefix len: {netMask}")

    netBroadcast = net.broadcast_address
    print(f"broadcast: {netBroadcast}")

    addr1 = IPv4Address("192.168.0.10") in net
    print(f"addr1 is in net: {addr1}")

    addr2 = IPv4Address("192.168.1.10") in net
    print(f"addr2 is in net: {addr2}")

    small_net = IPv4Network("192.0.2.0/28")
    big_net = IPv4Network("192.0.0.0/16")

    bool1 = small_net.compare_networks(big_net)
    print(f"small is subnet of big: {bool1}")
    bool2 = big_net.compare_networks(small_net)
    print(f"big is supernet of small: {bool2}")

    print("\n")

    # IPv4 Interfaces
    ifc = IPv4Interface("192.168.0.10/24")
    print(f"my interface: {ifc}")

    hostIfc = ifc.ip 
    print(f"host ifc: {hostIfc}")

    netIfc = ifc.network  
    print(f"network ifc: {netIfc}")

if __name__ == '__main__':
    main()