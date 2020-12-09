#importing all required packages
import tensorflow as tf
import os
import json
import ast
from PIL import Image
import numpy as np

from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions

# This simple fucntion crop largest possible square from a given PIL image
def crop_square(pil_img):
    img_width, img_height = pil_img.size
    crop = min(img_width, img_height)
    return pil_img.crop(((img_width - crop) // 2,
                         (img_height - crop) // 2,
                         (img_width + crop) // 2,
                         (img_height + crop) // 2))

if __name__ == "__main__":
    #Path to images on my machine, this need to be substituted
    path_to_images = '../unknown_label/'
    filelist = os.listdir(path_to_images)
    
    #Getting true labels is not very easy, it requries two mappings
    with open('../ILSVRC2012_validation_ground_truth.txt', 'r') as f:
        l2 = f.readlines()
    ld2 = {i:int(l2[i-1].strip()) for i in range(1, len(l2)+1)}
    with open('labels_dict.txt', 'r') as f:
        l3 = f.readlines()    
    df = {int(i.split(' ')[1]) : i.split(' ')[2].strip() for i in l3}
    
    #Specifying sized we want to try
    SIZES = (16, 32, 64, 96, 128, 224)
    
    #Loading model
    model = MobileNetV2(weights='imagenet')
    
    #Below is accuracy calculation loop
    for size in SIZES:
        counter = 0
        downsample_size = (size,size)
        for file in filelist:
            #Getting image
            img = Image.open('../unknown_label/' + file)
            if img.mode != "RGB":
                img = img.convert("RGB")
                
            #Getting correct label
            label = file.split('.')[0].split('_')[2]
            label = int(label)
            label_text = df[ld2[label]]

            #Image preprocessing, including upsampling/downsampling
            img_cropped = crop_square(img)
            img_r1 = img_cropped.resize(downsample_size)
            img_r2 = img_r1.resize((224,224))
            x = image.img_to_array(img_r2)
            x = np.expand_dims(x, axis=0)
            x = tf.convert_to_tensor(x)
            
            #Runnning model
            x = preprocess_input(x)
            preds = model.predict(x)
            prediction = decode_predictions(preds, top=1)[0][0]
            if label_text.lower() == prediction[1].lower():
                counter += 1

        print('Accuracy is {:.2f}%, while downsample size is {}'.format(counter/len(filelist)*100, 
                                                                downsample_size))
    