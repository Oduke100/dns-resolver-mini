import dns.resolver


def check(hostname):
#this function will use dns.resolver to look over the actual channels and give back an ip for the hostname we pass inside (hostname)

	ip=dns.resolver.resolve(hostname, "A")

	addresses=[]

	for i in ip:
		#cool thing I just learnt, okay I think I used to know part of it but today I clarified, a function has parenthesis, like it has to
		#so sth like in our case, resolve() is a function, but .address is an attribute and its written inside a package so we dont build it
		#we just use it, so .address is an attribute inside dns.resolver
		#now the append attribute is done to the list name in our case addresses and not to what you want to append
		addresses.append(i.address)

	return addresses
