from tornado import ioloop, web
from shh import HiddenService

class MainHandler(web.RequestHandler):
    def get(self):
        self.write('Hello onion!')

hidden = HiddenService()
print(hidden.onion)

app = web.Application([
    (r"/", MainHandler),
])

port = hidden.ports[80]
app.listen(port)
try:
    ioloop.IOLoop.instance().start()
except KeyboardInterrupt:
    ioloop.IOLoop.instance().stop()