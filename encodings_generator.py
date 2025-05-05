import face_recognition
import os
import numpy as np

# Path to your dataset
dataset_path = 'Celebrity_Faces_Dataset'

# List to store encodings and labels
encodings = []
names = []

# Loop through the dataset and extract features
celebrity_folders = os.listdir(dataset_path)

# Track progress
total_images = sum([len(files) for folder in celebrity_folders for files in os.walk(os.path.join(dataset_path, folder))])
processed_images = 0

for celebrity_name in celebrity_folders:
    celebrity_path = os.path.join(dataset_path, celebrity_name)
    if os.path.isdir(celebrity_path):
        print(f"Processing {celebrity_name}...")
        for img_name in os.listdir(celebrity_path):
            img_path = os.path.join(celebrity_path, img_name)
            try:
                image = face_recognition.load_image_file(img_path)
                encoding = face_recognition.face_encodings(image)
                
                if encoding:  # If a face encoding is found
                    encodings.append(encoding[0])
                    names.append(celebrity_name)

                processed_images += 1
                print(f"Processed {processed_images}/{total_images} images...")
            except Exception as e:
                print(f"Error processing {img_path}: {e}")

# Save the data for future use
np.save('encodings.npy', encodings)
np.save('names.npy', names)

print("Finished processing all images!")
