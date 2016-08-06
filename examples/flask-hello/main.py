from flask import Flask
from shh import HiddenService

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello onion!'

hidden = HiddenService()
print hidden.onion

app.run(port=hidden.port)