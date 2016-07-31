from flask import Flask
import good as G

from flask_pygood.flask_pygood import EndpointDecorator as endpoint

app = Flask(__name__)

@app.route('/')
@endpoint(G.Schema({}))
def hello_world():
    return 'Hello, World!'

app.run()
