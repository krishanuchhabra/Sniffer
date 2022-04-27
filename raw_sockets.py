#!/usr/bin/env python

import socket
import binascii
import struct

rawSocket = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.htons(0x0800))

pkt = rawSocket.recvfrom(2048)

ethernetHeader = pkt[0][0:14]

eth_hdr = struct.unpack("!6s6s2s", ethernetHeader)

print binascii.hexlify(eth_hdr[0])
print binascii.hexlify(eth_hdr[1])
binascii.hexlify(eth_hdr[2])

ipHeader = pkt[0][14:34]
ip_hdr = struct.unpack("!12s4s4s", ipHeader)

print "Source IP: " + socket.inet_ntoa(ip_hdr[1])

print "Destination IP:" +socket.inet_ntoa(ip_hdr[2])

tcpHeader = pkt[0][34:54]

tcp_hdr = struct.unpack("!HH16s", tcpHeader)


