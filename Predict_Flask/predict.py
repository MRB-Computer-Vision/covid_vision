#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:39:40 2020

@author: Julio Chilela and Lirio Ramalheira
"""
from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)
app.config["IMAGE_UPLOADS"] = "/Users/juliogabrielchilela1/Documents/Angola Cables/Covid19-AI/Respira_Brasil/"

# shows a list of all todos, and lets you POST to add new tasks
class predicting(Resource):

    def get(self):
        import os #
        os.chdir("/Users/juliogabrielchilela1/Documents/Angola Cables/Covid19-AI/Respira_Brasil/") # Path to the Folder
        
        from keras.preprocessing import image
        import numpy as np
        #Importing the library. Keras
        import tensorflow as tf 
        import json
        loaded_model = tf.keras.models.load_model('modelo/model1.h5', custom_objects={"custom_loss": 'accuracy'}, compile=False)
        loaded_model.compile(optimizer='adam', loss='accuracy')
        summary = str(loaded_model.to_json()) 
        #print(loaded_model.summary())

        return json.dumps(summary, indent=4, sort_keys=True)

    
    def post(self):
        
        import os #
        os.chdir("/Users/juliogabrielchilela1/Documents/Angola Cables/Covid19-AI/Respira_Brasil/") # Path to the Folder
        
        from keras.preprocessing import image
        import numpy as np
        #Importing the library. Keras
        import tensorflow as tf 
        loaded_model = tf.keras.models.load_model('modelo/model1.h5', custom_objects={"custom_loss": 'accuracy'}, compile=False)
        loaded_model.compile(optimizer='adam', loss='accuracy')
        
        #print(loaded_model.summary())
        # dimensions of our images
        img_width, img_height = 224, 224
        
        
        
        img = request.files["image"]

        img.save(os.path.join(app.config["IMAGE_UPLOADS"], img.filename))
        
        
        #imagefile = request.files('imagefile', '')
        
        img = image.load_img(img, target_size=(img_width, img_height))
        
        #img = image.load_img('dados-teste/c6844aa5-d3ae-4aa3-ace1-d358c469f9f4.png', target_size=(img_width, img_height))
        
        #img = image.load_img('dados-teste/covid-19-pneumonia-23-day9.jpg', target_size=(img_width, img_height))

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        images = np.vstack([x])
        import json
        classes = loaded_model.predict(images, batch_size=32)
        novaString = " Covid = "  + str(classes[0][0])  +  " | " + "No-COVID = " + str(classes[0][1])
        
        return str(novaString)


api.add_resource(predicting, '/predicting', methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)



"""
import os #
os.chdir("/Users/juliogabrielchilela1/Documents/Angola Cables/Covid19-AI/Respira_Brasil/") # Path to the Folder

from keras.preprocessing import image
import numpy as np

#classifierLoad = tf.keras.models.load_model('modelo/model1.h5')


#loaded_model.compile(optimizer='adam', loss='accuracy')
# Load the model while also loading optimizer and compiling (failing with "Unkown loss function: my_custom_loss")
#loaded_model = tf.keras.model.load('modelo/model1.h5', custom_objects={"custom_loss": 'accuracy'}) # compile is set to True by default


#Importing the library. Keras
import tensorflow as tf 
loaded_model = tf.keras.models.load_model('modelo/model1.h5', custom_objects={"custom_loss": 'accuracy'}, compile=False)
loaded_model.compile(optimizer='adam', loss='accuracy')

print(loaded_model.summary())
# dimensions of our images
img_width, img_height = 224, 224

img = image.load_img('dados-teste/COVID-00030.jpg', target_size=(img_width, img_height))

img = image.load_img('dados-teste/c6844aa5-d3ae-4aa3-ace1-d358c469f9f4.png', target_size=(img_width, img_height))

img = image.load_img('dados-teste/covid-19-pneumonia-23-day9.jpg', target_size=(img_width, img_height))

x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)


images = np.vstack([x])
classes = loaded_model.predict(images, batch_size=32)
print (classes)


"""