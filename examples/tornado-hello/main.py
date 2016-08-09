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

app.listen(hidden.port)
try:
    ioloop.IOLoop.instance().start()
except KeyboardInterrupt:
    ioloop.IOLoop.instance().stop()