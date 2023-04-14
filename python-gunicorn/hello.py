from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World>'

def init_app(app):
    app.wsgi_app = ProxyFix(app.wsgi_app)

init_app(app)

