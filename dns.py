from database import  set_dns, get_all, get_dns, delete_dns
from database import init_db

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
			print(record)

		elif parts[0]=="rem":
			delete_dns(parts[1])

			print(f"dns with key: {parts[1]} deleted successfully")

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
