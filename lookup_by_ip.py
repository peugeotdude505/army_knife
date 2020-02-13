import socket
#Get the DNS hostname for a list of a IPv4 adresses

results = []
output = open('hostnames_output.txt',"w+")

with open('hostnames_list.txt') as f:
    for ipadd in f:
        try:
            host = (ipadd.split())
            ipv4 = host[0] 
            info = socket.gethostbyaddr(ipadd)
            line = str(ipv4 + '  ' +str(info[0]))
            
        except socket.herror:
            line = (ipv4 + "  No DNS record was found ")
            print(line)
        
        except socket.gaierror:
            print("Error or EOF reached.")
            break
            
        output.write(str(line) + '\n')
  
  
output.close()   