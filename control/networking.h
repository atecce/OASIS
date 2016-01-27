// prompts the user for an action. should return a choice
void prompt() {

	// some networking required here
	return choice;
}

// dumps the current observation into a database
void dump(float *observation) {

	// some networking required here
}

// loading data from db (this example should help with writing to db eventually)
void load() {
	// interacting with mysql requires the mysql.h header file
	// do we want to include that file in this file or in the control loop file?
	
	MYSQL     *conn;
	MYSQL_RES *res;
	MYSQL_ROW *row;

	char *server   = "server";
	char *user     = "username";
	char *password = "password";
	char *database = "local"; // for now
	
	conn = mysql_init(NULL);
	mysql_real_connect(conn, server, user, password, database, 0, NULL, 0);
	
	mysql_query(conn, "SELECT * FROM website"); // get all the data
	
	res = mysql_use_result(conn);
	while ((row = mysql_fetch_row(res)) != NULL)
	{
		printf(row);
	}
	mysql_free_result(res);
	mysql_close(conn);
}
