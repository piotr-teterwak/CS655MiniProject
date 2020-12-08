from flask import Flask, render_template,request
import requests
app = Flask(__name__)

@app.route('/', methods=['GET'])
def submit_page():
    return render_template('index.html')

@app.route('/submit', methods=["POST","GET"])
def hello_world():
    image = request.files.get("image")
    payload = {"image":image}
    requests.post('http://192.12.245.174:5000/predict', files=payload).json()
    return r
