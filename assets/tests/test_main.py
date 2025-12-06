def main():
	serverCreate(IP, PORT)
	hostConnect(IP, PORT)
	roleSelect(Roles)
	findContent(Database)
	deliverContent(Content, IP, PORT)

def roleSelect(Roles):
	for role in Roles:
		if role == match:
			role.set()

def findContent(Database):
	for type, content in Database:
		if type == role:
			return content
def deliverContent(Content, IP, PORT):
	content.send(IP, PORT)
def serverCreate(IP, PORT):
	server.start(IP, PORT)
def hostConnect(IP, PORT):
	host.connect(IP, PORT)