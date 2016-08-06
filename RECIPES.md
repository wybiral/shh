## Serve Flask app
```python
from flask import Flask
from shh import Hidden

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello onion!'

port = 5000
hidden = Hidden(port)
print hidden.onion

app.run(port=port)
```
