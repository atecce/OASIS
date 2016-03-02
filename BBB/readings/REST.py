# need this for curl command
import os

# need this for json formatting
import json

class REST:

	# url for website
	url = "https://cumarsoasis.firebaseio.com/"

	def __init__(self, url):

		# set url for backend
		self.url = url

	def POST(self, entry, table):

		print "curl -X POST -d '" + json.dumps(entry) + "' '" + url + table + "'"

		# wrap the bash command with python
		os.system("curl -X POST -d '" + json.dumps(entry) + "' '" + url + table + "'")
