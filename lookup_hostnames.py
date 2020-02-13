import socket

results = []

with open('hostnames_list.txt') as f:
    for hostname in f:
        try:
            ip = socket.gethostbyname(hostname.strip())
        except socket.gaierror:
            ip = socket.gethostbyname('.'.join(hostname.strip().split('.')[1:]))
        results.append((ip, hostname.strip()))

for (ip, hostname) in sorted(results, key=lambda item: socket.inet_aton(item[0])):
    print ((ip.ljust(20,' ')), ' ' ,(hostname.ljust(30,' ')))
	