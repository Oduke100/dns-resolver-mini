import os
import json
import sqlite3

database_path=os.path.expanduser("~/sandbox/dns-resolver-mini/dns.db")

def get_conn():
	conn=sqlite3.connect(database_path)
	return conn
#the sqlite3.connect command pointed to our db path is what opens the connection everytime we need one and returns the component(the open connection)



def init_db():
	db=get_conn()
	cursor=db.cursor()
	cursor.execute(
		"CREATE TABLE IF NOT EXISTS dns (key TEXT PRIMARY KEY, value TEXT, metadata TEXT)"
		)
	db.commit()
	db.close()


#the init_db() function is the ignition to our db this is the initialization of the db as the name suggests
"""
	the syntax: 
		-now here is where we actually learn. The syntax makes a get_connection call as you can see in line 15 this makes our init function use the
		connection created and returned by the first function.
		-after the connection call we do a cursor call to get the cursor, its done to the db and saved too for future use, per Claude, cursor is
		used to run commands and get back replies via the connection pipeline so we need it big-time
		-after saving the cursor we call a cursor.execute() which from the explanation I have just given means we are telling the cursor, 
		execute all that you see inside this brackets
		-then the commit function and the close functions(self explanatory) and run on the database not the cursor
		so far the code just checks if the dns table exists and if not it writes a new one, just that
		-all SQL commands inside the exec function MUST be quoted or they will be read as python commands and throw an error
		NOTE: cursor only runs execute as its the pipeline manager, all else is run on the db
"""


def set_dns(key, value, metadata):
# this function will be identical to the init_db function
	db=get_conn()
	cursor=db.cursor()
	cursor.execute(
		"INSERT INTO dns (key, value, metadata) VALUES (?, ?, ?)", (key, value, metadata)
		)
	db.commit()
	db.close()

def get_all():
#this will follow the same convention we have rn only it wont have a commit as no data is being changed

	db=get_conn()
	cursor=db.cursor()
	cursor.execute(
		"SELECT * FROM dns"
		)
	rows=cursor.fetchall()
	db.close()
	return rows

def get_dns(key):
#this will sort through the db for the key we pass, I intend to swap it with an algo but for now we will use this one

	db=get_conn()
	cursor=db.cursor()
	cursor.execute(
		"SELECT * FROM dns WHERE key = ?", (key, )
		)
	row=cursor.fetchone()
	db.close()
	return row


def delete_dns(key):
#this will be responsible for the deletes as the name confirms
#just a quick note in SQL the delete syntax is just DELETE FROM {tablename} WHERE {column-name} is {value} it does not use a * as in select for the search

	db=get_conn()
	cursor=db.cursor()
	cursor.execute(
		"DELETE FROM dns WHERE key = ?", (key, )
		)
	db.commit()
	db.close()
	return {"message": "dns record successfully deleted"}


"""
this is the complete file with the  CRUD functions and the necessary stuff for the db config

now there is a reason for the ? and passing the values separately, the reason is for safety against Injection, also to prevent data manipulation and corruption
from bad writes in the direct SQL writes, so thats why, its better for security and preservation of ourselves in future, I think thats what I got
"""


