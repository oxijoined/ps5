import http.server, ssl, time #, cgi

from http.server import BaseHTTPRequestHandler, SimpleHTTPRequestHandler, HTTPServer

class RequestHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        tn = self.path.lstrip('/document/en/ps5/')
        #print('!POST!: tn:\n'  + tn)
        fn = tn + '.bin' # '.json'
        if (not tn.startswith("T_")):
        	if (fn!="a.bin"):
        		print('!POST!: INFO: '  + str(self.rfile.read(int(self.headers['Content-length']))),"utf-8")
        		return
        	else:
        		fn = time.strftime("%Y%m%d-%H%M%S") + ".json"

        print('!POST!: ' + self.path + ' -->> ' + fn)
        print('test: %d'%int(self.headers['Content-length']))
        data = self.rfile.read(int(self.headers['Content-length']))
        open("%s"%fn, "wb").write(data)


server_address = ('0.0.0.0', 443)
httpd = HTTPServer(server_address, RequestHandler) #http.server.SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='localhost.pem', ssl_version=ssl.PROTOCOL_TLS)
print('running server')
httpd.serve_forever()
