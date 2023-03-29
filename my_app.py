from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from predict import predict_image

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png', 'gif'}

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/api/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if True:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        # load in model here.
        prediction,probability=predict_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print(prediction,probability)
        
        

        return jsonify({"message": "Image uploaded successfully", "filename": filename, "prediction":prediction, "probability":probability}), 201

    return jsonify({"error": "File type not allowed"}), 400


@app.route('/api/data', methods=['POST'])
def get_data():
    received_data = request.get_json()
    print(f"Received data: {received_data}")

    response = {
        "message": "Data received successfully!",
        "data": received_data
    }

    return jsonify(response), 200

@app.route('/uploads/<filename>')
def send_image(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(debug=True)