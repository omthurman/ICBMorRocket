import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from sklearn.model_selection import train_test_split

# Set image and dataset parameters
image_size = 256
batch_size = 32
epochs = 100

# Load and preprocess the images
def load_images(data_dir, categories):
    data = []
    labels = []
    for i, category in enumerate(categories):
        path = os.path.join(data_dir, category)
        for img_name in os.listdir(path):
            img_path = os.path.join(path, img_name)
            img = tf.keras.preprocessing.image.load_img(img_path, target_size=(image_size, image_size))
            img_array = tf.keras.preprocessing.image.img_to_array(img)
            data.append(img_array)
            labels.append(i)
    return np.array(data), np.array(labels)

data_dir = './data'  # Replace with the path to your dataset
categories = ['falcon', 'missile']
data, labels = load_images(data_dir, categories)

# Normalize the images
data = data / 255.0

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

# Create data augmentation generator
train_datagen = ImageDataGenerator(
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Fit the generator to the training data
train_datagen.fit(x_train)

# Create the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(image_size, image_size, 3)),
    MaxPooling2D(2, 2),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(len(categories), activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model with data augmentation
model.fit(train_datagen.flow(x_train, y_train, batch_size=batch_size),
          steps_per_epoch=len(x_train) // batch_size,
          epochs=epochs,
          validation_data=(x_test, y_test))

# Save the model
model.save('falcon_missile_classifier.h5')

# Function to predict a single image
def predict_image(model, img_path):
    img = tf.keras.preprocessing.image.load_img(img_path, target_size=(image_size, image_size))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    prediction = model.predict(img_array)
    return categories[np.argmax(prediction)]

# Example: Predict a single image
img_path = './example.jpg'  # Replace with the path to your image
print(f'Prediction: {predict_image(model, img_path)}')