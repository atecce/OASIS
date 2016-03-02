# need this for curl command
import os

# need this for json formatting
import json

class REST:

	# url for website
	url = "https://cumarsoasis.firebaseio.com/"

	def PUT(self, entry, table):

		# wrap the bash command with python
		os.system("curl -X PUT -d '" + json.dumps(entry) + "' '" + self.url + table + "'")

	def PATCH(self, entry, table):

		# wrap the bash command with python
		os.system("curl -X PATCH -d '" + json.dumps(entry) + "' '" + self.url + table + "'")
