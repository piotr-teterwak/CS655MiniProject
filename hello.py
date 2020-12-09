from flask import Flask, render_template,request
import requests
import random
app = Flask(__name__)


servers = ['192.12.245.174']

@app.route('/', methods=['GET'])
def submit_page():
    return render_template('index.html')

@app.route('/submit', methods=["POST","GET"])
def hello_world():
    image = request.files.get("image")
    payload = {"image":image}
    server_idx = random.randint(0,len(servers)-1)
    r = requests.post('http://{}:5000/predict'.format(servers[server_idx]), files=payload).text
    return r
