#importing all required packages

from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
import numpy as np
from PIL import Image
import flask
import io


#initialising flask and model
app = flask.Flask(__name__)
model = MobileNetV2(weights='imagenet')

@app.route('/predict', methods = ['GET', 'POST'])
def upload_and_predict():
    if flask.request.method == 'POST':
        #Image preprocessing
        img = flask.request.files["image"].read()
        img = Image.open(io.BytesIO(img))
        img = img.resize((224,224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        #Model prediction
        preds = model.predict(x)
        prediction = decode_predictions(preds, top=1)[0][0][1]
        print(prediction)
        return flask.jsonify(prediction)
    else:
        answer = 'Please, submit an image with POST method'
        return flask.jsonify(answer)

#Rinning the server
if __name__ == "__main__":
        app.run('0.0.0.0', '5000')
