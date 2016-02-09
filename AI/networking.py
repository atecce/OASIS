#!usr/bin/env python

import MySQLdb as mdb # we can also import the MySQL C API with import _mysql

# prompts the user for an action. should return a choice
def prompt():

	# some networking required here
	return choice

# dumps the current observation to a file (for now)
def dump(observation): 

	with open("datalog.csv", 'w') as data:

		for sense in observation: 
			
			data.write(sense)
			data.write(',')		# will leave a trailing comma

		data.write('\n')

# dumps current observation to mysql db
# arguments must be strings 
def dump_to_db(table, row, observation):
	
	# logs in to database
	connection = mdb.connect('mysql.topboulder.com', 'mars_jared', 'password', 'mars_oasis_project'); # we should have a master user for this
	
	# open connection 
	with connection: 
	
		# set up cursor
		cursor = connection.cursor()
		
		try:
		
			# add entry to database
			cursor.execute( "INSERT INTO "
					+ table
					+ "("+row+") "
					+ "VALUES"
					+ "("+observation+")" )

		# catch database errors
		except mdb.Error, e:
  
			# display error
    			print "Error %d: %s" % (e.args[0], e.args[1])

			# potentially don't want to exit
    			sys.exit(1)

		finally:

			if connection: connection.close()

# querys the mars_oasis_project db
# accepts sql query string as argument (i.e. ("SELECT * FROM liquid_temp")
# currently just prints the result
def load(query): 

	connection = mdb.connect('mysql.topboulder.com', 'mars_jared', 'password', 'mars_oasis_project');

	with connection: # automatically connect w/ error handling 

		try:
		
			cursor = connection.cursor()
    			cursor.execute(query) 

			rows = cursor.fetchall() # get all the table rows

    			for row in rows:
        			print row
		
		except mdb.Error, e:
  
    			print "Error %d: %s" % (e.args[0],e.args[1])
    			sys.exit(1)

		finally:

			if connection:
				connection.close()

