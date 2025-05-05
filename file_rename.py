import os

dataset_folder = 'Celebrity_Faces_Dataset'

for folder_name in os.listdir(dataset_folder):
    folder_path = os.path.join(dataset_folder, folder_name)
    
    if os.path.isdir(folder_path):
        images = [f for f in os.listdir(folder_path) if f.endswith('.jpeg')]
        
        for idx, image_name in enumerate(images, start=1):
            new_name = f"{folder_name}_{idx}.jpeg"
            old_image_path = os.path.join(folder_path, image_name)
            new_image_path = os.path.join(folder_path, new_name)
            
            os.rename(old_image_path, new_image_path)
            print(f"Renamed: {image_name} -> {new_name}")
