#!usr/bin/env python

import MySQLdb as mdb # we can also import the MySQL C API with import _mysql

# prompts the user for an action. should return a choice
def prompt():

	# some networking required here
	return choice;

# dumps the current observation to a file (for now)
def dump(observation):

	with open("datalog.csv", 'w') as data:

		for sense in observation: 
			
			data.write(sense)
			data.write(',')		# will leave a trailing comma

		data.write('\n')

# querys the mars_oasis_project db
# accepts sql query string as argument (i.e. ("SELECT * FROM liquid_temp")
# currently just prints the result
def load(query): 

	connection = mdb.connect('mysql.topboulder.com', 'mars_jared', 'password', 'mars_oasis_project');

	with connection: # automatically connect w/ error handling 

		cursor = connection.cursor()
    		cursor.execute(query) 

		rows = cursor.fetchall() # get all the table rows

    		for row in rows:
        		print row

