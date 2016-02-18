import MySQLdb as mdb
import datetime
from ie_oxy import O2Percent
import threading
def writeToDB():
	threading.Timer(1800,writeToDB).start()
	time = str(datetime.datetime.now())
	connection = mdb.connect('mysql.topboulder.com', 'mars_jared', 'password', 'mars_oasis_project')
	cursor = connection.cursor()
	value = round(O2Percent,4)
	SysID = "S304"
	unit = "%"
	sensor_type = "ADC"
	with connection:
		cursor = connection.cursor()
		sql = ("INSERT INTO O2(value, time, SysID, unit, sensor_type) VALUES(%s,%s,%s,%s, %s)")
		values = (value,time,SysID, unit, sensor_type)
		cursor.execute(sql,values)

def main():
	print "Starting..."
	writeToDB()
	


if __name__ == '__main__':
	main()

