import shh
from argparse import ArgumentParser
try:
    from socketserver import TCPServer
except ImportError:
    from SocketServer import TCPServer
try:
    from http.server import SimpleHTTPRequestHandler
except:
    from SimpleHTTPServer import SimpleHTTPRequestHandler

parser = ArgumentParser()
parser.add_argument('-p', '--port', default=None, type=int)
parser.add_argument('-k', '--key', default=None, type=str)
args = parser.parse_args()

if args.port is None:
    port = shh.utils.find_port()
else:
    port = args.port
print('Using local port: {}'.format(port))

server = TCPServer(('', port), SimpleHTTPRequestHandler)

print('Creating hidden service...')
hidden = shh.HiddenService(port, key_file=args.key)

print('Serving at: ' + hidden.onion)
server.serve_forever()

