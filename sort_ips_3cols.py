#Sorts a list of IP Addresses in Ascending order.
#Code is adapted from https://stackoverflow.com/questions/6545023/how-to-sort-ip-addresses-stored-in-dictionary-in-python
#See also https://docs.python.org/3/library/socket.html#socket.inet_aton

import socket

output = open('sorted_output.txt',"w+")
results = []
counter = 0

with open('hosts_to_sort.txt') as f:
    for line in f:
        info = line.split()
        counter = counter+1
            try:
                results.append((info[0],info[1],info[2]))
            except IndexError:
                print('Bad input at line ', counter)


#See also https://docs.python.org/3/library/socket.html#socket.inet_aton
for (ip, hostname,dns) in sorted(results, key=lambda item: socket.inet_aton(item[0])):
    
    print ((ip.ljust(20,' ')), ' ' ,(hostname.ljust(30,' ')), ' ' ,dns)
    output.write ((ip.ljust(20,' ')) + ' # ' + (hostname.ljust(30,' ')) + ' ' + dns + '\n')
  
  
output.close()