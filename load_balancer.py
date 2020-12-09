from flask import Flask, render_template,request
import requests
import random
application = Flask(__name__)


#servers = ['192.12.245.174','192.12.245.175','192.12.245.176','192.12.245.177']
servers = ['10.10.1.1','10.10.2.1','10.10.3.1','10.10.4.1']

@application.route('/', methods=['GET'])
def submit_page():
    return render_template('index.html')

@application.route('/submit', methods=["POST","GET"])
def hello_world():
    image = request.files.get("image")
    payload = {"image":image}
    if request.form.get("number_backend_servers"):
        num_servers = int(request.form.get("number_backend_servers")) - 1
    else:
        num_servers = len(servers)-1
    server_idx = random.randint(0,num_servers)
    r = requests.post('http://{}:5000/predict'.format(servers[server_idx]), files=payload).text
    return r
    #return "Hello, world!"

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000, threaded=True)
