import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
from PIL import Image
import shutil 

# Set image parameter
image_size = 256

# Load the model
model = load_model('falcon_missile_classifier.h5')

# Function to predict a single image
def predict_image(model, img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(image_size, image_size))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    predicted_category_index = np.argmax(prediction)
    certainty = prediction[0][predicted_category_index]
    return categories[predicted_category_index], certainty

# Categories for prediction
categories = ['falcon', 'missile']

# Example: Predict a single image
img_path = './missile.jpg'  # Replace with the path to your image
predicted_category, certainty = predict_image(model, img_path)
print(f'Prediction: {predicted_category} (Certainty: {certainty*100:.2f}%)')