def find_port(start=1024, end=49151):
    ''' Loop over ports looking for an open one '''
    from socket import socket
    sock = socket()
    for port in range(start, end):
        try:
            sock.bind(('127.0.0.1', port))
        except:
            continue
        return port
    raise Error('No ports available')
