import socket
import socks

class Proxy:

    def __init__(self, host='127.0.0.1', port=9050):
        self.host = host
        self.port = port

    def __enter__(self):
        # Save original methods
        self._socket = socket.socket
        self._getaddrinfo = socket.getaddrinfo
        # Configure socks proxy
        socks.set_default_proxy(socks.SOCKS5, self.host, self.port)
        socket.socket = socks.socksocket
        # Patch domain lookup
        socket.getaddrinfo = _getaddrinfo

    def __exit__(self, type, value, traceback):
        # Restore original methods
        socket.socket = self._socket
        socket.getaddrinfo = self._getaddrinfo


def _getaddrinfo(host, port, *args):
    # https://docs.python.org/3/library/socket.html#socket.getaddrinfo
    sockaddr = (host, port)
    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', sockaddr)]
