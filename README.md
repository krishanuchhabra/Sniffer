# Packet Sniffer
Sniffer in python using raw sockets. Using raw sockets, the packet is directly transferred from the device driver to the application layer. The application gets the packet with all the headers ( Ethernet, IP, TCP). The packet is analyzed henceforth, and the header values of each component is checked. Modules used are socket, binascii and struct. 
