# frontend app.py
from flask import Flask
import requests

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return app.send_static_file('my_index.html')

@app.route('/api')
def proxy_backend():
    r = requests.get("http://backend:5000/")  # cluster 内访问
    return r.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
