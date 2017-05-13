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

args = parser.parse_args()

if args.port is None:
    port = shh.utils.find_port()
else:
    port = args.port
print('Local port: {}'.format(port))

print('Creating hidden service...')
hidden = shh.HiddenService(ports={80: port}, key_file=args.key)
print('Serving at: ' + hidden.onion)

while True:
    time.sleep(10)
