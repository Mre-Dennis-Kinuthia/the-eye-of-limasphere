## the-eye-of-limasphere
Cnn application for pest and desease identification with a remedy engine intergrated

### Image Loading and Preprocessing Script

This script loads a dataset of images from a specified directory, resizes them to a fixed size, and splits the data into training, validation, and testing sets. It is intended for use in machine learning projects, specifically for image classification tasks.

Prerequisites
The script requires the following Python packages to be installed:

PIL (Python Imaging Library)
os
Usage
To use the script, follow these steps:

Set the dataset_path variable to the path of the directory containing the image dataset.
Define a list of labels for each class of image in the dataset.
Run the script.
The script will load all images from the specified directory, resize them to 224x224 pixels using PIL, and associate each image with a label based on the subdirectory that it is located in. It will then split the data into training, validation, and testing sets, where 70% of the data is used for training, 15% for validation, and 15% for testing.

The resulting training_data, validation_data, and test_data lists can be used to train, validate, and test a machine learning model for the image classification task.

Authors
Your Name
License
This project is licensed under the MIT License.
