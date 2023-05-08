import http.server
import http.client
import socketserver
import time

# Servers with their port numbers
servers = [
	('localhost', 8000),
	('localhost', 8001),
	('localhost', 8002),
	('localhost', 8003),
	('localhost', 8004)
]

# Chain of servers for chained failover load balancing
server_chain = [
    [('localhost', 8000), ('localhost', 8001), ('localhost', 8002)],
    [('localhost', 8003), ('localhost', 8004)]
]

# Dictionary of server weights
server_weights = {'8000': 2, '8001': 1, '8002': 3, '8003': 2, '8004': 1}

next_chain_index = 0

next_server_index = 0

def round_robin():
	global next_server_index
	assigned_server = servers[next_server_index]
	next_server_index = (next_server_index + 1) % len(servers)
	return assigned_server

def weighted_round_robin():
	global next_server_index
	weighted_servers = []
	for server in servers:
		weighted_servers.extend([server] * server_weights[str(server[1])])
	assigned_server = weighted_servers[next_server_index]
	next_server_index = (next_server_index + 1) % len(weighted_servers)
	return assigned_server
	
def least_time():
	# Find server having minimum response time
	min_response_time = float('inf')
	assigned_server = None
	for server in servers:
		conn = http.client.HTTPConnection(server[0], server[1])
		start_time = time.time()
		conn.request('GET', '/')
		response = conn.getresponse()
		end_time = time.time()
		if response.status == 200:
			response_time = end_time - start_time
			if response_time < min_response_time:
				min_response_time = response_time
				assigned_server = server
		conn.close()
	if assigned_server is None:
		assigned_server = servers[0]
	return assigned_server

def chained_failover():
	global next_chain_index, next_server_index
	while True:
		assigned_server_chain = server_chain[next_chain_index]
		assigned_server = assigned_server_chain[next_server_index]
		next_server_index = (next_server_index + 1) % len(assigned_server_chain)
		conn = http.client.HTTPConnection(assigned_server[0], assigned_server[1])
		conn.request('GET', '/healthcheck')
		response = conn.getresponse()
		if response.status == 200:
			conn.close()
			return assigned_server
		elif next_server_index == 0:
			next_chain_index = (next_chain_index + 1) % len(server_chain)
		conn.close()
		
#Handle requests by selecting load balancing algorithm based on user's choice 
class RequestHandler(http.server.SimpleHTTPRequestHandler):
	def do_GET(self):
		if user_choice == 1:
			# Fetch the assigned server using the round robin algorithm
			assigned_server = round_robin()
		elif user_choice == 2:
			# Fetch the assigned server using the weighted round robin algorithm
			assigned_server = weighted_round_robin()
		elif user_choice == 3:
			# Fetch the assigned server using the least time algorithm
			assigned_server = least_time()
		elif user_choice == 4:
			# Fetch the assigned server using the chained failover algorithm
			assigned_server = chained_failover()
		print(f"Request received, forwarding to server {assigned_server[0]}:{assigned_server[1]}")
		# Forward the request to the assigned server
		conn = http.client.HTTPConnection(assigned_server[0], assigned_server[1])
		conn.request(self.command, self.path)
		# Fetch the response from the assigned server
		response = conn.getresponse()
		self.send_response(response.status)
		for header, value in response.getheaders():
			self.send_header(header, value)
		self.end_headers()
		self.copyfile(response, self.wfile)
		conn.close()

# Start the load balancer by reserving a port number for the load balancer
port = 8080



with socketserver.ThreadingTCPServer(('', port), RequestHandler) as httpd:
	print(f"Load balancer on port {port}")
	user_choice = int(input("Please enter your choice of load balancing algorithm: \n 1 for Round Robin \n 2 for Weighted Round Robin \n 3 for Least Time \n 4 for Chained Failover \n"))
	httpd.serve_forever()
	
