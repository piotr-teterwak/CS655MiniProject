from flask import Flask
app = Flask(__name__)

@app.route('/submit', methods=["POST","GET"])
def hello_world():
    app.logger.info("SUCCESS")
    return 'Hello, World!'
