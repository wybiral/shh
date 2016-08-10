import shh
import time
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '-p',
    '--port',
    default=None,
    type=int,
    help='local port to serve through Tor (otherwise random)',
)
parser.add_argument(
    '-k',
    '--key',
    default=None,
    type=str,
    help='key file to use (will generate if not found)',
)
parser.add_argument(
    '-s',
    '--server',
    default=False,
    action='store_true',
    help='create a basic file server as hidden service',
)
args = parser.parse_args()

if args.port is None:
    port = shh.utils.find_port()
else:
    port = args.port
print('Local port: {}'.format(port))

print('Creating hidden service...')
hidden = shh.HiddenService(port, key_file=args.key)
print('Serving at: ' + hidden.onion)

if args.server:
    try:
        from socketserver import TCPServer
    except ImportError:
        from SocketServer import TCPServer
    try:
        from http.server import SimpleHTTPRequestHandler
    except:
        from SimpleHTTPServer import SimpleHTTPRequestHandler
    print('Serving current directory')
    server = TCPServer(('', port), SimpleHTTPRequestHandler)
    server.serve_forever()
else:
    while True:
        time.sleep(1);
