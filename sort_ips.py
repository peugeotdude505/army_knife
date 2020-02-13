#Sorts a list of IP Addresses in Ascending order.
#Code is adapted from https://stackoverflow.com/questions/6545023/how-to-sort-ip-addresses-stored-in-dictionary-in-python
#See also https://docs.python.org/3/library/socket.html#socket.inet_aton

import socket

results = []

with open('hosts_to_sort.txt') as f:
    for line in f:
        info = line.split()
        results.append((info[0],info[1]))


#See also https://docs.python.org/3/library/socket.html#socket.inet_aton
for (ip, hostname) in sorted(results, key=lambda item: socket.inet_aton(item[0])):
    print ((ip.ljust(20,' ')), ' ' ,(hostname.ljust(30,' ')),)
    