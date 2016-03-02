class REST:

	def __init__(self, url):

		# set url for backend
		self.url = url

	def POST(self, entry, database):

		# will be os.write command
		print "curl -X POST -d '" + str(entry) + "' '" + url + database + "'"

# set url
url = "https://cumarsoasis.firebase.com/"

# create REST object
backend = REST(url)

# POST
entry = {'user_id': 'jack', 'text': 'Ahoy!'}

database = "message_list.json"

print
backend.POST(entry, database)
print
