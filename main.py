from flask import Flask, render_template, request
import face_recognition
import numpy as np
import os

app = Flask(__name__)

# Load the saved encodings
encodings = np.load('encodings.npy')
names = np.load('names.npy')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['image']
    img_path = os.path.join('uploads', file.filename)
    file.save(img_path)
    
    # Load image and get face encodings
    image = face_recognition.load_image_file(img_path)
    face_encoding = face_recognition.face_encodings(image)
    
    if not face_encoding:
        return "No face detected"
    
    face_encoding = face_encoding[0]
    
    # Compare face with known encodings
    matches = face_recognition.compare_faces(encodings, face_encoding)
    
    # Check for the most likely match
    if True in matches:
        match_index = matches.index(True)
        predicted_name = names[match_index]
        return f"Predicted Celebrity: {predicted_name}"
    else:
        return "No match found"
    
if __name__ == '__main__':
    app.run(debug=True)
