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
        self.id = 'anon{}'.format(next_id)
        next_id += 1
        broadcast({'type': 'join', 'id': self.id})
        clients[self.id] = self
        self.write_message(json.dumps({'type': 'welcome', 'id': self.id}))
        self.send_list()

    def send_list(self):
        global clients
        ids = list(clients.keys())
        ids.sort()
        self.write_message(json.dumps({'type': 'list', 'ids': ids}))

    def on_message(self, msg):
        try:
            self.handle_message(json.loads(msg))
        except Exception as e:
            print(e)
            self.close()

    def handle_message(self, msg):
        global clients
        type = msg['type']
        if type == 'msg':
            body = msg['body']
            broadcast({'type': 'msg', 'id': self.id, 'body': body})
        elif type == 'list':
            self.send_list()
        elif type == 'name':
            oldid = self.id
            newid = msg['id']
            if newid not in clients:
                del clients[oldid]
                clients[newid] = self
                self.id = newid
                broadcast({'type': 'name', 'old': oldid, 'new': newid})

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
