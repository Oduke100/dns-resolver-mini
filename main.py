import dns.resolver

exit_code = 0

while exit_code == 0:
    command = input("DNS >>>  ")
    
    words = command.split(" ", maxsplit=1)
    arg   = words[0]
    
    if arg == "find":
        domains = words[1].split(", ")
        addresses = []
        
        for d in domains:
            ip_addresses = []
            domain_addresses = dns.resolver.resolve(d, "A")
            for ip_address in domain_addresses:
                ip_addresses.append(ip_address.address)

            addresses.append(ip_addresses)

        for a in addresses:
            for ip in a:
                print(ip)
        
    if arg == "exit":
        print("Exiting dns-resolver-mini gracefully!")
        exit_code = 1

        

        


