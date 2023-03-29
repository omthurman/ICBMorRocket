import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import os
from PIL import Image
import shutil 




def predict_image(img_path):
    def convert_to_jpg(file_path):
        file_dir, file_name = os.path.split(file_path)
        file_name, ext = os.path.splitext(file_name)
        if ext.lower() != ".jpg":
            # Convert image to JPEG format
            img = Image.open(file_path)
            jpg_file_path = os.path.join(file_dir, f"{file_name}.jpg")
            img.convert('RGB').save(jpg_file_path)
            return jpg_file_path
        else:
            return file_path

    img_path = convert_to_jpg(img_path)

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
    # img_path = './missile.jpg'  # Replace with the path to your image
    predicted_category, certainty = predict_image(model, img_path)
    return(predicted_category,certainty*100)