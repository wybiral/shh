import json
from os import path
from tornado import websocket, web, ioloop
from shh import HiddenService

next_id = 1
clients = {}

class IndexHandler(web.RequestHandler):

    def get(self):
        self.render('index.html')


class SocketHandler(websocket.WebSocketHandler):

    def check_origin(self, origin):
        return True

    def open(self):
        global next_id
        global clients
        self.id = next_id
        next_id += 1
        broadcast({'type': 'join', 'id': self.id})
        clients[self.id] = self
        self.write_message(json.dumps({'type': 'welcome', 'id': self.id}))

    def on_message(self, msg):
        global clients
        msg = msg.strip()
        if 0 < len(msg) <= 140:
            broadcast({'type': 'msg', 'id': self.id, 'msg': msg})

    def on_close(self):
        if self.id in clients:
            del clients[self.id]
            broadcast({'type': 'leave', 'id': self.id})


def broadcast(evt):
    data = json.dumps(evt)
    for client in clients.values():
        client.write_message(data)


app = web.Application([
    (r'/', IndexHandler),
    (r'/socket', SocketHandler),
], static_path=path.join(path.dirname(__file__), 'static'))

if __name__ == '__main__':
    hidden = HiddenService()
    print(hidden.onion)
    port = hidden.ports[80]
    app.listen(port)
    try:
        ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        ioloop.IOLoop.instance().stop()

