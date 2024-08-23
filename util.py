import os
import cv2
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array
import pandas as pd
from ast import literal_eval

def preprocess_image(image_path):
    """
    Loads, resizes, and converts an image to a NumPy array.

    Args:
        image_path: Path to the image file.

    Returns:
        A preprocessed image as a NumPy array.
    """
    IMG_WIDTH = 224  # Desired width (adjust as needed)
    IMG_HEIGHT = 224 # Desired height (adjust as needed)
    # Load the image
    img = cv2.imread(image_path)

    # Resize the image
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))

    # Convert to RGB (if not already)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Convert to array and normalize (important for most models)
    img_array = img_to_array(img) / 255.0 

    return img_array

# def load_data_from_csv(csv_file):
#     df = pd.read_csv(csv_file)
#     df['image'] = df['image'].apply(literal_eval) # Convert string representation back to list
#     X = np.array(df['image'].tolist())
#     y = df['label'].values
#     return X, y