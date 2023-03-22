#!/usr/bin/env python3
from PIL import Image
import os

# Define the path to the dataset directory
dataset_path = '/home/nansi/limasphere-engines/the-eye-of-limasphere/datasets'

# Define a list of labels fr each class of image
labels = ['healthy', 'pest', 'disease']

# load the images and labels for each class of image
data = []
for label in labels:
    label_path = os.path.join(dataset_path, label)
    for filename in os.listdir(label_path):
        img_path = os.path.join(label_path, filename)
        img = Image.open(img_path)
        img = img.resize((224, 224)) # Resize the image to 224x224 pixels
        data.append((img, label))
        
# split the data into training, validation, and testing sets
training_data = data[:int(0.7*len(data))]
validation_data = data[int(0.7*len(data)):int(0.85*len(data))]
test_data = data[int(0.85*len(data)):]

print(len(training_data))
print(len(validation_data))
print(len(test_data))