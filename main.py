from database import  set_dns, get_all, get_dns, delete_dns
from checker import check
from database import init_db


#another gotcha I came across is that when any filename in your codebase matches the library you are trying to import, python throws an error coz it checks
#your file first before checking the library, always name the files differently and preferrably further away from library packages you will use
init_db()

try:
	while True:
		command=input("dns> ")

		parts=command.split()
		parts[0].lower()

		if parts[0]=="insert":
			set_dns(parts[1], parts[2], parts[3])
			print(f"dns created. Key:{parts[1]}")

		elif parts[0]=="gall":
			records=get_all()
			print(records)

		elif parts[0]=="gdns":
			record=get_dns(parts[1])

			if record is not None:
				print(record)

			elif record is None:
				md=parts[1].split()

				addresses=check(parts[1])
				#we had to add an enumarate attribute for the dns lookups with more than one address this allows us to store them numbered
				#like pinterest1, pinterest2 and so on

				for index, a in enumerate(addresses):

					set_dns((parts[1] + str(index)), a, md[0])

					print(f"The address for the domain-name: {parts[1]} is {a}")

		elif parts[0]=="rem":
			delete_dns(parts[1])

			print(f"dns with key: {parts[1]} deleted successfully")

#		elif parts[0]=="resolve":
#			check(parts[1])

#			print(f"address for the key: {parts[1]} is: ")

		elif parts[0]=="help":
			print("""
			dns takes the following command format:

			[argument] [values]

			arguments; 
				insert-to create a dns record
				gall-to get all dns records in storage
				gdns-to get a specific dns record and value is passed after the argument
				rem-to remove a dns record and the key is supplied 

			values:
				insert takes three values in the following order:
					first is the key(ie, google.com)
					second is the address/value(ie, 1.1.1.1)
					third is the metadata(simple one word like: google)

			exit is the hard exit command.
				""")


		elif  command=="exit":
			break

except KeyboardInterrupt:
		print("\nExiting...")
