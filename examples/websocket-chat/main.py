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
        clients[self.id] = self
        self.write_message(json.dumps({'type': 'join', 'id': self.id}))

    def on_message(self, msg):
        global clients
        update = json.dumps({'type': 'msg', 'id': self.id, 'msg': msg})
        for client in clients.values():
            client.write_message(update)

    def on_close(self):
        if self.id in clients:
            del clients[self.id]


app = web.Application([
    (r'/', IndexHandler),
    (r'/socket', SocketHandler),
], static_path=path.join(path.dirname(__file__), 'static'))

if __name__ == '__main__':
    hidden = HiddenService()
    print(hidden.onion)
    app.listen(hidden.port)
    try:
        ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        ioloop.IOLoop.instance().stop()

