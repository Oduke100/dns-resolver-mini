import json
import dns.resolver

exit_code = 0
filepath  = "ips.json"

while exit_code == 0:
    with open(filepath, "a") as file:
        file.close()

    data       = input("DNS >>>> ")
    data_parts = data.split(" ", maxsplit=1)

    argument   = data_parts[0]

    if argument == "status":
        print("Resolver is up and running!")

    elif argument == "oduke":
        print("Yes Master, at your service!!")

    elif argument == "find":
        flag        = False
        domains     = data_parts[1].split(", ")
        dns_records = []
        
        with open(filepath, "r") as file:
            for f in file:
                dns_records.append(json.loads(f))

        for domain in domains:
            if any(d["domain_name"] == domain for d in dns_records):
                flag = True
            else:
                flag = False
            
        if flag == True:
            for domain in domains:
                for d in dns_records:
                    if domain == d["domain_name"]:
                        print(f"""domain_name : {domain}\ndomain_addresses : {d["domain_addresses"]}""")
                        
        else:        
            domain_record = {}

            for domain in domains:
                addresses     = []
                domain_addresses = dns.resolver.resolve(domain, "A")
            
                for address in domain_addresses:
                    addresses.append(address.address)
                
                domain_record = {
                    "domain_name"      : domain,
                    "domain_addresses" : addresses 
                }
                
                with open(filepath, "a") as file:
                    json.dump(domain_record, file)
                    file.write("\n")
                    
                print(f"""domain_name : {domain}\ndomain_addresses : {addresses}""")
                        
            print("Domain recorded!")

    elif argument == "resolve":
        dns_records = []
        domains = data_parts[1].split(", ")

        with open(filepath, "r") as file:
            for f in file:
                dns_records.append(json.loads(f))

        for domain in domains:
            for d in dns_records:
                if domain == d["domain_name"]:
                    print(f"""domain_name : {domain}\ndomain_addresses : {d["domain_addresses"]}""")
                    
    elif argument == "dns-logs":
        dns_records = []
        with open(filepath, "r") as file:
            for f in file:
                dns_records.append(f.strip())

        for d in dns_records:
            print(d)
        
    elif argument == "exit":
        print("Exitting DNS-resolver-mini gracefully!")
        exit_code = 1

    else:
        print("enter a valid command or type help for help -- NOT YET IMPLIMENTED!!!")
